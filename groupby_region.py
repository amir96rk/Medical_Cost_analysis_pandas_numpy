# The dataset is grouped by 4 region (Northeast, Northwest, Northwest, Southwest)
# and mean and std of  bmi,charges and age of individual has aggregrated to the groups.  
# Numpy is used in order to get mean and std (ignoring nan).
import pandas as pd
import numpy as np
df=pd.read_csv("insurance.csv")
gp = df.groupby('region').agg({'bmi': (np.nanmean , np.std),
                               'charges' : (np.nanmean , np.std),
                               'age' :(np.nanmean , np.std) })
