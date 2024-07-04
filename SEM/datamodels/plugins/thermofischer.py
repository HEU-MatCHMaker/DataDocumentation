from pathlib import Path
import dlite

import configparser
from PIL import Image
from PIL.TiffTags import TAGS

# Add new tags to TIFF
TAGS[34682] = "ThermoFischer"

class ThermoFischerStorage(dlite.DLiteStorageBase):
    """DLite storage plugin for a ThermoFischer SEM image."""

    with open(Path(__file__).resolve().parent.parent /
          "ThermoFischer.json", "r") as f:
        ThermoFischer = dlite.Instance.from_json(f.read())

    def open(self, location, options=None):
        """Opens ThermoFischer metadata

        Arguments:
            location: Path to temperature profile data file.
            options: Additional options for this driver.  Unused.
        """
        self.location = location

    def load(self, id=None):
        """Reads storage into an new instance and returns the instance.

        Arguments:
            id: Optional URI to assign to the new instance.

        Returns:
            A new ThermoFisher instance with the loaded metadata
        """

        # Crash early if the file is not tif
        extension = self.location.rsplit('.', 1)[1]
        if extension.lower() != "tif":
            raise Exception("File extension must be .tif")

        # Store img metadata with semantic tags, for example,
        # 34682 -> ThermoFischer
        with Image.open(self.location) as img:
            metadata = {}
            for key in img.tag:
                new_key = TAGS[key]
                metadata[new_key] = img.tag[key]

        # ThermoFischer metadata is parsed differently
        # It is stored in INI format
        if "ThermoFischer" not in metadata:
            raise Exception("ThermoFischer metadata not found")

        metadata["ThermoFischer"] = list(metadata["ThermoFischer"])
        for i in range(1):#len(metadata["ThermoFischer"])):
            ini_str = metadata["ThermoFischer"][i]
            config_metadata = ThermoFischerStorage.parse_ini(ini_str)
            metadata["ThermoFischer"][i] = config_metadata

        # From dict to DLite instance
        inst = self.ThermoFischer(id=id)
        for key1 in metadata["ThermoFischer"][0]:
            for key2 in metadata["ThermoFischer"][0][key1]:
                key = (key1 + key2).lower()
                value = metadata["ThermoFischer"][0][key1][key2]
                inst.set_property(key, value)

        return inst


    @staticmethod
    def parse_ini(ini_str : str):
        """
        Parse a INI file from string to dict.
        """
        config = configparser.ConfigParser()
        config.read_string(ini_str)

        # Convert to dict
        metadata = dict()
        sections = config.sections()
        for section in sections:
            items = config.items(section)
            metadata[section] = dict(items)

        return metadata


