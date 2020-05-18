# PhysiCell DAPT Example

This repository shows several examples of how to use the [Distributive Automated Parameter Testing](https://github.com/BenSDuggan/DAPT) (DAPT) package with [PhysiCell](https://github.com/MathCancer/PhysiCell) version 1.7.0.  DAPT makes parameter testing easy by making it easy to use APIs (e.g. Google Sheets and Box) to build a pipeline.  By connecting to "Databases", these tests can be run by many people simultaneously.  This repository contains examples of a simple example ([basic.py]), example with a configuration file ([config.py]), and an example using Google Sheets ([sheets.py]).

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
├── outputs                			# Directory where output from the pipeline is saved
├── PhysiCell          				# PhysiCell 1.7.0 source code
├── basic.py          				# Simplest example using DAPT with PhysiCell
├── config.py              			# Example of using config file with DAPT
├── sheet.py             			# Example showing how to combine cloud services like Google Sheets with DAPT
├── reset.py           				# Python script that removes files created by examples
└── parameters.csv           		# Parameters used for by each example, not used directly
```

## Examples

There are a few different examples provided.  The `basic.py` example shows how a CSV can be used to run different parameters in a PhysiCell simulation.  This is the simplest example.

To remove `parameters.csv` and the files in the `output/` folder, you can run the `reset.py` script.  To additionally remove the .o and executable file created by PhysiCell you can include the `--hard` flag.
