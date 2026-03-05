# Semantic documentation of tools, datasets and workflows

This example is intended to be a simple guide for how to step-by-step semantically document software tools, datasets and workflows.

The aim of the documentation is to enhance reusability by providing context in the form of [linked data], that relates the various resources to each other using relations with semantically well-defined meaning.

- [Important underlying principles](#important-underlying-principles)
  - [Individuals versus Classes](#individuals-versus-classes)
  - [Documenting the processes and their relationships to potential real datasets](#documenting-the-processes-and-their-relationships-to-potential-real-datasets)
  - [Documenting the actual datasets and executed workflows](#documenting-the-actual-datasets-and-executed-workflows)
- [How to do this in practice](#how-to-do-this-in-practice)
  - [1. Documentation of software tools](#1-documentation-of-software-tools)
  - [2. Documentation of related resources](#2-documentation-of-related-resources)
  - [3. Documentation of computation and dataset types](#3-documentation-of-computation-and-dataset-types)
  - [4. Documentation of actual datasets](#4-documentation-of-actual-datasets)
  - [5. Documentation of executed workflows](#5-documentation-of-executed-workflows)
  - [6. Documentation of content of datasets](#6-documentation-of-content-of-datasets)
-[List of templates](#list-of-templates)


## Important underlying principles ##

### Individuals versus Classes ###

We distinguish between individuals and classes.
Individuals are specific instances of a concept, while classes are general categories that can have multiple instances. For example, a specific software tool would be an individual, while the category of software tools would be a class.


### Documenting the processes and their relationships to potential real datasets ###

The figure below illustrates the documentation of software tools the type of computation they implements and the type of datasets it takes as input and output (step 1 to 3 under [How to do this in practice](#how-to-do-this-in-practice)).
Here a **computation class** is related to a **software individual** and the types of datasets (i.e. **dataset classes**) it takes as input and output.
It is important to realise that at this level of the documentation we focus on documenting the processes that we can run and their relationships to potential real datasets.


![Documentation of step 1 to 3.](https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/datadoc-example/examples/tools/figs/computation.svg)

### Documenting the actual datasets and executed workflows ###

Once the **types of**  proesses and datasets that we treat have been documented, it is possible to document actual datasets and workflows (step 4 and 5).
This principle on how the classes (the concepts) and individuals (actual instances) are related is shown in the figure below.

![Documentation of step 4 and 5.](https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/datadoc-example/examples/tools/figs/workflow.svg)


## How to do this in practice ##

The main interface for this semantic documentation is simple spreadsheets with well-defined column headers.
The names in the column headers are under the hood mapped to ontological concepts via a [JSON-LD] context.
However, a normal user is not exposed to the complexity of semantic technologies.
The important thing to understand is that these headers are not just arbitrary names, but they have a specific meaning in the context of semantic documentation.
Instead, the user is presented with a simple set of spreadsheet [templates].
Each documented resource will be a row in one of these templates.

Since the FAIR principles demand that all resources must have a globally [unique and persistent identifier], all the templates have a column labeled "@id".
This column should contain an IRI.
These IRIs can be written is as [URI]s, like <https://he-matchmaker.eu/resource/my_software>, or as compact URIs (so-called [CURIE]s), like mm:my_software,
where the prefix `mm` is a shorthand for the namespace <https://he-matchmaker.eu/resource/>, intended for MatCHMaker-owned resources.

For semantics, it is also important to document the type of the resource.
Hence, all templates also have a column labeled "@type".
The values in this column should also be an IRI identifying an ontological concept describing the type of the resource.
General values for the type are described in the following sections, which also explains how the templates should be filled out.


### 1. Documentation of software tools ###

For a minimal documentation of a software tool, the user should fill in table such as the one below.
See the [software template] for a more elaborate template.
Note that software tools are documented as individials in the ontology, and not as classes, since we are documenting specific instances of software tools, and not general categories of software tools.

| @id            | @type         | title       | description                   |
|----------------|---------------|-------------|-------------------------------|
| mm:my_software | emmo:Software | My Software | Description of my software... |

The expected values for each column are:

- **@id**: Unique persistent identifier, in the form of an [URI] or [CURIE].
- **@type**: Type of the software. In the general case, it could be `emmo:Software`, but if a more specialised subclass is known, it should be used. This must refer to a concept in an ontology, such as the [EMMO], and not to a free text string.
- **title**: Name or title of the software as a string.
- **description**: A human readable description of the software as a string.


### 2. Documentation of related resources ###

The minimal documentation in the previous section does not provide sufficient information to access and use it.
For that, we will add a few additional columns to our table:

| @id            | @type         | title       | description                   | rightsHolder              | license                                      | landingPage                                   |
|----------------|---------------|-------------|-------------------------------|---------------------------|----------------------------------------------|-----------------------------------------------|
| mm:my_software | emmo:Software | My Software | Description of my software... | <https://ror.org/0422tvz87> | <https://creativecommons.org/licenses/by/4.0/> | <https://github.com/HEU-MatCHMaker/my_software> |

Meaning of the extra columns:

- **rightsHolder**: URI to a person or organisation owning or managing rights over the software.
  You will typically refer to people by their [ORCID] or similar.
  Organisations may be referred to by their [ROR] ID or webpage URL.
- **license**: URL to a legal document under which the distribution is made available.
  If your software doesn't have a license yet, it is highly recommended that you give it a license.
  Without a clear license, it is not possible to use the software.
  See the this [list of standard open-source licenses] and the [license chooser].
- **landingPage**: URL to a web page that provides access to the software and/or additional information about it.

The [templates] folder includes a [template for agents][agents template].
In principle you will not need this table, since the agents referred to in, e.g. the *rightsHolder* column, should be fully documented by the site the URI is referring to.
However, the [agents template] may still be useful to fill out to ensure that we use a unique URI when referring to the same agent or in the case that the URI is not resolvable.


### 3. Documentation of computation and dataset types ###

As shown in the first figure on this page, we want to document the computation procedure and relate it to the software with which the computation is performed as well as to the types of datasets it takes as input and output.
As mentioned [above](#documenting-the-processes-and-their-relationships-to-potential-real-datasets), it is important to notice that we here want to document a computation procedure (that can be executed many times) and not a specific execution.
The same is the case for the dataset types.
It is not actual datasets we want to document, but the type of datasets that the computation takes as input and output.

Class-level documentation of computations:

| @id              | @type     | subClassOf       | label         | definition                                           | hasInput      | hasOutput     | isComputedBy   |
|------------------|-----------|------------------|---------------|------------------------------------------------------|---------------|---------------|----------------|
| mm:MyComputation | owl:Class | emmo:Computation | MyComputation | Definition of this specific computation procedure... | mm:MyDataset1 | mm:MyDataset2 | mm:my_software |

Class-level documentation of dataset types:

| @id           | @type     | subClassOf   | label      | definition               |
|---------------|-----------|--------------|------------|--------------------------|
| mm:MyDataset1 | owl:Class | emmo:Dataset | MyDataset1 | Definition of dataset 1. |
| mm:MyDataset2 | owl:Class | emmo:Dataset | MyDataset2 | Definition of dataset 2. |

Meaning of the columns:

- **@id**: Unique persistent identifier, in the form of an [URI] or [CURIE].
- **@type**: For class-level documentation, this should be [owl:Class].
- **subClassOf**: The superclass. This should be [emmo:Computation] and [emmo:Dataset] for the computations and datasets, respectively.
- **label**: A label for the class. Class labels are typically written in [UpperCamelCase].
- **definition**: A human readable definition of the class.
- **hasInput**: IRI of an input dataset type documented in the dataset types table.
- **hasOutput**: IRI of an output dataset type documented in the dataset types table.
- **isComputedBy**: IRI of a software documented in the software table that is executing this computation.


### 4. Documentation of actual datasets ###

W3C has created the [DCAT] vocabulary as a standard way to document datasets.
The documentation of datasets will be based on this vocabulary, but may extended with additional concepts needed for describing materials science datasets.

The table below shows a simple generic example of documentation of a few datasets.

| @id            | @type         | title     | description               | rightsHolder              | license                                      | creator                               | distribution.downloadURL                                                                                              |
|----------------|---------------|-----------|---------------------------|---------------------------|----------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| mm:my_dataset1 | mm:MyDataset1 | Dataset 1 | Description of dataset 1. | <https://ror.org/0422tvz87> | <https://creativecommons.org/licenses/by/4.0/> | <https://orcid.org/0000-0002-1560-809X> | <https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/master/examples/tools/data/dataset1.txt> |
| mm:my_dataset2 | mm:MyDataset2 | Dataset 2 | Description of dataset 2. | <https://ror.org/0422tvz87> | <https://creativecommons.org/licenses/by/4.0/> | <https://orcid.org/0000-0002-1560-809X> | <https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/master/examples/tools/data/dataset2.txt> |
| mm:my_dataset3 | mm:MyDataset3 | Dataset 3 | Description of dataset 3. | <https://ror.org/0422tvz87> | <https://creativecommons.org/licenses/by/4.0/> | <https://orcid.org/0000-0002-1560-809X> | <https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/master/examples/tools/data/dataset3.txt> |
| mm:my_dataset4 | mm:MyDataset4 | Dataset 4 | Description of dataset 4. | <https://ror.org/0422tvz87> | <https://creativecommons.org/licenses/by/4.0/> | <https://orcid.org/0000-0002-1560-809X> | <https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/master/examples/tools/data/dataset4.txt> |

It is often possible to generate the above table using a script that traverse the folder structure where you have your datasets are stored.

Most of the columns have already been described above, except for `creator` and `distribution.downloadURL`.
In addition to these, there are a set of common columns that also could be included:

- **creator**: URI of the person or organisation creating the dataset.
- **publisher**: URI of the person or organisation that makes the dataset available.
- **identifier**: A unique identifier (in addition to the `@id`) of the dataset.
- **distribution.accessURL**: URL of a resource that gives access to a distribution of the dataset. E.g. a landing page or feed or database.
- **distribution.accessService**: URL of a data service that gives access to the distribution of the dataset.
- **distribution.downloadURL**: URL of a downloadable file containing the dataset.
- **distribution.mediaType**: The media type of the distribution as defined by [IANA]. Example: [iana:text/csv].
- **distribution.format**: The file format of the distributed dataset. Use `distribution.mediaType` if the format is defined by [IANA].
- **version**: The version indicator (name or identifier) of a resource.
- **previousVersion**: IRI to the previous version of a resource.
- **status**: The status of the resource. Use one of the values: [stat:Completed], [stat:Deprecated], [stat:UnderDevelopment], [stat:Withdrawn].
- **conformsTo**: URI to an established standard to which the described resource conforms.
- **releaseDate**: Date of formal issuance (e.g., publication) of the resource. Written as 'YYYY-MM-DD', optionally followed by the time, e.g. "2026-03-05T21:20:12".


### 5. Documentation of executed workflows ###

At this stage, to document the full provenance of your workflows, all you need to do is to create a table with performed computation that lists the input and output datasets:

| @id                | @type             | description | hasInput       | hasOutput      |
|--------------------|-------------------|-------------|----------------|----------------|
| mm:my_computation1 | mm:MyComputation1 |             | mm:my_dataset1 | mm:my_dataset2 |
| mm:my_computation2 | mm:MyComputation2 |             | mm:my_dataset2 | mm:my_dataset3 |
| mm:my_computation3 | mm:MyComputation3 |             | mm:my_dataset3 | mm:my_dataset4 |

Like for step 4, this table can often be generated by the same script you used to generate the table of dataset individuals.


### 6. Documentation of content of datasets ###

To enable interoperability, you can document the datum (or properties) within your datasets by extending the table of dataset types from step 3.
From the added columns, it is possible to generate DLite data models that describes the internal structure of the datasets.

| @id           | @type     | subClassOf   | label      | definition               | datumName[1] | datumType[1] | datumUnit[1] | datumShape[1] | datumDescription[1]            | datumMapping[1]      | datumName[2] | datumType[2] | datumUnit[2] | datumShape[2] | datumDescription[2]       | datumMapping[2]      |
|---------------|-----------|--------------|------------|--------------------------|--------------|--------------|--------------|---------------|--------------------------------|----------------------|--------------|--------------|--------------|---------------|---------------------------|----------------------|
| mm:MyDataset1 | owl:Class | emmo:Dataset | MyDataset1 | Definition of dataset 1. | smiles       | string       |              |               | SMILES string of the molecule. | emmo:SMILESReference | mass         | float64      | u            |               | Atomic mass of molecule.  | emmo:Mass            |
| mm:MyDataset2 | owl:Class | emmo:Dataset | MyDataset2 | Definition of dataset 2. | bond_length  | float        | Å            | nbonds        | Length of each atomic bond.    | atomistic:BondLength | bond_energy  | float        | eV           | nbonds        | Bond energy of each bond. | atomistic:BondEnergy |

The meaning of the added columns are:

- **datumName**: A local name of the datum/property. Should be a string without spaces.
- **datumType**: Type of the datum/property. Use one of bool, int, float, string. For int and float the number of bits can be added. E.g. int32, float64.
- **datumUnit**: Unit of the datum/property. Leave empty if dimensionless.
- **datumShape**: Comma-separated list of the dimension names if the datum/property is multi-dimensional. Leave empty if it is a scalar.
- **datumDescription**: Human-readable description of the datum/property.
- **datumMapping**: IRI of the concept(s) in the ontology that defines the datum/property.


## List of templates ##

- [agents.csv](https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/agents.csv)
- [computations.csv](https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/computations.csv)
- [computation-classes.csv](https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/computation-classes.csv)
- [datasets.csv](https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/datasets.csv)
- [dataset-classes.csv](https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/dataset-classes.csv)
- [software.csv](https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/software.csv)


These templates can be extended with additional columns.
The [Tripper] documentation provides a list of [pre-defined keywords] that can be used as a column header.

See [user-defined keywords] in the [Tripper] documentation for how to extend the list of supported keywords.


[JSON-LD]: https://json-ld.org/
[unique and persistent identifier]: https://faircookbook.elixir-europe.org/content/recipes/findability/identifiers.html
[ORCID]: https://orcid.org/
[ROR]: https://ror.org/
[URI]: https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
[CURIE]: https://www.w3.org/TR/2010/NOTE-curie-20101216/
[linked data]: https://en.wikipedia.org/wiki/Linked_data
[license chooser]: https://choosealicense.com/
[list of standard open-source licenses]: https://choosealicense.com/appendix/
[UpperCamelCase]: https://en.wikipedia.org/wiki/Camel_case
[DCAT]: https://www.w3.org/TR/vocab-dcat-3/
[Tripper]: https://emmc-asbl.github.io/tripper/
[pre-defined keywords]: https://emmc-asbl.github.io/tripper/latest/datadoc/keywords/
[user-defined keywords]: https://emmc-asbl.github.io/tripper/latest/datadoc/customisation/#user-defined-keywords
[templates]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates
[software template]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/software.csv
[agents template]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/agents.csv
[owl:Class]: http://www.w3.org/2002/07/owl#Class
[emmo:Computation]: https://w3id.org/emmo#Computation
[emmo:Dataset]: https://w3id.org/emmo#Dataset
[stat:Completed]: http://purl.org/adms/status/Completed
[stat:Deprecated]: http://purl.org/adms/status/Deprecated
[stat:UnderDevelopment]: http://purl.org/adms/status/UnderDevelopment
[stat:Withdrawn]: http://purl.org/adms/status/Withdrawn
[IANA]: https://www.iana.org/assignments/media-types/
[iana:text/csv]: https://www.iana.org/assignments/media-types/text/csv
