# methds of serieses........
import pandas as pd
series1 = pd.Series([4,5,6,7])
series2 = pd.Series([6,7,8,5])
adding_serieses =series1.add(series2)
print("adding the two series will be:\n",adding_serieses)
sereies4 = pd.Series(["pavan","kumar","raju","naveen","ramu","kalyan","pavan"])
print("the 3rd index in the element is:\n",sereies4[3])
print("slicing between 1 to 3\n",sereies4[1:3])#index will be key to the serieses values
print("head method will be returns the first five elements in the series:\n",sereies4.head())
print("head method will be returns the last five elements in the series:\n",sereies4.tail())
print("head method will be returns the first 4 five elements in the series:\n",sereies4.head(4))
print("head method will be returns the last 3 five elements in the series:\n",sereies4.tail(3))
print("genarate discriptive statistics:\n",sereies4.describe())#it will print count,unique elementsNo,firstelement,freq....
somenumbers = pd.Series([4,5,6,7,8,3,2])
print("mean of the sesrisis:\n",somenumbers.mean)
print("median of the series is:\n",somenumbers.median)
print("std of the series is:\n",somenumbers.std)
print("shap of the series is:\n",somenumbers.shape)
print("sizeof the series is:\n",somenumbers.size)
print("ndim of the series is:\n",somenumbers.ndim)
print("given series is null or :\n",somenumbers.isnull())
print("given series is notnull:\n",somenumbers.notnull())






