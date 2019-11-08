# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 09:16:09 2018

@author: bkhve
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



test = pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

plt.plot(test)


test.sort_values('Name')
test.sort_index()

len(test)

test.index

test.rename(columns = {'PassengerId':'passenger_id', 'Pclass':'passenger_class'})

test.columns


test2 = test.rename(columns = {'PassengerId':'passenger_id', 'Pclass':'passenger_class'})
test2.columns

test2.describe