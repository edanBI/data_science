import pandas as pd
import numpy as np
from sklearn import preprocessing


class PreProcess:

    def __init__(self, df):
        self.df = df
        self.handle_values()

    def handle_values(self):
        # fill in missing values - handle NaN
        self.df.fillna(self.df.mean(), inplace=True)

        # standardization process
        for column in self.df.columns:
            if self.df[column].dtypes == 'float64':
                self.df[column] = (self.df[column] - self.df[column].mean()) / (self.df[column].std())

        # group by 'country'
        self.df = self.df.groupby('country').mean()
        self.df = self.df.drop('year', 1)




