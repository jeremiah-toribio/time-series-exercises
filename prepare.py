import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


def prepare_opsd(opsd):
    '''
    - Lowers column letters
    - Changes date column to 'datetime64[ns]' & sets as index
    - Add month and year columns
    - Backfills null values.
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