
#### 7-8-26     examples using all libraries in one  ------

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd


data={
    "student":["a","b","c","d","e","f","g","h","i","j"],
    "python":[65,45,65,76,87,99,45,34,55,23],
    "sql":[23,56,34,65,77,33,44,66,78,98],
    "java":[44,65,77,44,87,45,65,33,54,65],
    "c_lang":[34,88,23,43,54,66,98,66,54,23],
    "attendance":[56,78,88,99,55,44,65,76,34,76]


}


# <bound method NDFrame.head of   student  python  sql  java  c_lang
# 0       a      65   23    44      34
# 1       b      45   56    65      88
# 2       c      65   34    77      23
# 3       d      76   65    44      43
# 4       e      87   77    87      54
# 5       f      99   33    45      66
# 6       g      45   44    65      98
# 7       h      34   66    33      66
# 8       i      55   78    54      54
# 9       j      23   98    65      23>



df=pd.DataFrame(data)
print("\n =================shape of frame=======")
print("\n Student Data : ",data )
print(df.shape)
print(df.head)
print(df.tail)

# <bound method NDFrame.describe of   student  python  sql  java  c_lang
# 0       a      65   23    44      34
# 1       b      45   56    65      88
# 2       c      65   34    77      23
# 3       d      76   65    44      43
# 4       e      87   77    87      54
# 5       f      99   33    45      66
# 6       g      45   44    65      98
# 7       h      34   66    33      66
# 8       i      55   78    54      54
# 9       j      23   98    65      23>

print(df.describe)




marks=df[["python","sql","java"]].values

total=np.sum(marks,axis=1)
print(total)

# [132 166 176 185 251 177 154 133 187 186]


avg=np.average(marks,axis=1)               
print(avg)


# 44.         55.33333333 58.66666667 61.66666667 83.66666667 59.
#  51.33333333 44.33333333 62.33333333 62.    



df["Total"]=total
df["Average"]=avg

df["Average"]=df["Average"].round(2)     # for only two digits after decimal point
print(df)


#    marks topper student   ------- it returns index 


topper_index =df["Total"].idxmax()
print(topper_index)
print(df.loc[topper_index])    # location

print("python",df["python"].mean())         # for one subject average
print("sql",df["sql"].mean())  
print("java",df["java"].mean())  
print("c_lang",df["c_lang"].mean())  





high_performance= df[df["Average"]>70]
print(high_performance)

#  student  python  sql  java  c_lang  Total  Average
# 4       e      87   77    87      54    251    83.67


# to find a rank based on average 

ranking=df.sort_values(
    by="Avg",
    ascending=False)
print(ranking)

#print(ranking ["name","avg"])

      

co_relation=df["attendence"].corr(df["Avg"])
print(co_relation)




# # bar chart
# plt.figure(figsize=(8, 5))

# plt.bar(df["student"], df["Total"])

# plt.xlabel("Students")
# plt.ylabel("Total Marks")
# plt.title("Student Total Marks")

# plt.show()



# #line chart
# plt.figure(figsize=(8, 5))

# plt.plot(df["student"], df["Average"], marker="o")

# plt.xlabel("Students")
# plt.ylabel("Average Marks")
# plt.title("Student Average Marks")

# plt.show()



