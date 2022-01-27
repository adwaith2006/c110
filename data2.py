import csv
import statistics as st
import pandas as pd
import plotly.figure_factory as ff 
import random

df=pd.read_csv("data.csv")
data=df["temp"].to_list()

def randomSetOfMean(counter):
    data_set=[]
    for i in range(0,counter):

        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)

    mean2=st.mean(data_set)
    return(mean2)

def showFig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()
    mean=st.mean(mean_list)
    print("mean is:",mean)
    standard_deviation2=st.stdev(mean_list)
    print("std is:",standard_deviation2)
def setUp():
    mean_list=[]
    for i in range(0,1000):
        setOfMean=randomSetOfMean(100)
        mean_list.append(setOfMean)

    showFig(mean_list)

setUp()


