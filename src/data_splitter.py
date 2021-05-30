# data_splitter.py
import os

import pandas as pd
from sklearn import model_selection

CSV_NAME = 'raw_data.csv'
CSV_DIR = 'input'

# Reads raw data csv from the input folder
df = pd.read_csv(os.path.join(CSV_DIR,CSV_NAME))

# Shuffle
df = df.sample(frac=1, replace = False).reset_index(drop=True)

# Initialize the fold class
kf = model_selection.KFold(n_splits = 5)

# Create  kfold column
df['kfold'] = 0

# Fill the kfold column
for fold, (trn_, val_) in enumerate(kf.split(X=df)):
    df.loc[val_, 'kfold'] = fold

# Print distribution of classes in each fold
print(pd.pivot_table(df, index='kfold', columns='class', aggfunc='size').reset_index(drop=True))

# Export to input folder the train data splitted in N folds
df.to_csv('input/raw_data_splitted.csv', index = False)