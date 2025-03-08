"""DLite storage plugin for MatCHMaker compressive strength

This plugin can parse an Excel file into an instance of the
CompressiveStrength datamodel and serialises the instance back to
Excel.

"""
import re
from pathlib import Path

import pandas as pd

import dlite
from dlite.options import Options


thisdir = Path(__file__).resolve().parent
datamodeldir = (thisdir / ".." / "datamodels").resolve()

dlite.storage_path.append(datamodeldir)


class CompressiveStrength(dlite.DLiteStorageBase):
    """DLite storage plugin for MatCHMaker compressive strength."""

    datamodel = "http://onto-ns.com/meta/cement/0.1/CompressiveStrength"

    def open(self, location, options=None):
        """Opens `location`.

        Arguments:
            location: Path to xlsx file.
            options:

              - sheet_name: Sheet name or number to load. Default: 0
              - header: Index of the header row (first row has index 0).
                Default: 1
              - nrows: Number of rows following the header row to parse.
                Default: all remaining rows
              - decimal: Character to recognise as decimal point. Default: .

        """
        opts = Options(options, defaults="header=1;decimal=.")
        self.location = location

        sn = opts.get("sheet_name")
        self.loadkw = {
            "sheet_name": 0 if sn is None else int(sn) if sn.isdigit() else sn,
            "header": int(opts.header),
            "decimal": opts.decimal,
        }
        if "nrows" in opts:
            self.loadkw["nrows"] = int(opts.nrows)

        self.savekw = {
            "index": False,
            "startrow": int(opts.header),
        }
        if sn is not None:
            self.savekw["sheet_name"] = sn

    def load(self, id=None):
        """Load compressive strength.

        If `id` is given, the ID of the returned instance will be `id`.
        Otherwise it will be a random UUID.
        """
        frame = pd.read_excel(self.location, **self.loadkw)
        data = frame.to_numpy()
        rows, cols = frame.shape
        header = list(frame.columns.values)
        nX = sum(1 for h in header if h.upper().startswith("X"))
        nS = cols - nX
        stacked = cols == nX + 2 and "time" in header[nX].lower()
        mult = 1 if stacked else nS

        meta = dlite.get_instance(self.datamodel)
        inst = meta(dimensions={"nX": nX, "nmeasurements": mult*rows})
        inst.X = data[:, :nX].repeat(mult, 0)
        if stacked:
            inst.curing_time = data[:, -2]
            inst.mortar_strength = data[:, -1]
        else:
            hi = 0
            for i in range(nS):
                lo = hi
                hi += rows
                m = re.match(".*[^0-9]([0-9]+)[dD]", header[nX+i])
                if m:
                    inst.curing_time[lo:hi] = int(m.groups()[0])
                elif nS == 4:
                    inst.curing_time[lo:hi] = [1, 2, 7, 28][i]
                else:
                    raise RuntimeError(
                        "cannot determine curing time from "
                        f"'{self.location}' column {nX+i} ({header[nX+i]})"
                    )
                inst.mortar_strength[lo:hi] = data[:, nX+i]

        return inst

    def save(self, inst):
        """Save `inst` to excel."""
        d = {f"X{i}": inst.X[:,i] for i in range(inst.nX)}
        d["curing_time(Day)"] = inst.curing_time
        d["mortar_strength(MPa)"] = inst.mortar_strength
        frame = pd.DataFrame(d)
        frame.to_excel(self.location, **self.savekw)
