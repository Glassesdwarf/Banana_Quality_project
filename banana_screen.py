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
        #self.label = tk.Label(text = "Quality estimatation").pack()
        self.label = tk.Label(text = "Quality estimatation (type in number between -10 to 10)")
        self.label.pack()
        self.estimate_init()
        self.estimate_button = tk.Button(root, text='estimate', command=self.quality_estimate)
        self.estimate_button.pack()
        self.estimation_value = tk.Label(text = " ")
        self.estimation_value.pack()
    def estimate_init(self):
        """creating entry widget for estimated"""
        self.entry_widgets = {}
        for i in ['Size', 'Weight', 'Sweetness','Softness','Ripeness','Harvesttime','Acidity']:
                label = tk.Label(root, text=f"{i}")
                label.pack()
                entry = ttk.Entry(root, font=('Arial', 14))
                entry.pack()
                self.entry_widgets[i] = entry
    def quality_estimate(self):
        """""estimate the quality of banana the number in this method are based on decision tree plotted in rapidminer"""
        d_t = 0
        for i in ['Size', 'Weight', 'Sweetness','Softness','Ripeness','Harvesttime','Acidity']:
            if i == "":
                d_t += 0
            elif not isinstance(i, (float, int)):
                self.label.config(foreground="red")
            elif self.entry_widgets[i] > 10 or self.entry_widgets[i] < -10:
                self.label.config(foreground="red")
            
            if float(self.entry_widgets["Sweetness"].get()) > 2.109 and float(self.entry_widgets["Harvesttime"].get()) > -4.968 and float(self.entry_widgets["Weight"].get()) <= -1.58 and float(self.entry_widgets["Size"].get()) > -2.144:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) > 2.109 and float(self.entry_widgets["Harvesttime"].get()) > -4.968 and float(self.entry_widgets["Weight"].get()) >= -1.58 and float(self.entry_widgets["Softness"].get()) > 2.76:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) > 2.109 and float(self.entry_widgets["Harvesttime"].get()) > -4.968 and float(self.entry_widgets["Weight"].get()) >= -1.58 and float(self.entry_widgets["Softness"].get()) <= 2.76 and float(self.entry_widgets["Size"].get()) <= -5.17:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) > 2.109 and float(self.entry_widgets["Harvesttime"].get()) > -4.968 and float(self.entry_widgets["Weight"].get()) >= -1.58 and float(self.entry_widgets["Softness"].get()) <= 2.76 and float(self.entry_widgets["Size"].get()) > -5.17 and float(self.entry_widgets["Softness"].get()) <= 1.2:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) > 2.109 and float(self.entry_widgets["Harvesttime"].get()) > -4.968 and float(self.entry_widgets["Weight"].get()) >= -1.58 and float(self.entry_widgets["Softness"].get()) <= 2.76 and float(self.entry_widgets["Size"].get()) > -5.17 and float(self.entry_widgets["Softness"].get()) > 1.2 and float(self.entry_widgets["Sweetness"].get()) > 2.4:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Ripeness"].get()) > -4.26 and float(self.entry_widgets["Acidity"].get()) <= -4.93 and float(self.entry_widgets["Softness"].get()) > -3.48 and float(self.entry_widgets["Ripeness"].get()) > -2.99 and float(self.entry_widgets["Softness"].get()) <= -2.53 and float(self.entry_widgets["Ripeness"].get()) <= 0.97:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Ripeness"].get()) > -4.26 and float(self.entry_widgets["Acidity"].get()) <= -4.43:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Ripeness"].get()) > -4.26 and float(self.entry_widgets["Acidity"].get()) <= -4.93 and float(self.entry_widgets["Softness"].get()) > -3.48 and float(self.entry_widgets["Ripeness"].get()) > -2.99 and float(self.entry_widgets["Size"].get()) > 2.02:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) <= 1.74 and float(self.entry_widgets["Softness"].get()) > 3.89 :
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Softness"].get()) > 3.89 and float(self.entry_widgets["Acidity"].get()) <= 5.32 and float(self.entry_widgets["Acidity"].get()) > -2.932 and float(self.entry_widgets["Harvesttime"].get()) > -4.22 and float(self.entry_widgets["Softness"].get()) > 1.1 and float(self.entry_widgets["Size"].get()) > -0.29:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Softness"].get()) > 3.89 and float(self.entry_widgets["Acidity"].get()) <= 5.32 and float(self.entry_widgets["Acidity"].get()) > -2.932 and float(self.entry_widgets["Harvesttime"].get()) > -4.22 and float(self.entry_widgets["Softness"].get()) <= 1.1 and float(self.entry_widgets["Harvesttime"].get()) > -3.82:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Softness"].get()) <= 3.89 and float(self.entry_widgets["Weight"].get()) <= 1.72 and float(self.entry_widgets["Size"].get()) > 3.2 and float(self.entry_widgets["Harvesttime"].get()) > -2.5 and float(self.entry_widgets["Softness"].get()) > -3.2 and float(self.entry_widgets["Ripeness"].get()) > -5.19:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Softness"].get()) <= 3.89 and float(self.entry_widgets["Weight"].get()) <= 1.72 and float(self.entry_widgets["Size"].get()) <= 3.2 and float(self.entry_widgets["Acidity"].get()) > -6 and float(self.entry_widgets["Ripeness"].get()) > 6.6:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Softness"].get()) <= 3.89 and float(self.entry_widgets["Weight"].get()) <= 1.72 and float(self.entry_widgets["Size"].get()) <= 3.2 and float(self.entry_widgets["Acidity"].get()) > -6 and float(self.entry_widgets["Ripeness"].get()) <= 6.6 and float(self.entry_widgets["Softness"].get()) > 3.3 and float(self.entry_widgets["Size"].get()) > -2.4:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Softness"].get()) <= 3.89 and float(self.entry_widgets["Weight"].get()) <= 1.72 and float(self.entry_widgets["Size"].get()) <= 3.2 and float(self.entry_widgets["Acidity"].get()) > -6 and float(self.entry_widgets["Ripeness"].get()) <= 6.6 and float(self.entry_widgets["Softness"].get()) <= 3.3 and float(self.entry_widgets["Size"].get()) > -2.4:
                d_t += 1
            if float(self.entry_widgets["Sweetness"].get()) <= 2.109 and float(self.entry_widgets["Harvesttime"].get()) > 1.74 and float(self.entry_widgets["Softness"].get()) <= 3.89 and float(self.entry_widgets["Weight"].get()) <= 1.72 and float(self.entry_widgets["Size"].get()) <= 3.2 and float(self.entry_widgets["Acidity"].get()) <= -6:
                d_t += 1
        else:
            pass
        if d_t >= 1:
            self.estimation_value.config(text="Good Banana")
        elif d_t == 0:
            self.estimation_value.config(text="Bad Banana")
                
                
    def handle_hist_button(self):
        """return the value in checkbox out"""
        new_list = []
        list_of_attribute = ['Size', 'Weight', 'Sweetness','Softness','Ripeness','HarvestTime','Acidity']
        checked = list(self.checkbar.state())
        
        for value, label in zip(checked,list_of_attribute):
            if value == 1:
                new_list.append(label)
        if new_list != []:
            return (new_list)
    def scatter_graph(self):
        """""handle making scatter graph"""
        _list = self.handle_hist_button()
        if len(_list) != 2 or len(_list) == []:
            self.label_scatter.config(foreground="red")
        else:
            self.graph.correl_graph(_list[0],_list[1])
    def print(self):
        """""show basic plot"""
        self.graph.show_hist(self.handle_hist_button())
    def quality_check(self):
        """""showing box plot of quality good bad of selected attribute"""
        _list = self.handle_hist_button()
        for value in _list:
            self.graph.quality_graph(value)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Banana Quality")
    app = Banana_application(root)
    root.mainloop()