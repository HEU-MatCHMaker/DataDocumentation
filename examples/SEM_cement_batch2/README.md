Example of documenting a series of SEM datasets
===============================================

This example shows how to populate a knowledge base with a series of SEM datasets and related resources.

Setup
-----

This demo assumes that you have git and Python installed.

Clone the MatCHMaker DataDocumentation GitHub repository.

**NB!** This is a private repo, so you must have added an ssh-key to GitHub.
How to [generate an SSH key] and [add an SSH key] is well described on GitHub.

    git clone git@github.com:HEU-MatCHMaker/DataDocumentation.git
    cd DataDocumentation

For now, switch the example branch:

    git fetch origin sem-example
    git checkout sem-example

Create a virtual Python environment for this demo and activate it.
This is done slightly different on Linux (incl. WSL) and Windows PowerShell:

- Linux:

      envname=semdemo
      cd examples/SEM_cement_batch2
      python3 -m venv $envname
      source $envname/bin/activate

- Windows PowerShell:

      $envname = "semdemo"  # Windows PowerShell
      cd examples/SEM_cement_batch2
      python3 -m venv $envname
      ".\${envname}\Scripts\activate.bat"  # Windows PowerShell

Install required Python packages

    pip install -U pip
    pip install -r requirements.txt

Document the SEM datasets and related resources
-----------------------------------------------

The following types of resources will be documented:

- SEM datasets consisting of two files; a .tiff (image data) and a .txt (instrument metadata).
- A dataset, that is a series of the above SEM datasets.
- Investigated samples.
- OTEIO parsers and generators.

The [input/] folder contain CSV files with documentation for each resource type.

The CSV files has a header row with keywords. The available keywords and their meaning is described in the list of [pre-defined keywords] in the [tripper documentation].

In addition this example uses a few custom keywords defined in the [context.json] file.
Their have the following meaning:
- **fromSample**: Relates an experimental dataset to the sample (material object) its was acquired from.
- **magnification**: The magnification of the microscope (for imaging).
- **highVoltage_kV**: The acceleration voltage of the microscope in kV.
- **positionNo**: Index of the image in a map composed of several images. Should be further defined...
- **hasComposition**: Relates a sample to a dataset describing its composition.


### Working against an in-memory knowledge base

For now we will work against an in-memory knowledge base stored in a local file named `kb.ttl`.

Document all the different types of resources in the [input/] folder:

    datadoc add input/samples.csv --context=input/context.json --dump=kb.ttl
    datadoc --parse=kb.ttl add input/parsers.csv --context=input/context.json --dump=kb.ttl
    datadoc --parse=kb.ttl add input/series.csv --context=input/context.json --dump=kb.ttl
    datadoc --parse=kb.ttl add input/datasets.csv --context=input/context.json --dump=kb.ttl

Take a look at the generated knowledge base:

    less kb.ttl  # Use more in Windows PowerShell

List IRIs of all SEM image datasets:

    datadoc --parse=kb.ttl find --type=sem:SEMImage

Show detailed documentation of dataset `https://he-matchmaker.eu/data/sem#77600-23-001_15kV_400x_m001` (as json):

    datadoc --parse=kb.ttl find --criteria "@id=semdata:77600-23-001_15kV_400x_m001" --format=json

List IRIs of all resources who's title contain the word "Heidelberg":

    datadoc --parse=kb.ttl find --criteria "dcterms:title~=Heidelberg"

List IRIs of all samples

    datadoc --parse=kb.ttl find --type chameo:Sample

Access a documented dataset (does not handle sftp credentials yet...):

    datadoc --parse=kb.ttl fetch semdata:77600-23-001_15kV_400x_m001 --output=77600-23-001_15kV_400x_m001.zip

### Working against GraphDB hosted by SIMAVI

Repeat the above example, but work against the SIMAVI GraphDB instance.

[generate an SSH key]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
[add an SSH key]:  https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
[input/]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/sem-example/examples/SEM_cement_batch2/input/
[pre-defined keywords]: https://emmc-asbl.github.io/tripper/latest/datadoc/keywords/
[tripper documentation]: https://emmc-asbl.github.io/tripper/latest/
[context.json]: input/context.json
