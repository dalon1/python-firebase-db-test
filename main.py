# Importing packages
import requests
import yaml

# 1. Reading config file
with open("config.yml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

print("Config Object: " + str(config))

# 2. Calling data source rest api (e.g. country-rest-api) and parsing data
api_response = requests.get(config.get("data_source_url"))
raw_data = api_response.json()

# 2.1. Just getting the name for each country record
parsed_data = [country.get("name") for country in raw_data]
# print(parsed_data)

# 3.0 Log in to firebase realtime database and storing parsed data
from firebase import firebase
firebase_db = firebase.FirebaseApplication(config.get("firebase_db_url"), authentication=None)
firebase_db_result = firebase_db.get('/countries', None, {'print': 'pretty'})
print("First DB Request - Output: " + str(firebase_db_result))

# 3.1. Push data to firebase realtime database
firebase_db.post('/countries', parsed_data, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})

# 3.2. Confirm new parsed data is stored in firebase realtime db
firebase_db_result = firebase_db.get('/countries', None, {'print': 'pretty'})
print("Second DB Request -  Output" + str(firebase_db_result))