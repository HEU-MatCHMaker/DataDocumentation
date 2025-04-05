# Documenting a CHADA workflow


![CHADA workflow](figs/SEM-CHADA-bpmn_diagram.png)

Figure 1. BPMN diagram for the CHADA workflow.


![CHADA workflow](figs/SEM-CHADA-bpmn_legend.png)

Figure 2. Explanation of symbols in the above BPMN diagram.


## Setting up the graph database

### Setup of python environment

Create a virtual Python environment for this demo and activate it.
Make sure that you are in the folder where you want your environment.

    # choose your desired environment name
    envname=pinkdemo  # Linux
    $envname = "pinkdemo"  # Windows PowerShell
    python3.X -m venv ${envname}  # you probably have to choose python version
    source ${envname}/bin/activate  # Linux
    ".\${envname}\Scripts\activate.bat" # Windows PowerShell
    pip install ipython  # If you want to use ipython

Install tripper

    pip install -U pip
    pip install "tripper[datadoc] @ git+https://github.com/EMMC-ASBL/tripper.git@master"

For handling of username and password

    pip install keyring
    # This is the simplest cross-platform keyring, more secure version exist
    pip install keyrings.alt

NB! In Windows Powershell you will get an error as the folder with the
scripts is not in the PATH.  You can fix this in the current session
as shown below.  Note that the first ';' is crucial

    $env:Path += ';C:\path\displayed\in\the\warning'

The development version of tripper from the `master` branch together
with extra dependencies for data documentation is now installed.

Clone the DataDocumentation folder to where you want.

    git clone git@github.com:HEU-MatCHMaker/DataDocumentation.git
    cd DataDocumentation/examples/CHADA-workflow


### Prepare your local triplestore

For demonstration and easy testing purposes it is useful to set up a
local triplestore on your machine.  Choice of triplestore is up to
you, but we suggest fuseki which can be set up as follows:

```bash
docker pull stain/jena-fuseki
docker run -d --name fuseki -p 3030:3030 -e ADMIN_PASSWORD=admin0 \
  -e=FUSEKI_DATASET_1=test_repo stain/jena-fuseki
```

Since adding the password everytime is timeconsuming you can create a
configuration file for tripper.
Create a file in ~/.config/tripper/session.yaml with the following content:

```yaml
FusekiTest:
  backend: sparqlwrapper
  base_iri: http://localhost:3030/test_repo
  update_iri: http://localhost:3030/test_repo/update
  username: admin
  password: admin0
```

You are now ready to populate and search your knowledge base.

The triplestore can be browsed online by going to localhost:3030.
Note that the browser cannot have pop-up windoes
blocked, as FUSEKI used a pop-up window for authentication.

## Populate your triplestore

First we can check that the triplestore is empty:

```bash
datadoc --triplestore FusekiTest find
```

If nothing it returned, it means that the triplestore is empty.

We can now add the documentation:

```bash
# First add the datasets
datadoc --triplestore FusekiTest add input/datasets.csv --context input/matchmaker_context.json --dump ts.ttl

# Add the samples
datadoc --triplestore FusekiTest add input/material.csv --context input/matchmaker_context.json

# Add the processes
datadoc --triplestore FusekiTest add input/processes.csv --csv-option delimiter=, --context input/matchmaker_context.json
```


## Query the triplestore

List the IRI of all the documented resources:

```bash
$ datadoc -t FusekiTest find
https://he-matchmaker.eu/example/CHADA-workflow#sem_parameters
https://he-matchmaker.eu/example/CHADA-workflow#bse_image
https://he-matchmaker.eu/example/CHADA-workflow#eds_map
https://he-matchmaker.eu/example/CHADA-workflow#chem_comp_map
https://he-matchmaker.eu/example/CHADA-workflow#clustered_image
https://he-matchmaker.eu/example/CHADA-workflow#phase_fractions
https://he-matchmaker.eu/example/CHADA-workflow#material
https://he-matchmaker.eu/example/CHADA-workflow#unpolished_sample
https://he-matchmaker.eu/example/CHADA-workflow#uncoated_sample
https://he-matchmaker.eu/example/CHADA-workflow#sample
https://he-matchmaker.eu/example/CHADA-workflow#sem_characterisation
https://he-matchmaker.eu/example/CHADA-workflow#sample_extraction
https://he-matchmaker.eu/example/CHADA-workflow#sample_polishing
https://he-matchmaker.eu/example/CHADA-workflow#sample_inspection
https://he-matchmaker.eu/example/CHADA-workflow#sample_coating
https://he-matchmaker.eu/example/CHADA-workflow#parameter_adjustment
https://he-matchmaker.eu/example/CHADA-workflow#parameter_selection
https://he-matchmaker.eu/example/CHADA-workflow#beam_alignment
https://he-matchmaker.eu/example/CHADA-workflow#sem_image_acqusition
https://he-matchmaker.eu/example/CHADA-workflow#eds_mapping
https://he-matchmaker.eu/example/CHADA-workflow#bse_processing
https://he-matchmaker.eu/example/CHADA-workflow#bse_preprocessing
https://he-matchmaker.eu/example/CHADA-workflow#bse_postprocessing
https://he-matchmaker.eu/example/CHADA-workflow#eds_processing
https://he-matchmaker.eu/example/CHADA-workflow#eds_preprocessing
https://he-matchmaker.eu/example/CHADA-workflow#eds_postprocessing
https://he-matchmaker.eu/example/CHADA-workflow#result_analysis
```

Lets take a closer look at the documentation of the final result,
which is the `:phase_fractions` dataset.  We use the `--format` option
to specify that we want to list the result in JSON format

```bash
datadoc -t FusekiTest find --criteria @id=https://he-matchmaker.eu/example/CHADA-workflow#phase_fractions --format json
```

```json
[
  {
    "@id": "https://he-matchmaker.eu/example/CHADA-workflow#phase_fractions",
    "publisher": {
      "@type": [
        "http://xmlns.com/foaf/0.1/Agent",
        "https://w3id.org/emmo#EMMO_2480b72b_db8d_460f_9a5f_c2912f979046"
      ],
      "name": "MatCHMaker"
    },
    "theme": [
      "https://he-matchmaker.eu/",
      "https://w3id.org/emmo/domain/characterisation-methodology/chameo#ScanningElectronMicroscopy",
      "https://w3id.org/emmo/domain/theme/characterisation/SEM"
    ],
    "contactPoint": {
      "hasName": "Geoffrey Daniel",
      "@type": "http://www.w3.org/2006/vcard/ns#Kind"
    },
    "@type": [
      "http://onto-ns.com/meta/matchmaker/0.1/PhaseFractions",
      "http://www.w3.org/ns/dcat#Dataset",
      "https://w3id.org/emmo#EMMO_194e367c_9783_4bf5_96d0_9ad597d48d9a",
      "https://w3id.org/emmo/domain/sem#PhaseFractions"
    ],
    "distribution": {
      "mediaType": "https://www.iana.org/assignments/media-types/application/vnd.ms-excel",
      "@type": "http://www.w3.org/ns/dcat#Distribution"
    },
    "description": "Relative amount of the different phases in the sement",
    "title": "Phase fractions"
  }
]
```
