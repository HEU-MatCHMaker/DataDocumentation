# Semantic data documentation for MatCHMaker

Within this repository are the entities that represent (eventually all) data used in the MatCHMaker project.
It holds the "source of truth" for these entities, and as such, if updated, the entities will be uploaded for wide use in the project.

The repository is structured according to domain, concrete, SOFC, PEMFC, SEM, TEM, etc.
For each domain a standard subfolder structure is used, like
- `/datamodels/`: Data models in YAML or JSON format.
- `/plugins/`: DLite storage plugins for the data models.
- `/example_data/`: Example datasets and instances.
- `/tests/`: Tests for plugins and other scripts.
- `/doc/`: Further documentation.

The repository also contains instance examples for these entities.

Eventually, semantic mappings will be included here, possibly also OTEAPI pipeline configurations.

All these things together completely document the data used in the MatCHMaker project in a semantic and FAIR way.

## Acknowledgements & funding

This work is funded by the MatCHMaker project, which has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement N 101091687.

## License & copyright

This work is licensed under the [MIT License](LICENSE).
Copyright &copy; 2022-2024 MatCHMaker.
