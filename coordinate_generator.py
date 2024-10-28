import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm

geolocator = Nominatim(user_agent="geoapi")
df =pd.read_csv('/Users/zehan/Documents/Python/Data/DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS/DataCoSupplyChainDataset.csv', encoding='ISO-8859-1') 
# Example list of cities
cities = df['Order City'].unique()

# Function to fetch coordinates
def get_coordinates(city):
    try:
        location = geolocator.geocode(city)
        if location:
            return (location.latitude, location.longitude)
        else:
            return (None, None)
    except:
        return (None, None)

# Collect geolocation data for each city
geodata = {"Order City": [], "Order Latitude": [], "Order Longitude": []}
for city in tqdm(cities):
    lat, lon = get_coordinates(city)
    geodata["Order City"].append(city)
    geodata["Order Latitude"].append(lat)
    geodata["Order Longitude"].append(lon)

# Save to CSV or any format
df = pd.DataFrame(geodata)
print(df)
df.to_csv("/Users/zehan/Documents/Python/Data/DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS/order_city_geolocation.csv", index=False)