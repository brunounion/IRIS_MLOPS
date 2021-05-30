# data_connection.py
import pandas as pd
import sklearn.datasets


# importing data from sklearn library
data_dict = sklearn.datasets.load_iris()

# Creating data frame with X values and with his features names
df_data_raw = pd.DataFrame(data_dict.data, columns = data_dict.feature_names)

# Creating the Y column
df_data_raw['target'] = data_dict.target

# Creating a dictionary with the Y value and his class
dict_target_names = dict(zip(df_data_raw['target'].unique(), data_dict.target_names))

# Creating a columns in the dataframe with the target classes names
df_data_raw['class'] = df_data_raw['target'].map(dict_target_names)

# Exporting the raw data dataframe to posterior use
df_data_raw.to_csv(r'input/raw_data.csv', index=False)