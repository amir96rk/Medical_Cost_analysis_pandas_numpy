# In this code, I got the subtraction with the "charges" (Individual medical costs billed by health insurance) and "mean charges of each region" for each row.
# Then, I found out what percent of inpatient costs is more than avreage of their region and what percent is less than 
# avreage of their region.

import pandas as pd
import numpy as np

def charges_mean_diff():
        df = pd.read_csv('insurance.csv')
        
        # I transformed df to a dataframe which has two columns of region and charges
        # and groupby with region.
        cols=['region','charges']
        transform_df=df[cols].groupby('region').transform(np.nanmean)
        
        # Then, I renamed 'charges' in transformed df to 'mean_charges_of_region'
        transform_df.rename({'charges':'mean_charges_of_region'}, axis='columns', inplace=True)
        
        # Then, two dataframes were merged.
        df=df.merge(transform_df, left_index=True, right_index=True)
        
        # New column named 'mean_diff' were added to df.
        df['mean_diff']=df['charges']-df['mean_charges_of_region']
        
        charged_more_percent = (len(df[df['mean_diff'] > 0]) / len(df)) * 100
        charged_less_percent = (len(df[df['mean_diff'] < 0]) / len(df)) * 100
        
        output = ''' {0:.2f} percent of inpatient medical costs are more than there region's mean and {1:.2f} percent 
        of inpatient medical costs are less than there region's mean'''.format(charged_more_percent,charged_less_percent)
        
        return output
# returns : '31.99 percent of inpatient medical costs are more than there region's mean 
# and 68.01 percent of inpatient medical costs are less than there region's mean'
​


