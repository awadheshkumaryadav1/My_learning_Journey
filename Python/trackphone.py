# import phonenumbers
# from phonenumbers import geocoder

# # Parse phone numbers
# phone_number1 = phonenumbers.parse("+918210089387")
# phone_number2 = phonenumbers.parse("+918878586271")
# phone_number3 = phonenumbers.parse("+12136574429")
# phone_number4 = phonenumbers.parse("+201234567890")

# print("\nPhone Numbers Location\n")

# # Print locations
# print(geocoder.description_for_number(phone_number1, "en"))
# print(geocoder.description_for_number(phone_number2, "en"))
# print(geocoder.description_for_number(phone_number3, "en"))
# print(geocoder.description_for_number(phone_number4, "en"))

# import phonenumbers
# from phonenumbers import geocoder, carrier, timezone

# numbers = [
#     "+918210089387",  # India
#     "+12136574429",   # USA (New York)
#     "+201234567890"   # Egypt
# ]

# for num_str in numbers:
#     phone = phonenumbers.parse(num_str)
#     country_or_state = geocoder.description_for_number(phone, "en")
#     sim_carrier = carrier.name_for_number(phone, "en")
#     time_zones = timezone.time_zones_for_number(phone)

#     print(f"\nPhone Number: {num_str}")
#     print(f"Country/State: {country_or_state}")
#     print(f"Carrier: {sim_carrier}")
#     print(f"Time Zones: {time_zones}")



import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests

# 🔑 Replace with your real Google Maps Geocoding API key
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"

def get_location_details(region_name, country_code):
    """Use Google Maps API to get detailed location info."""
    query = f"{region_name}, {country_code}"
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": query, "key": GOOGLE_API_KEY}

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") == "OK" and data["results"]:
        components = data["results"][0]["address_components"]
        country = state = city = None

        for comp in components:
            if "country" in comp["types"]:
                country = comp["long_name"]
            elif "administrative_area_level_1" in comp["types"]:
                state = comp["long_name"]
            elif "locality" in comp["types"]:
                city = comp["long_name"]
            elif "administrative_area_level_2" in comp["types"] and city is None:
                city = comp["long_name"]  # fallback if locality missing

        return {"country": country, "state": state, "city": city}
    else:
        return {"country": None, "state": None, "city": None}


# ✅ Phone numbers to test
numbers = [
    "+917294536271",  # India
    "+12136574429",   # USA
    "+201234567890"   # Egypt
]

print("\n📍 Phone Number Location Info\n")

for num_str in numbers:
    phone = phonenumbers.parse(num_str)
    region_name = geocoder.description_for_number(phone, "en")
    country_code = phonenumbers.region_code_for_number(phone)
    sim_carrier = carrier.name_for_number(phone, "en")
    time_zones = timezone.time_zones_for_number(phone)

    # Get detailed location info
    location = get_location_details(region_name, country_code)

    print(f"📞 {num_str}")
    print(f"Region (from number): {region_name}")
    print(f"Carrier: {sim_carrier or 'Unknown'}")
    print(f"Time Zones: {time_zones}")
    print(f"Country: {location['country'] or 'Unknown'}")
    print(f"State: {location['state'] or 'Unknown'}")
    print(f"City: {location['city'] or 'Unknown'}")
    print("-" * 50)
