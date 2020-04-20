import pandas as pd
import  matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df1=pd.DataFrame({"Days":[1,2,3,4],"INT_rate ":[21,12,36,11],"US_GDP_Thousands":[123,45,67,89]},
                 index=[2001,2002,2003,2004])
df1.set_index("Days",inplace=True)
print(df1)

#df1.plot()
#plt.show()
df1=df1.rename(columns={"INT_rate":"Rate"})
print(df1)

