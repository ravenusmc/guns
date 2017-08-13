#This file will handle all of the data for the graphs on the see.html page. 
from bokeh.plotting import figure, output_file, show
from bokeh.models import CategoricalColorMapper, HoverTool
import numpy as np
import pandas as pd 


class Graphs():

    def __init__(self):
        self.__data = pd.read_csv('guns.csv')

    #This method will generate the graph to see the data by year.
    def by_year(self):
        #This is where 
        output_file('by_year.html')
        #Setting up the dimensions of the graph.
        p = figure(title="Deaths by Year", plot_width=400, plot_height=400)
        #setting up a list for the specific years and number of deaths. 
        years = [2012,2013,2014]
        number_of_deaths = []
        #This count variable will hold the number of loops as well as position in the list
        count = 0
        while count < 3:
            #getting the number of deaths for each year.
            deaths_by_year = len(self.__data[self.__data.year == years[count]])
            #Appending the deaths by year to the number of deaths. 
            number_of_deaths.append(deaths_by_year)
            #increasing the count by one. 
            count += 1
        #rendering the graph 
        p.line(years, number_of_deaths, legend="Deaths", line_color='blue', line_width=2)
        p.xaxis.axis_label = "Year"
        p.yaxis.axis_label = "Deaths"
        hover = p.select_one(HoverTool)
        hover.tooltips = [('Year', '@years'),
            ('Deaths', '@number_of_deaths')]
        show(p)

test = Graphs()
test.by_year()







































