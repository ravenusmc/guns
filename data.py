#This file will contain the class and methods that will handle the data queries.
import numpy as np
import pandas as pd 

class Gundata():

    def __init__(self):
        self.__data = pd.read_csv('guns.csv')

    #This method will return the number of murders by the year that the user entered.
    def year_count(self, year):
        #This line gets the all of the data points that match the year that the user entered.
        deaths_by_year = self.__data[self.__data.year == year]
        #I then get the count of the number of values for that year. 
        count = len(deaths_by_year)
        return count


test = Gundata()
test.year_count(2014)