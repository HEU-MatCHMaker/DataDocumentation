Semantic documentation of tools, datasets and workflows
=======================================================

This example is intended to be a simple guide for how to do a step-by-step documentation of

- [Semantic documentation of tools, datasets and workflows](#semantic-documentation-of-tools-datasets-and-workflows)
    - [Important underlying principles](#important-underlying-principles)
    - [Documenting the processes and their relationships to potential real datasets](#documenting-the-processes-and-their-relationships-to-potential-real-datasets)
    - [Documenting the actual datasets and executed workflows](#documenting-the-actual-datasets-and-executed-workflows)
    - [How to do this in practice](#how-to-do-this-in-practice)
  - [1. Documentation of software tools](#1-documentation-of-software-tools)
  - [2. Documentation of related resources](#2-documentation-of-related-resources)
  - [3. Documentation of dataset types](#3-documentation-of-dataset-types)
  - [4. Documentation of actual datasets](#4-documentation-of-actual-datasets)
  - [5. Documentation of executed workflows](#5-documentation-of-executed-workflows)
  - [6. Documentation of content of datasets](#6-documentation-of-content-of-datasets)

### Important underlying principles ###

- **Individuals versus Classes**: 
    We distinguish between individuals and classes. Individuals are specific instances of a concept, while classes are general categories that can have multiple instances. For example, a specific software tool would be an individual, while the category of software tools would be a class.


### Documenting the processes and their relationships to potential real datasets ###
The figure below illustrates the documentation of step 1 to 3, where a **computation class** is related to a **software individual** and the types of datasets (i.e. **dataset classes**) it takes as input and output. It is important to realise that at this level of the documentation we 
focus on documenting the processes that we can run and their relationships to potential real datasets. 


![Documentation of step 1 to 3.](https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/datadoc-example/examples/tools/figs/computation.svg)

### Documenting the actual datasets and executed workflows ###

Once the **types of**  proesses and datasets that we treat have been documented, 
it is possible to document actual datasets and workflows (step 4 and 5). 
This principle on how the classes (the concepts) and individuals (actual instances)
are related is shown in the figure below.

![Documentation of step 4 and 5.](https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/datadoc-example/examples/tools/figs/workflow.svg)


### How to do this in practice ###

The main interface for this semantic documentation is simple spreadsheets with well-defined column headers.
The names in the column headers are under the hood mapped to ontological concepts via a [JSON-LD] context.
However, a normal user is not exposed to the complexity of semantic technologies.
The important thing to understand is that these headers are not just arbitrary names, but they have a specific meaning in the context of semantic documentation.
Instead, the user is presented with a simple set of [spreadsheet templates].
Each documented resource will be a row in one of these templates.

Since the FAIR principles demand that all resources must have a globally [unique and persistent identifier], all the templates have a column labeled "@id".
This column should contain an IRI.
These IRIs can be written is as [URI]s, like <https://he-matchmaker.eu/resource/my_software>, or as compact URIs (so-called [CURIE]s), like mm:my_software, where the prefix `mm` is a shorthand for the namespace <https://he-matchmaker.eu/resource/>, intended for MatCHMaker-owned resources.

For semantics, it is also important to document the type of the resource.
Hence, all templates also have a column labeled "@type".
The values in this column should also be an IRI identifying an ontological concept describing the type of the resource.
General values for the type are described in the following sections, which also explains how the templates should be filled out.


## 1. Documentation of software tools

For a minimal documentation of a software tool, the user should fill in table such as the one below.
See the [software template] for a more elaborate template.

| @id | @type | title | description |
|-----|-------|-------|-------------|
|     |       |       |             |

The expected values for each column are:

- **@id**: Unique persistent identifier, in the form of an [URI] or [CURIE].
- **@type**: Type of the software. In the general case, it could be `emmo:Software`, but if a more specialised subclass is known, it should be used. This must refer to a concept in an ontology, such as the [EMMO], and not to a free text string.
- **title**: Name or title of the software as a string.
- **description**: A human readable description of the software, also a string.


## 2. Documentation of related resources


## 3. Documentation of dataset types


## 4. Documentation of actual datasets


## 5. Documentation of executed workflows


## 6. Documentation of content of datasets



[JSON-LD]: https://json-ld.org/
[spreadsheet templates]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates
[software template]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/software.csv
[URI]: https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
[CURIE]: https://www.w3.org/TR/2010/NOTE-curie-20101216/
