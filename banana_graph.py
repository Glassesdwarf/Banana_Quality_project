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
        """"show basic histogram"""
        self.new_df[name].hist(figsize=(10, 8))
        plt.show()
    def correlation(self,name):
        """"finding correlation"""
        new_df = self.df.copy()
        new_df.drop(columns=["Quality"], inplace=True)  # Drop the 'Quality' column
        corr_matrix = new_df.corr()
        return corr_matrix[name]
    def correl_graph(self, x_attr, y_attr):
        """""making scatter graph from 2 selected attribute"""
        plt.figure(figsize=(10, 8))
        plt.scatter(self.new_df[x_attr], self.new_df[y_attr])
        plt.xlabel(x_attr)
        plt.ylabel(y_attr)
        plt.title(f'Scatter plot of {x_attr} vs {y_attr}')
        plt.grid(True)
        plt.show()
    def quality_graph(self,name):
        """""Making box plot of quality of selected attribute"""
        plt.figure(figsize=(12, 8))
        sns.boxplot(x= name, hue='Quality', data=self.new_df)
        plt.xlabel(f'{name}')
        plt.ylabel('Frequency')
        plt.title(f'Boxplot of Rating for {name} , with Good quality vs.Bad quality')
        plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
        plt.legend(title=f'Quality of {name}', loc='upper left')
        plt.show()
#k = Banana_graph_maker()
#k.show_hist(["Size",'Sweetness'])
#k.quality_graph("Size")
#print(k.correlation())