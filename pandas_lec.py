import pandas as pd 
import numpy as np
print("pandas series and dataframecreation")

temperature = pd.Series([10, 20, 27, 39,44,35 ,45 ])
print(temperature)

temperature = pd.Series([10, 20, 27, 39,44,35 ,45], index=['nsk', 'mumbai', 'chennai', 'pune', 'bangalore', 'hyderabad', 'kolkata'],name='temperature of cities') 
print(temperature)         #index number chya evji city name print honartable format madhe and name he table chya name display sathi use kelay 

                 

print(f"max temperature is {temperature.max()} of city {temperature.idxmax()}")   # this prints maximum temperature and its corresponding city


student = {
    "stu_id": [1,2,3,4,5],
    "stu_name":["cp","hp","tp","sp","RP"],
    "department":["IT","Meical","Ecommerce","Science","computers"],
    "Age ":[21,19,22,20,np.nan],
    "Fees":[45000,30000,60000,34000,25000],
    "Year": [4,3,np.nan,2,4],
    "performance" :[45,76,44,62,77]

}


data =pd.DataFrame(student)
print(data)
# print(data.head(2))


# print(data.dtypes)
# print(data.shape)
# print(data.describe())
# print(data.info())

