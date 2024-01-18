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
    path = "../Raw/cities.csv"

    column_names = ['city_name', 'latitude', 'longitude', 'country_code_2',
                    'capital', 'population', 'insert_date']

    cities = pd.read_csv(path, sep=',', index_col=0, names=column_names)
    return cities

print(get_cities())