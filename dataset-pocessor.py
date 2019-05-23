#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from itertools import combinations as cnb

#Read csv file to Cov, set header to 'None' since data comes with no headers.
Cov = pd.read_csv('wine.data', sep = ',', header = None)

Cov.columns = ['Class','Alcohol', 'Malic Acid', 'Ash', 'Alcalinity', 'Magnesium', 'Total phenols', 'Flavanoids',
               'Nonflavanoid', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD_280_OD_315', 'Proline']

#To display maximum columns when printing data
pd.set_option('display.max_columns', None)

#print dataset in table format
print(Cov.to_string())
print()

#print standard stats of dataset without including the Class column
Cov2 = Cov.drop(['Class'], axis = 1)
print(Cov2.describe())

os.makedirs('plots', exist_ok=True)
os.makedirs('plots/line_plots',exist_ok=True)
os.makedirs('plots/scatter_plots',exist_ok=True)
os.makedirs('plots/heatmap_plots', exist_ok=True)

# Plotting line chart without Class column only
for i in Cov2.columns:
     plt.plot(i)
     plt.plot(Cov[i], color='red')
     plt.title(str(i)+' by Index')
     plt.xlabel('Index')
     plt.ylabel(i)
     plt.savefig(f'plots/line_plots/'+str(i)+'_by_index_plot.png', format='png')
     plt.clf()

#making a list of all column combinations but with no repeats
comb = cnb(Cov2.columns, 2)

#scatterplotting the combinations with no repeats, for unique plots
for i in comb:

    plt.scatter(Cov2[i[0]],Cov2[i[1]], color='b')
    plt.title(i[0]+' to '+i[1])
    plt.xlabel(i[0])
    plt.ylabel(i[1])
    plt.savefig(f'plots/scatter_plots/'+i[0]+'_to_'+i[1]+'.png', format='png')

    plt.close()

#create a list of correlations using corr()
corr = Cov2.corr()

#create a plot figure
fig, ax = plt.subplots()

# create heatmap table
im = ax.imshow(corr.values)

# set labels for the table
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment to the table.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")
plt.savefig(f'plots/heatmap_plots/heatmap.png',format='png')
plt.close()

