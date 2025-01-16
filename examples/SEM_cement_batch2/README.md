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
Make sure that you are in the folder where you want your environment.

- On Linux:

      envname=semdemo
      cd examples/SEM_cement_batch2
      python3 -m venv $envname
      source $envname/bin/activate

- On Windows PowerShell:

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

[generate an SSH key]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
[add an SSH key]:  https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
[input/]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/sem-example/examples/SEM_cement_batch2/input/
