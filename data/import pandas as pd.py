import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r'D:\Project\ecommerece_raw.csv',encoding='latin1')

# First look
print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())