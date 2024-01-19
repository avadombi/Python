from utilisFunctions import *

# currencies, countries, cities
currencies = get_processed_currencies()
countries = get_process_countries()
cities = get_processed_cities()

# save
path = '../Processed'
currencies.to_csv(f'{path}/currencies.csv', sep=',', index=False)
countries.to_csv(f'{path}/countries.csv', sep=',', index=False)
cities.to_csv(f'{path}/cities.csv', sep=',', index=False)

