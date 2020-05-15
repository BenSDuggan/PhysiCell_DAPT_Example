"""
PhysiCell Example
=================

This file shows an example workflow with PhysiCell.
"""

import os,platform,datetime, time, csv
import xml.etree.ElementTree as ET
import dapt

def main(db_path):

    sheet = dapt.Delimited_file(db_path, delimiter=',')
    ap = dapt.Param(sheet, config=None)

    print("Starting main script")

    parameters = ap.next_parameters() #Get the next parameter

    while parameters is not None:

        print("Request parameters: %s" % parameters)

        try:
            # Reset from the previous run
            print("Cleaning up folder")
            os.system("make data-cleanup")
            ap.update_status(parameters['id'], 'clean')

            # Create the parameters
            print("Creating parameters xml")
            create_XML(parameters, default_settings="config/PhysiCell_settings_default.xml", save_settings="config/PhysiCell_settings.xml")
            ap.update_status(parameters['id'], 'xml')
            # Run PhysiCell
            print("Running test")
            if platform.system() == 'Windows':
                os.system("biorobots.exe")
            else:
                os.system("./biorobots")
            ap.update_status(parameters['id'], 'sim')

            # Moving final image to output folder
            os.system("cp output/final.svg ../output/%s_final.svg" % parameters["id"])

            # Update sheets to mark the test is finished
            ap.successful(parameters["id"])

        except ValueError:
            print("Test failed:")
            print(ValueError)
            ap.failed(parameters["id"], ValueError)

        parameters = ap.next_parameters() #Get the next parameter
        
def create_XML(parameters, default_settings="PhysiCell_settings_default.xml", save_settings="PhysiCell_settings.xml", off_limits=[]):
    """
    Create a PhysiCell XML settings file given a dictionary of paramaters.  This function works by having a ``default_settings`` file which contains the generic XML structure.  Each key in ``parameters` then contains the paths to each XML tag in the ``default_settings`` file.  The value of that tag is then set to the value in the associated key.  If a key in ``parameters`` does not exist in the ``default_settings`` XML file then it is ignored.  If a key in ``parameters`` also exists in ``off_limits`` then it is ignored.

    Args:
        paramaters (dict): A dictionary of paramaters where the key is the path to the xml variable and the value is the desired value in the XML file.
        default_settings (str): the path to the default xml file
        save_settings (str): the path to the output xml file
        off_limits (list): a list of keys that should not be inserted into the XML file.
    """

    parameters = dict(parameters)
    tree = ET.parse(default_settings)
    root = tree.getroot()

    for key in parameters:
        if key in off_limits:
            next

        node = root.find(key)

        if node != None:
            node.text = str(parameters[key])

    tree.write(save_settings)

def reset_params(db_path):
    """
    Reset the CSV parameters
    """
    print('Reseting Parameters')

    with open(db_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'status', 'start-time', 'end-time', 'comment', './overall/max_time','./user_parameters/number_of_workers'])
        writer.writeheader()
        writer.writerow({'id':'test1', 'status':'', 'start-time':'', 'end-time':'', 'comment':'', './overall/max_time':'2880', './user_parameters/number_of_workers':'5', })
        writer.writerow({'id':'test2', 'status':'', 'start-time':'', 'end-time':'', 'comment':'', './overall/max_time':'2880', './user_parameters/number_of_workers':'50', })
        #writer.writerow({'id':'test3', 'status':'', 'start-time':'', 'end-time':'', 'comment':'', './overall/max_time':'2880', './user_parameters/number_of_workers':'150', })

if __name__ == '__main__':
    db_path = '../parameters.csv'
    os.chdir('PhysiCell')

    reset_params(db_path)
    main(db_path)
