#This file will handle all of the data for the graphs on the see.html page. 
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label
from bokeh.plotting import figure, output_file, show
import numpy as np
import pandas as pd 

from nvd3 import discreteBarChart


class Graphs():

    def __init__(self):
        self.__data = pd.read_csv('guns.csv')

    #This method will generate the graph to see the data by year.
    def by_year(self):
        #This is where the code that this method generates will be stored
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
        #This line will launch the graph 
        # show(plot)

    #This method will show the deaths by type. I tried to use bokeh to make the bar graph for type but 
    #it simply would not work.
    # def by_type(self):
    #     #This is where the code that this method generates will be stored
    #     output_file('by_type.html')
    #     #These lists will hold the data. 
    #     death_type = [1,2,3,4]
    #     # death_type = ['Accidental', 'Homicide', 'Suicide', 'Undetermined']
    #     count_of_type = []
    #     #Setting up the dimensions of the graph and its labels.
    #     plot = figure(title="Deaths by Type", x_axis_label='Death Type', y_axis_label='Deaths', plot_width=400, 
    #         plot_height=400)
    #     #This count variable will hold the number of loops as well as position in the list
    #     count = 0
    #     while count < 4:
    #         count_of_deaths = len(self.__data[self.__data.intent == death_type[count]])
    #         #Appending the count of the death type to the list 
    #         count_of_type.append(count_of_deaths)
    #         #increasing the count by 1 
    #         count += 1 
    #     #Rendering the graph
    #     plot.Bar(x=death_type, width=0.5, bottom=500, top=count_of_type, legend='Deaths', line_color='blue',
    #         line_width=2)
    #     show(plot)

    def by_type(self):
        output_file = open('by_type.html', 'w')
        #These lists will hold the data. 
        death_type = ['Accidental', 'Homicide', 'Suicide', 'Undetermined']
        # death_type = ['Accidental', 'Homicide', 'Suicide', 'Undetermined']
        count_of_type = []
        chart = discreteBarChart(name='discreteBarChart', height=400, width=400)
        #This count variable will hold the number of loops as well as position in the list
        count = 0
        while count < 4:
            count_of_deaths = len(self.__data[self.__data.intent == death_type[count]])
            #Appending the count of the death type to the list 
            count_of_type.append(count_of_deaths)
            #increasing the count by 1 
            count += 1 
        xdata = death_type
        ydata = count_of_type
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()

test = Graphs()
test.by_type()


# hover = p.select_one(HoverTool)
# hover.tooltips = [('Year', '@years'),
#     ('Deaths', '@number_of_deaths')]







































