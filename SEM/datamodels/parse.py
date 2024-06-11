import configparser
from PIL import Image
from PIL.TiffTags import TAGS

# Add new tags to TIFF
TAGS[34682] = "ThermoFischer"
TAGS[34118] = "Zeiss"

def parse_metadata(fname):
    """
    Parse metadata from .tif image using the Tiff standard tags
    """
    # Store img metadata with semantic tags, for example,
    # 34682 -> ThermoFischer
    with Image.open(fname) as img:
        metadata = {}
        for key in img.tag:
            new_key = TAGS[key]
            metadata[new_key] = img.tag[key]

    # ThermoFischer metadata is parsed differently
    # It is stored in INI format
    if "ThermoFischer" in metadata:
        metadata["ThermoFischer"] = list(metadata["ThermoFischer"])
        for i in range(len(metadata["ThermoFischer"])):
            ini_str = metadata["ThermoFischer"][i]
            config_metadata = parse_ini(ini_str)
            metadata["ThermoFischer"][i] = config_metadata


    # Zeiss metadata is parsed differently
    # It is stored in a non-intuitive format, with every other line being a
    # a configuration, a lot of unused values.
    # The header is an array of numbers.
    if "Zeiss" in metadata:
        metadata["Zeiss"] = list(metadata["Zeiss"])
        for i in range(len(metadata["Zeiss"])):
            string = metadata["Zeiss"][i]
            new_string = string.splitlines()
            array = new_string[:35]
            unused = new_string[35::2]
            config = new_string[36::2]

            # In Zeiss config, configuration is stored as key = value,
            # except for Date/Time, which is stored as key :value
            config_dict = {}
            for line in config:
                print(line)
                try:
                    key, value = line.split(" = ")
                except:
                    key, value = line.split(" :")
                config_dict[key] = value

            config_dict["ARRAY"] = array
            config_dict["UNUSED"] = unused

            metadata["Zeiss"][i] = config_dict

    return metadata


def parse_ini(ini_str : str):
    """
    Example of how a .INI file might be parsed in Python.
    Here from .INI to dict, which can be converted to many other formats.
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


def read_ini(fname : str):
    """
    Example of how a .INI file might be parsed in Python.
    Here from .INI to dict, which can be converted to many other formats.
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


def read_jeol(fname):
    """
    JEOL metadata .txt files are stored in encoding ISO-8859 as
        $CM_FORMAT Bitmap
        ...
    """
    metadata = {}
    with open(fname, "r", encoding="ISO-8859-1") as f:
        for line in f.readlines():
            try:
                key, value = line.split(maxsplit=1)
                metadata[key] = value.strip()
            except:
                key, = line.split(maxsplit=1)
                metadata[key] = ""

    return metadata



if __name__ == "__main__":
    metadata = parse_metadata("(ThermoFischer) pos1_01_grid_200x.tif")
    #metadata = parse_metadata("(Zeiss) 0,5k 2 high.tif")
    #metadata = parse_metadata("(Hitachi) 15_m001.tif")
    #metadata["Hitachi"] = read_ini("(Hitachi) 15_m001.txt")
    #metadata = read_jeol("(JEOL) Exp_Reference 6005 T6 05.txt")
    for k in metadata:
        print(k)
        print(metadata[k])
        print()
