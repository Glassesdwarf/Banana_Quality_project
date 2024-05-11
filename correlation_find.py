import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from banana_graph import Banana_graph_maker

k = Banana_graph_maker()

#k.show_hist(["Size",'Sweetness'])
#k.quality_graph("Size")
#print(k.correlation("Size"))
#print(k.correlation("Weight"))
#print(k.correlation("Sweetness"))
#print(k.correlation("Softness"))
#print(k.correlation("HarvestTime"))
#print(k.correlation("Ripeness"))
print(k.correlation("Acidity"))

#Size and Harvest time are affect together
#weight affect the Acidity and Sweetness
#Sweetness affect the weight
#Softness nearly have nothing to do with other attribute
#harvest time affect the Size of Banana
#Ripeness make acidity low
#Acidity affect the wright

#Story that you can get from this data set is 
#-The longer it take to harvest the banana the bigger it will be
#-THe more heavy banana the more sweet the banana is
#-This could be said that most of the good bana are Big Sweet Banana which could be obtain from take longer time to harvest 
#probably meaning the banana are should be taking long time to care for