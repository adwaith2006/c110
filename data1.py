import csv
import statistics as st
import pandas as pd
import plotly.figure_factory as ff 
import random

df=pd.read_csv("data.csv")
data=df["temp"].to_list()
#print(data)
fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.show()
mean=st.mean(data)
print("Mean is: ",mean)
standard_deviation=st.stdev(data)
print("standard deviation is :",standard_deviation)

data_set=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    data_set.append(value)

mean1=st.mean(data_set)
standard_deviation1=st.stdev(data_set)
print("mean is:",mean1,"standard deviation is:",standard_deviation1)




