#This file will handle all of the data for the graphs on the see.html page. 
from bokeh.plotting import figure, output_file, show
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label
import numpy as np
import pandas as pd 


class Graphs():

    def __init__(self):
        self.__data = pd.read_csv('guns.csv')

    #This method will generate the graph to see the data by year.
    def by_year(self):
        #This is where 
        output_file('by_year.html')
        #setting up a list for the specific years and number of deaths. 
        years = [2012,2013,2014]
        number_of_deaths = []
        #Setting up the dimensions of the graph and its labels.
        plot = figure(title="Deaths by Year", x_axis_label='Years', y_axis_label='Deaths', plot_width=400, 
            plot_height=400)
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
        plot.vbar(x=years, width=0.3, bottom=33500, top=number_of_deaths, legend="Deaths", line_color='blue', line_width=2) 
        # plot.line(years, number_of_deaths, legend="Deaths", line_color='blue', line_width=2)
        plot.legend.location = (0,300)
        show(plot)

test = Graphs()
test.by_year()


# hover = p.select_one(HoverTool)
# hover.tooltips = [('Year', '@years'),
#     ('Deaths', '@number_of_deaths')]







































