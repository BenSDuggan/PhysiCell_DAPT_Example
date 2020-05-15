"""
Reset the repository by removing simulation data
"""

import os, sys, csv

db_path = 'parameters.csv'

print('Reseting Parameters')

with open(db_path, 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'status', 'start-time', 'end-time', 'comment', './overall/max_time','./user_parameters/number_of_workers'])
    writer.writeheader()
    writer.writerow({'id':'test1', 'status':'', 'start-time':'', 'end-time':'', 'comment':'', './overall/max_time':'2880', './user_parameters/number_of_workers':'5', })
    writer.writerow({'id':'test2', 'status':'', 'start-time':'', 'end-time':'', 'comment':'', './overall/max_time':'2880', './user_parameters/number_of_workers':'50', })
    writer.writerow({'id':'test3', 'status':'', 'start-time':'', 'end-time':'', 'comment':'', './overall/max_time':'2880', './user_parameters/number_of_workers':'150', })

# Remove images we moved
os.system('rm -rf output/*')
os.system('touch output/empty.txt')

os.system('make -C PhysiCell data-cleanup')

if '--hard' in sys.argv:
    os.system('make -C PhysiCell clean')
