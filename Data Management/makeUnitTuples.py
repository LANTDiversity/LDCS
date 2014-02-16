#makeUnitTuples

#the purpose of this code is used to associate a collection of units to a survey record for easy lookup of the data by unit

#open and read in raw data

import os
import sys
import numpy
import io

v = open('voviciRaw.csv',"r")
data = v.read()

v.close()


#for each survey record group the units found in the record into a list

#define unitTuple to store all the units associated with a survey record

# append this to the original data as a new column

#End

