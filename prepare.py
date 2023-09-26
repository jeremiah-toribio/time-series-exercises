import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

def prepare_store(store):
    '''
    - Changes date column to 'datetime64[ns]' & sets as index
    - Add month and year columns
    '''
    # change dtype of date
    store.sale_date = store.sale_date.astype('datetime64[ns]')
    # set index
    store = store.set_index('sale_date')
    # month and year columns
    store['month'] = store.index.month
    store['year'] = store.index.year
    # agg column
    store['sales_total'] = store.sale_amount + store.item_price
    store.drop(columns=['store_id','item_id'],inplace=True)
    return store

def prepare_opsd(opsd):
    '''
    - Lowers column letters
    - Changes date column to 'datetime64[ns]' & sets as index
    - Add month and year columns
    - Backfills null values
    '''
    # lower columns #
    opsd.columns = opsd.columns.str.lower()
    # change dtype for date #
    opsd.date = opsd.date.astype('datetime64[ns]')
    # set index #
    opsd = opsd.set_index('date')
    # month and year #
    opsd['month'] = opsd.index.month 
    opsd['year'] = opsd.index.year
    # fill na #
    opsd.backfill(inplace=True)

    return opsd

def check_distributions(df, columns):
    for col in columns:
        sns.histplot(data=df, x=col)
        plt.show()
    return
