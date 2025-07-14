import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

# Replace 'your key' with your actual OpenCage API key
key = "your key"  
number = input("Please enter the phone number (without country code): ")
default_region = "IN"  # Set the default region code (e.g., "IN" for India)
new_number = phonenumbers.parse(number, default_region)

# Get location description
location = geocoder.description_for_number(new_number, "en")
print("Location:", location)

# Get carrier information
service_name = carrier.name_for_number(new_number, "en")
print("Carrier:", service_name)

# Geocoding the location
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

# Extract latitude and longitude
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print("Latitude:", lat)
print("Longitude:", lng)

# Create a map with the location
my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)

# Save the map to an HTML file
my_map.save("location.html")

print("Location tracking completed. Check location.html for the map.")
