"""Test storage plugin for compressive strength."""

from pathlib import Path

import pytest

import dlite

pytest.importorskip("pandas")
pytest.importorskip("openpyxl")


rootdir = Path(__file__).resolve().parent.parent
datamodeldir = rootdir / "Concrete" / "datamodels"
plugindir = rootdir / "Concrete" / "plugins"
datadir = rootdir / "Concrete" / "example_data"
outdir = rootdir / "tests" / "output"

dlite.python_storage_plugin_path.append(plugindir)


# if True:
def test_compressive_strength():
    inst = dlite.Instance.from_location(
        driver="CompressiveStrength",
        location=datadir / "compressive_strength.xlsx",
    )

    inst.save("CompressiveStrength", location=outdir / "tmp.xlsx")

    assert (outdir / "tmp.xlsx").exists()
