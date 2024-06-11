from pathlib import Path
import dlite
import glob

thisdir = Path(__file__).resolve().parent
dlite.python_storage_plugin_path.append(thisdir  / "plugins")

# ThermoFischer
inst1 = dlite.Instance.from_location("ThermoFischerStorage", "(ThermoFischer) pos1_01_grid_200x.tif")
print(inst1)

# Hitachi
inst2 = dlite.Instance.from_location("HitachiStorage", "(Hitachi) 15_m001.tif")
print(inst2)

# To test this, change to your corresponding path to SEM_cement_batch2
#cement_batch2_files = glob.glob("/mnt/c/Users/torha/SINTEF/HEU MatCHMaker - Dokumenter/WP2/SEM_cement_batch2/77600-23-001/*.tif")
#coll = dlite.Collection()
#for fname in cement_batch2_files[0:5]:
#    print(fname)
#    inst = dlite.Instance.from_location("HitachiStorage", fname)
#    coll.add(fname, inst)
#print(coll)
