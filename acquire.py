import requests
import os
import math
import pandas as pd
import numpy as np
import env

def get_db_url(db, user=env.username, host=env.host, password=env.password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_store_data():
    '''
    Returns a dataframe of all store data in the tsa_item_demand database and saves a local copy as a csv file.
    '''
    url = get_db_url('tsa_item_demand')

    query = '''
            SELECT *
            FROM items
            JOIN sales USING(item_id)
            JOIN stores USING(store_id)
            '''

    df = pd.read_sql(query, url)
    df.to_csv('tsa_store_data.csv', index=False)
    return df

def swapi() -> pd.DataFrame:
    if os.path.isfile('swapi.csv'):
        # If csv file exists read in data from csv file.
        print('File exists, pulling from system.')
        data = pd.read_csv('swapi.csv', index_col=0)
    else:
        # pulling data from mysql
        print('No file exists, extracting from MySQL.')
        data = pd.DataFrame()
        objects = ['people','planets','starships']
        for obj in objects:
            url_response = requests.get(f'https://swapi.dev/api/{obj}')
            url = url_response.json()
            # count number of observations in total
            num_count = url['count']
            # num. results on page
            num_results = len(url['results'])
            # defining outer range
            max_page = math.ceil(num_count / num_results)
            for page in range(1,max_page+1):
                url_response = requests.get(f'https://swapi.dev/api/{obj}/?page={page}')
                url = url_response.json()
                results = url['results']
                df = pd.DataFrame(results)
                data = pd.concat([data, df], ignore_index=True)

    data = data.drop_duplicates(subset=['name']).reset_index(drop=True)

    data.to_csv('./swapi.csv')

    return data

def swapi_merge() -> pd.DataFrame:
    if os.path.isfile('swapi.csv'):
        # If csv file exists read in data from csv file.
        print('File exists, pulling from system.')
        data = pd.read_csv('swapi.csv', index_col=0)
    else:
        # pulling data from mysql
        print('No file exists, extracting from MySQL.')
        data = pd.DataFrame()
        objects = ['people','planets','starships']
        for obj in objects:
            url_response = requests.get(f'https://swapi.dev/api/{obj}')
            url = url_response.json()
            # count number of observations in total
            num_count = url['count']
            # num. results on page
            num_results = len(url['results'])
            # defining outer range
            max_page = math.ceil(num_count / num_results)
            for page in range(1,max_page+1):
                url_response = requests.get(f'https://swapi.dev/api/{obj}/?page={page}')
                url = url_response.json()
                results = url['results']
                df = pd.DataFrame(results)
                data = pd.merge([data, df], ignore_index=True)

    data = data.drop_duplicates(subset=['name']).reset_index(drop=True)

    data.to_csv('./swapi.csv')

    return data


def people_swapi() -> pd.DataFrame:
    if os.path.isfile('people.csv'):
        # If csv file exists read in data from csv file.
        print('File exists, pulling from system.')
        data = pd.read_csv('people.csv', index_col=0)
    else:
        # pulling data from mysql
        print('No file exists, extracting from MySQL.')
        # setting df 
        data = pd.DataFrame()

        uri_response = requests.get(f'https://swapi.dev/api/people')
        uri = uri_response.json()
        # count number of observations in total
        num_count = uri['count']
        # num. results on page
        num_results = len(uri['results'])
        # defining outer range
        max_page = math.ceil(num_count / num_results)

        for page in range(1,max_page+1):
            uri_response = requests.get(f'https://swapi.dev/api/people/?page={page}')
            uri = uri_response.json()
            results = uri['results']
            df = pd.DataFrame(results)
            data = pd.concat([data, df], ignore_index=True)

    data.to_csv('people.csv')

    return data

def planets_swapi() -> pd.DataFrame:
    if os.path.isfile('planets.csv'):
        # If csv file exists read in data from csv file.
        print('File exists, pulling from system.')
        data = pd.read_csv('planets.csv', index_col=0)
    else:
        # pulling data from mysql
        print('No file exists, extracting from MySQL.')
        # setting df 
        data = pd.DataFrame()

        uri_response = requests.get(f'https://swapi.dev/api/planets')
        uri = uri_response.json()
        # count number of observations in total
        num_count = uri['count']
        # num. results on page
        num_results = len(uri['results'])
        # defining outer range
        max_page = math.ceil(num_count / num_results)

        for page in range(1,max_page+1):
            uri_response = requests.get(f'https://swapi.dev/api/planets/?page={page}')
            uri = uri_response.json()
            results = uri['results']
            df = pd.DataFrame(results)
            data = pd.concat([data, df], ignore_index=True)

        data.to_csv('planets.csv')

    return data

def starships_swapi() -> pd.DataFrame:
    if os.path.isfile('starships.csv'):
        # If csv file exists read in data from csv file.
        print('File exists, pulling from system.')
        data = pd.read_csv('starships.csv', index_col=0)
    else:
        # pulling data from mysql
        print('No file exists, extracting from MySQL.')
        # setting df 
        data = pd.DataFrame()

        uri_response = requests.get(f'https://swapi.dev/api/starships')
        uri = uri_response.json()
        # count number of observations in total
        num_count = uri['count']
        # num. results on page
        num_results = len(uri['results'])
        # defining outer range
        max_page = math.ceil(num_count / num_results)

        for page in range(1,max_page+1):
            uri_response = requests.get(f'https://swapi.dev/api/starships/?page={page}')
            uri = uri_response.json()
            results = uri['results']
            df = pd.DataFrame(results)
            data = pd.concat([data, df], ignore_index=True)
        
        data.to_csv('planets.csv')

    return data


def opsd_germany() -> pd.DataFrame:
    if os.path.isfile('opsd_germany.csv'):
        # If csv file exists read in data from csv file.
        print('File exists, pulling from system.')
        data = pd.read_csv('opsd_germany.csv', index_col=0)
    else:
        # pulling data from mysql
        print('No file exists, extracting from MySQL.')

        data = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')

    return data