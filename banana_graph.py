import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from check_bar import Checkbar
class Banana_graph_maker:
    def __init__(self):
        self.df = pd.read_csv('C:/worktoomuch/compro2 project/Banana_Quality_project/banana_quality.csv')
        self.df.dropna(inplace=True)
        self.new_df = self.df.copy()
    def show_hist(self,name,**kwargs):
        self.new_df[name].hist(figsize=(10, 8))
        plt.show()
    def assoication(self):
        pass
k = Banana_graph_maker()
k.show_hist(["Size",'Sweetness'])
    