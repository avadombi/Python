import pandas as pd

DIR_PATH = '../Raw'
SAVE_PATH = '../Processed'


def get_countries():
    path = f"{DIR_PATH}/countries.xlsx"
    countries = pd.read_excel(path, index_col=0)
    countries = countries.rename(columns={'country_code_2': 'country_code'})

    # remove duplicates
    countries = countries.drop_duplicates(subset='country_name')

    # sort by asc order
    countries = countries.sort_values(by='country_name')
    return countries


def get_cities():
    path = f"{DIR_PATH}/cities.xlsx"
    cities = pd.read_excel(path, index_col=0)
    cities = cities.rename(columns={'country_code_2': 'country_code'})
    return cities


def get_currencies():
    path = f"{DIR_PATH}/currencies.xlsx"
    currencies = pd.read_excel(path, index_col=0)
    currencies = currencies.rename(columns={'country_code_2': 'country_code'})

    # remove duplicates (currency)
    currencies_no_duplicates = currencies.drop_duplicates(subset='currency_code')

    # remove duplicates (country_code)
    currencies_no_duplicates = currencies_no_duplicates.drop_duplicates(subset='country_code')

    # sort by asc order
    currencies_no_duplicates = currencies_no_duplicates.sort_values(by='currency_name')

    # add index column
    currencies_no_duplicates['currency_id'] = currencies_no_duplicates.index
    return currencies_no_duplicates


def get_processed_currencies():
    # get currencies data
    currencies_data = get_currencies()

    # reorganize
    columns = ['currency_id', 'currency_name', 'currency_code']
    currencies_no_duplicates = currencies_data[columns]

    # sort
    currencies_no_duplicates = currencies_no_duplicates.sort_values(by='currency_id')
    return currencies_no_duplicates


def get_process_countries():
    # get countries data
    countries_data = get_countries()

    # get currencies raw data
    currencies = get_currencies()

    # merge on country_code_2
    merged_data = pd.merge(
        countries_data, currencies,
        on='country_code', how='inner'
    )

    # get the columns of interest
    column_names = ['country_name', 'country_code', 'region',
                    'sub_region', 'currency_code']

    countries_data = merged_data[column_names]

    # get processed currencies data
    currencies_no_duplicates = get_processed_currencies()

    # merge on currency_code
    merged_data = pd.merge(
        countries_data, currencies_no_duplicates,
        on='currency_code', how='left'
    )

    countries_data = merged_data

    # columns of interest
    columns = ['country_name', 'country_code', 'region',
               'sub_region', 'currency_id']
    countries_data = countries_data[columns]

    # add index column
    countries_data['country_id'] = countries_data.index + 1
    columns = ['country_id', 'country_name', 'country_code', 'region',
               'sub_region', 'currency_id']
    countries_data = countries_data[columns]

    return countries_data


def get_processed_cities():
    # get cities data
    cities_data = get_cities()

    # get processed countries data
    proc_countries = get_process_countries()

    # merge
    merged_data = pd.merge(
        cities_data, proc_countries,
        on='country_code', how='inner'
    )

    columns = ['city_name', 'latitude', 'longitude',
               'capital', 'population', 'country_id']
    cities_data = merged_data[columns]

    # print(cities_data[cities_data['country_id']])
    return cities_data
