import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import prepare as p




def check_year(train, columns):
    for i, col in enumerate(columns):
        ax1 = train.groupby(train.index.year)[col].mean().plot(kind='bar')
        ax1.set_title(f'Average Yearly {col}')
        ax1.set_xlabel('Sale Date')
        ax1.yaxis.set_major_formatter('${x:1.2f}')
        ax1.yaxis.set_tick_params(which='major', labelcolor='green',
                                labelleft=True)
        plt.show()
        # ax2 = validate.groupby(validate.index.year)[col].mean().plot(kind='bar')
        # ax2.set_title(f'Average Yearly {col}')
        # ax2.set_xlabel('Sale Date')
        # ax2.yaxis.set_major_formatter('${x:1.2f}')
        # ax2.yaxis.set_tick_params(which='major', labelcolor='green',
        #                         labelleft=True)
        # plt.show()

def heatmap(train,method):
    corrs = train.corr(method=method)
    np.triu(corrs)
    sns.heatmap(corrs, 
            cmap='Blues', 
            mask=np.tril(corrs))