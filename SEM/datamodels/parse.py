"""
Example of how a .INI file might be parsed in Python.
Here from .INI to dict, which can be converted to many other formats.

A [Default] header was added to the .INI file to make it compatible.
"""
import configparser

# Read INI
config = configparser.ConfigParser()
config.read('ThermoFischer_Apreo_SEM.INI')

# Convert to dict
metadata = dict()
sections = config.sections()
for section in sections:
    items = config.items(section)
    metadata[section] = dict(items)

print(metadata)
