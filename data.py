#This file will contain the class and methods that will handle the data queries.
import numpy as np
import pandas as pd 

class Gundata():

    def __init__(self):
        self.__data = pd.read_csv('guns.csv')

    #This method will return the number of gun deaths by the year that the user entered.
    def year_count(self, year):
        #This line gets the all of the data points that match the year that the user entered.
        deaths_by_year = self.__data[self.__data.year == year]
        #I then get the count of the number of values for that year. 
        count = len(deaths_by_year)
        return count

    #This method will return the number of gun deaths by type that the user enters
    def type_count(self, death_type):
        #getting the areas where intent matches the death type from weapon
        deaths_by_type = self.__data[self.__data.intent == death_type]
        #Getting the count
        count = len(deaths_by_type)
        return count

    #This method will return the number of gun deatahs by location that the user selects. 
    def location(self, location):
        #getting the areas where the location matches the what the user entered. 
        location = self.__data[self.__data.place == location]
        #Getting the count 
        count = len(location)
        return count



# test = Gundata()
# test.year_count('Home')