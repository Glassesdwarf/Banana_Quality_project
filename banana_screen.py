import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from banana_graph import Banana_graph_maker
from check_bar import Checkbar
class Banana_application(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.graph = Banana_graph_maker()
        self.checkbar =  Checkbar(root, ['Size', 'Weight', 'Sweetness','Softness','Ripeness','Harvesttime','Acidity'])
        self.checkbar.pack()
        self.quit = tk.Button(root, text='Quit', command=root.quit).pack()
        #self.graph_button = tk.Button(root, text='hist', command=lambda: self.graph.show_hist(self.handle_hist_button())).pack()
        self.graph_button = tk.Button(root, text='hist', command=self.print).pack() 
        self.quality_check_button = tk.Button(root, text='quality_check', command=self.quality_check).pack()
        self.label_scatter = tk.Label(text = "Scatter_plot(Choose only 2 attribute)")
        self.label_scatter.pack()
        self.scatter_button = tk.Button(root, text='scatter', command=self.scatter_graph)
        self.scatter_button.pack()
        self.label = tk.Label(text = "Quality estimatation").pack()
    def handle_hist_button(self):
        new_list = []
        list_of_attribute = ['Size', 'Weight', 'Sweetness','Softness','Ripeness','HarvestTime','Acidity']
        checked = list(self.checkbar.state())
        
        for value, label in zip(checked,list_of_attribute):
            if value == 1:
                new_list.append(label)
        if new_list != []:
            return (new_list)
    def scatter_graph(self):
        _list = self.handle_hist_button()
        if len(_list) != 2 or len(_list) == []:
            self.label_scatter.config(foreground="red")
        else:
            self.graph.correl_graph(_list[0],_list[1])
    def print(self):
        self.graph.show_hist(self.handle_hist_button())
    def quality_check(self):
        _list = self.handle_hist_button()
        for value in _list:
            self.graph.quality_graph(value)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Banana Quality")
    app = Banana_application(root)
    root.mainloop()