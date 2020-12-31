def get_cat_df(cat_list):
  """"
  Create pandas DataFrame with one row per single year group and associated category.
  -----------
  Params:
  cat_list: list of strings indicating continuous categories (e.g., ["0-5","6-9"])
  -----------
  Return: pandas DataFrame with two columns: cat_col (based on cat_list) and int_col
  
  """"
  import pandas as pd
  import numpy as np
  # transform into numpy array
  x = np.array(cat_list)
  # create empty list to know how many times to report the category string (e.g., "0-5" is 6)
  category_list = []
  # create empty list to know the min and max of each category string
  age_list = []
  for i in range(0,len(x)):
    min_age = int(x[i].replace('-', ' ').split()[0])
    age_list.append(min_age)
    max_age = int(x[i].replace('-', ' ').split()[1])
    age_list.append(max_age)
    category_list.append((max_age - min_age)+1)
  # repeat each category string
  category = np.repeat(x,category_list, axis=0)
  df = pd.DataFrame()
  df['cat_col'] = category
  df['int_col'] = pd.Series(range(min(age_list), (max(age_list)+1)))
  return df
