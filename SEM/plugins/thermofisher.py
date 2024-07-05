from pathlib import Path
import dlite

import configparser
from PIL import Image
from PIL.TiffTags import TAGS

class ThermoFisherStorage(dlite.DLiteStorageBase):
    """DLite storage plugin for a ThermoFisher SEM image."""

    with open(Path(__file__).resolve().parent.parent / "datamodels" /
          "ThermoFisher.json", "r") as f:
        ThermoFisher = dlite.Instance.from_json(f.read())

    def open(self, location, options=None):
        """Opens ThermoFisher metadata

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
        # 34682 -> ThermoFisher, 256 -> ImageWidth, ...
        TAGS[34682] = "ThermoFisher"
        with Image.open(self.location) as img:
            metadata = {}
            for key in img.tag:
                new_key = TAGS[key]
                metadata[new_key] = img.tag[key]

        # ThermoFisher metadata is parsed differently
        # It is stored in INI format
        if "ThermoFisher" not in metadata:
            raise Exception("ThermoFisher metadata not found")

        metadata["ThermoFisher"] = list(metadata["ThermoFisher"])
        for i in range(1):#len(metadata["ThermoFisher"])):
            ini_str = metadata["ThermoFisher"][i]
            config_metadata = ThermoFisherStorage.parse_ini(ini_str)
            metadata["ThermoFisher"][i] = config_metadata

        # From dict to DLite instance
        inst = self.ThermoFisher(id=id)
        for key1 in metadata["ThermoFisher"][0]:
            for key2 in metadata["ThermoFisher"][0][key1]:
                key = (key1 + key2).lower()
                value = metadata["ThermoFisher"][0][key1][key2]
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
