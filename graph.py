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

    #This method will show the user deaths by type
    def by_type(self):
        output_file = open('by_type.html', 'w')
        #These lists will hold the data. 
        death_type = ['Accidental', 'Homicide', 'Suicide', 'Undetermined']
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

    #This method will show the deaths by location
    def by_place(self):
        output_file = open('by_location.html', 'w')
        #These lists will hold the data. 
        location = ['Farm', 'Home', 'Street', 'Trade/service area','Residential institution','Street','Industrial/construction' ]
        location_count = []
        chart = discreteBarChart(name='discreteBarChart', height=500, width=800)
        #This count variable will hold the number of loops as well as position in the list
        count = 0
        while count < 7:
            count_of_deaths = len(self.__data[self.__data.place == location[count]])
            #Appending the count of the death type to the list 
            location_count.append(count_of_deaths)
            #increasing the count by 1 
            count += 1 
        xdata = location
        ydata = location_count
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()

    #This method will show the user deaths by age. 
    def by_age(self):
        output_file = open('by_age.html', 'w')
        age = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100']
        chart = discreteBarChart(name='discreteBarChart', height=500, width=800)
        count = 0 
        #These numbers will make up the individual age groups. Essentially my way of creating a bin. 
        ones = 0
        teens = 0
        twent = 0
        thirty = 0
        forty = 0 
        fifty = 0
        sixty = 0
        seventy = 0
        eighty = 0
        ninety = 0
        #I use the while loop to go through the ages in the csv file. 
        while count < 101:
            count_of_deaths = len(self.__data[self.__data.age == count])
            if count <= 10:
                ones = ones + count_of_deaths
            elif count <= 20:
                teens = teens + count_of_deaths
            elif count <= 30:
                twent = twent + count_of_deaths
            elif count <= 40:
                thirty = thirty + count_of_deaths
            elif count <= 50:
                forty = forty + count_of_deaths
            elif count <= 60:
                fifty = fifty + count_of_deaths
            elif count <= 70:
                sixty = sixty + count_of_deaths
            elif count <= 80:
                seventy = seventy + count_of_deaths
            elif count <= 90:
                eighty = eighty + count_of_deaths
            elif count <= 100:
                ninety = ninety + count_of_deaths
            count += 1
        age_count = [ones, teens, twent, thirty, forty, fifty, sixty, seventy, eighty, ninety]
        xdata = age
        ydata = age_count
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()

    def by_race(self):
        output_file = open('by_race.html', 'w')
        race = ['White', 'Black', 'Asian/Pacific Islander', 'Native American/Native Alaskan', 'Hispanic']
        race_count = []
        chart = discreteBarChart(name='raceBarChart', height=500, width=800)
        count = 0 
        while count < 5:
            count_of_deaths = len(self.__data[self.__data.race == race[count]])
            race_count.append(count_of_deaths)
            count += 1
        #I build this list twice because Native American/Native Alaskan was taking to much space up 
        #on my graph.
        race = ['White', 'Black', 'Asian/Pacific Islander', 'Native American', 'Hispanic']
        xdata = race
        ydata = race_count
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()

    def by_police(self):
        output_file = open('by_police.html', 'w')
        police = ['Not police killed', 'Police killed']
        police_count = []
        chart = discreteBarChart(name='policeBarChart', height=500, width=800)
        count = 0 
        while count < 2:
            count_of_deaths = len(self.__data[self.__data.police == count ])
            police_count.append(count_of_deaths)
            count += 1
        xdata = police
        ydata = police_count
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()

    def by_education(self):
        output_file = open('by_educ.html', 'w')
        education = ['> High School', 'High School', 'Some College', 'Graduated College', 'Not Available']
        death_count = []
        chart = discreteBarChart(name='educBarChart', height=500, width=800)
        count = 1
        while count < 6:
            count_of_deaths = len(self.__data[self.__data.education == count ])
            death_count.append(count_of_deaths)
            count += 1
        xdata = education
        ydata = death_count
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()



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








































