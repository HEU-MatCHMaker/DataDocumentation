from pathlib import Path
import dlite

thisdir = Path(__file__).resolve().parent
dlite.python_storage_plugin_path.append(thisdir  / "plugins")

# ThermoFischer
inst1 = dlite.Instance.from_location("ThermoFischerStorage", "(ThermoFischer) pos1_01_grid_200x.tif", options="mode=r")
print(inst1)

# Hitachi
inst2 = dlite.Instance.from_location("HitachiStorage", "(Hitachi) 15_m001.tif", options="mode=r")
print(inst2)
