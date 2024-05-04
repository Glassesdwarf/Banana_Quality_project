import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class Banana_graph_maker:
    def __init__(self):
        self.df = pd.read_csv('banana_quality.csv')
        self.df.dropna(inplace=True)
        self.new_df = self.df.copy()
    def show_hist(self,name):
        self.new_df[name].hist(figsize=(10, 8))
        plt.show()
    