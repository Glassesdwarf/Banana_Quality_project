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
    def quality_graph(self,name):
    
        plt.figure(figsize=(12, 8))
        sns.boxplot(x= name, hue='Quality', data=self.new_df)
        plt.xlabel(f'{name}')
        plt.ylabel('Frequency')
        plt.title(f'Boxplot of Rating for {name} , with Good quality vs.Bad quality')
        plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
        plt.legend(title=f'Quality of {name}', loc='upper left')
        plt.show()
k = Banana_graph_maker()
#k.show_hist(["Size",'Sweetness'])
k.quality_graph("Size")