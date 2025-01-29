from pathlib import Path
import dlite

rootdir = Path(__file__).resolve().parent.parent
print(rootdir)
dlite.python_storage_plugin_path.append(rootdir  / "plugins")

# ThermoFisher
fname1 = rootdir / "example_data" / "ThermoFisher_pos1_01_grid_200x.tif"
inst1 = dlite.Instance.from_location("ThermoFisherStorage", fname1)
print(inst1)

# Hitachi
fname2 = rootdir / "example_data" / "Hitachi_15_m001.tif"
inst2 = dlite.Instance.from_location("HitachiStorage", fname2)
print(inst2)

# To test this, change to your corresponding path to SEM_cement_batch2
#cement_batch2_files = glob.glob("/mnt/c/Users/torha/SINTEF/HEU MatCHMaker - Dokumenter/WP2/SEM_cement_batch2/77600-23-001/*.tif")
#with dlite.Storage("pyrdf", location="SEM_cement_batch2.rdf", options="mode=w;single=no") as s:
#    for fname in cement_batch2_files:
#        print(fname)
#        inst = dlite.Instance.from_location("HitachiStorage", fname)
#        s.save(inst)
