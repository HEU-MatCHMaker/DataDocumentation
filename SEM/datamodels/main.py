from pathlib import Path
import dlite

thisdir = Path(__file__).resolve().parent
dlite.python_storage_plugin_path.append(thisdir  / "plugins")
inst = dlite.Instance.from_location("ThermoFischerStorage", "(ThermoFischer) pos1_01_grid_200x.tif", options="mode=r")
print(inst)


print()
print()
print()
print()
print()

print("HELLO")
