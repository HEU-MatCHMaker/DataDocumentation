from pathlib import Path
import dlite

import configparser
from PIL import Image
from PIL.TiffTags import TAGS


class HitachiStorage(dlite.DLiteStorageBase):
    """DLite storage plugin for a Hitachi SEM image."""

    with open(Path(__file__).resolve().parent.parent /
          "Hitachi.json", "r") as f:
        Hitachi = dlite.Instance.from_json(f.read())

    def open(self, location, options=None):
        """Opens Hitachi metadata

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
            A new Hitachi instance with the loaded metadata
        """

        # Crash early if the file is not tif
        extension = self.location.rsplit('.', 1)[1]
        if extension.lower() != "tif":
            raise Exception("File extension must be .tif")

        # Store img metadata with semantic tags
        with Image.open(self.location) as img:
            metadata = {}
            for key in img.tag:
                new_key = TAGS[key]
                metadata[new_key] = img.tag[key]

        # Hitachi metadata is parsed differently
        # It is stored in INI format in a different file
        config_fname = self.location.rsplit('.', 1)[0] + ".txt"
        try:
            metadata["Hitachi"] = HitachiStorage.read_ini(config_fname)
        except:
            raise Exception(f"Did not find metadata file: {config_fname}")

        # From dict to DLite instance
        inst = self.Hitachi(id=id)
        for key1 in metadata["Hitachi"]:
            for key2 in metadata["Hitachi"][key1]:
                key = (key1 + key2).lower()
                value = metadata["Hitachi"][key1][key2]
                inst.set_property(key, value)

        return inst


    @staticmethod
    def read_ini(fname : str):
        """
        Parse a INI file from file to dict.
        """
        config = configparser.ConfigParser()
        config.read(fname)

        # Convert to dict
        metadata = dict()
        sections = config.sections()
        for section in sections:
            items = config.items(section)
            metadata[section] = dict(items)

        return metadata
