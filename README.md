# PhysiCell DAPT Example

This repository shows several examples of how to use the [Distributive Automated Parameter Testing](https://github.com/BenSDuggan/DAPT) (DAPT) package with [PhysiCell](https://github.com/MathCancer/PhysiCell) version 1.7.0.  DAPT makes parameter testing easy by making it easy to use APIs (e.g. Google Sheets and Box) to build a pipeline.  By connecting to "Databases", these tests can be run by many people simultaneously.  This repository contains examples of a simple example ([basic.py](basic.py)), example with a configuration file ([config.py](/config.py)), and an example using Google Sheets ([sheets.py](/sheets.py)).  

The PhysiCell biorobots sample project is used in this tutorial.  You can interact with this model using the [biorobots NanoHub tool](https://nanohub.org/tools/pc4biorobots).  This sample project has three types of agents: cargo cells (blue), worker cells (red), and director cells (green).  The worker cells will move to cargo cells, attach to them, move the cargo cells to the directory cells, drop off them off, and then look for another cargo cell.  

Two important parameters for this model are `attached_worker_migration_bias`, the motility bias when worker cells are attached to cargo cells, and `unattached_worker_migration_bias`, the motility bias when worker cells aren't attached to cargo cells.  When the bias is 1, the worker cells' strictly follow the chemotaxis signal, and when it's 0, the worker cell's motility direction is random.  Bias between 0 and 1 change how biased the migration towards random or deterministic motion.

## Setup instructions

Before setting up these examples, make sure that you can run PhysiCell by consulting the [Quickstart Guide](https://github.com/MathCancer/PhysiCell/blob/master/Quickstart.pdf).  Once you have confirmed that you can compile and run PhysiCell, open Terminal or CMD and type the following:

```
git clone https://github.com/BenSDuggan/PhysiCell_DAPT_Example
make -C PhysiCell
pip install dapt
```

## Repository contents

```
.
├── outputs                         # Directory where output from the pipeline is saved
├── PhysiCell                       # PhysiCell 1.7.0 source code
├── basic.py                        # Simplest example using DAPT with PhysiCell
├── config.py                       # Example of using config file with DAPT
├── sheet.py                        # Example showing how to combine cloud services like Google Sheets with DAPT
├── reset.py                        # Python script that removes files created by examples
└── parameters.csv                  # Parameters used for by each example, not used directly
```

## Basic Example

The simplest way to use DAPT is with a delimiter-separated file, such as a CSV.  CSVs are common files used to store two-dimensions of data, typically with a header.  This makes them natural to use as a "database", where rows are tests and columns are the attributes.

XML

The parameters used for this (and the other examples) are shown in the table below.  The table has three tests (one per row) named test1, test2, and test3, using the `id` attribute.  The `status` attribute can be updated to reflect what task is currently in progress and needs to be initially empty to be ran.  The `start-time` and `end-time` attributes are set when the test begins and ends, respectively.  The `comment` attribute can be set before, during, or after a test is ran to provide additional information.  The attributes to the right of `comment` are used for the PhysiCell biorobots sample project settings.

| id                | status | start-time | end-time | comment | ./overall/ max_time | ./user_parameters/ attached_worker_migration_bias | ./user_parameters/ unattached_worker_migration_bias |
|-------------------|--------|------------|----------|---------|--------------------|--------------------------------------------------|----------------------------------------------------|
| default           |        |            |          |         | 2880               | 1.0                                              | 0.5                                                |
| attached-random   |        |            |          |         | 2880               | 0.1                                              | 1.0                                                |
| unattached-random |        |            |          |         | 2880               | 1.0                                              | 0.1                                                |


## Config Example

## Sheets Example


## Cleanup

To cleanup the directory, you can run the [reset.py](/reset.py) script.  This script will remove the finals in the outputs folder, cleanup the data created by PhysiCell, and remove the CSVs used by the example scripts, except for [parameters.csv](/parameters.csv).  To remove the `.o` and executable file created by PhysiCell you can include the `--hard` flag (`python reset.py --hard`).
