#This file will handle all of the data for the graphs on the see.html page. 

import numpy as np
import pandas as pd 

class Graphs():

    def __init__(self):
        self.__data = pd.read_csv('guns.csv')