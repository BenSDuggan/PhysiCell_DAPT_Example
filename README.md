# PhysiCell DAPT Example

This repository shows several examples of how to use the [Distributive Automated Parameter Testing](https://github.com/BenSDuggan/DAPT) (DAPT) package with [PhysiCell](https://github.com/MathCancer/PhysiCell).  DAPT makes parameter testing easy by making it easy to use APIs (e.g. Google Sheets and Box) to build a pipeline.  By connecting to "Databases", these tests can be run by many people simultaneously. 

## Setup instructions

Before setting up these examples, make sure that you can run PhysiCell by consulting the [Quickstart Guide](https://github.com/MathCancer/PhysiCell/blob/master/Quickstart.pdf).  Once you have confirmed that you can compile and run PhysiCell, open Terminal or CMD and type the following:

```
git clone https://github.com/BenSDuggan/PhysiCell_DAPT_Example
make -C PhysiCell
pip install dapt
```

## Run examples

There are a few different examples provided.  The <basic.py> example shows how a CSV can be used to run different parameters in a PhysiCell simulation.  This is the simplest example.

To remove <parameters.csv> and the files in the <output/> folder, you can run the <reset.py> script.  To additionally remove the .o and executable file created by PhysiCell you can include the `--hard` flag.
