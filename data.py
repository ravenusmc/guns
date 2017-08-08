#This file will contain the class and methods that will handle the data queries.
import numpy as np
import pandas as pd 

class Gundata():

    def __init__(self):
        self.__data = pd.read_csv('guns.csv')

    #This method will return the number of murders by the year that the user entered.
    def year_count(self, year):
        #I have to convert the year to a string
        # year_to_string = str(year)
        deaths_by_year = self.__data[self.__data.year == year]
        #Getting the count of the UFO's in the year that the user specified.
        count = len(deaths_by_year)
        print(count)

        # #Getting the state column
        # years = self.__data[[1]]
        # #Here I get the count of the number of deaths by year
        # count = len(years[years.year == year])
        # print(count)


test = Gundata()
test.year_count(2014)