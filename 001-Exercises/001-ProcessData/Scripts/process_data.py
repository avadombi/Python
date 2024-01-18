import pandas as pd
import os

# Set the working directory to the directory containing our script (else, relative path will not work)
# __file__ : contains absolute or relative path of our current file
# os.path.abspath(__file__): return the absolute path of __file__
# os.path.dirname(): return the parent folder of the current file
# os.chdir(): change the dir to the one specified.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DIR_PATH = '../Raw'
SAVE_PATH = '../Processed'

# load data
def get_cities():
    path = f"{DIR_PATH}/cities.csv"

    column_names = ['city_name', 'latitude', 'longitude', 'country_code_2',
                    'capital', 'population', 'insert_date']

    cities = pd.read_csv(path, sep=',', index_col=0, lineterminator='\n', names=column_names)
    return cities

def get_countries():
    path = f"{DIR_PATH}/countries.csv"

    column_names = ['country_name', 'country_code_2', 'country_code_3', 'region',
                    'sub_regiocreate_on', 'intermediate_region', 'insert_date']

    countries = pd.read_csv(path, sep=',', index_col=0, lineterminator='\n', names=column_names)
    return countries


def get_currencies():
    path = f"{DIR_PATH}/currencies.csv"

    column_names = ['country_code_2', 'currency_name', 'currency_code']
    countries = pd.read_csv(path, sep=',', index_col=0, lineterminator='\n', names=column_names)
    return countries


print(get_currencies())
