Semantic documentation of tools, datasets and workflows
=======================================================

This example is intended to be a simple guide for how to do a step-by-step documentation of

1. software tools
2. related resources, like its owner and license
3. classes/types of datasets it takes as input and returns as output
4. actual datasets
5. executed workflows
6. the content of datasets (in terms of data models)

The figure below illustrates the documentation of step 1 to 3, where a class of computations is related to a software and the types of datasets it takes as input and output.

![Documentation of step 1 to 3.](https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/datadoc-example/examples/tools/figs/computation.svg)

How this connects to the documentation of actual datasets and workflows (step 4 and 5) is shown in the figure below.

![Documentation of step 4 and 5.](https://raw.githubusercontent.com/HEU-MatCHMaker/DataDocumentation/refs/heads/datadoc-example/examples/tools/figs/workflow.svg)

The main interface for this semantic documentation are simple spreadsheets with well-defined column headers.
The names in the column header are under the hood mapped to ontological concepts via a [JSON-LD] context.
However, a normal user is not exposed to the complexity of semantic technologies.
Instead, the user is presented with a simple set of [spreadsheet templates].
Each documented resource will be a row in one of these templates.

Since the FAIR principles demands that all resources must have a globally [unique and persistent identifier], all the templates has a column labeled "@id".
This column should contain an IRI.
These IRIs can be written is as [URI]s, like <https://he-matchmaker.eu/resource/my_software>, or as compact URIs (so-called [CURIE]s), like mm:my_software, where the prefix `mm` is a shorthand for the namespace <https://he-matchmaker.eu/resource/>, intended for MatCHMaker-owned resources.

For semantics, it is also important to document the type of the resource.
Hence, all templates also has a column labeled "@type".
The values in this column should also be an IRI identifying an ontological concept describing the type of the resource.
General values for the type are described in the following sections, which also tries to explain how the templates should be filled out.


## 1. Documentation of software tools

For a minimal documentation of a software tool, the user should fill in the table below.
See the [software template] for a more elaborate template.

| @id | @type | title | description |
|-----|-------|-------|-------------|
|     |       |       |             |

The expected values for each column are:

- **@id**: Unique persistent identifier, in the form of an [URI] or [CURIE].
- **@type**: Type of the software. In the general case, it could be `emmo:Software`, but if a more specialised subclass is known, it should be used.
- **title**: Name or title of the software.
- **description**: A human readable description of the software.



[JSON-LD]: https://json-ld.org/
[spreadsheet templates]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates
[software template]: https://github.com/HEU-MatCHMaker/DataDocumentation/tree/master/examples/tools/templates/software.csv
[URI]: https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
[CURIE]: https://www.w3.org/TR/2010/NOTE-curie-20101216/
