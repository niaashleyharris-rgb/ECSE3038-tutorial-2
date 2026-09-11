readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

#write a function called list_devices(devices) — print each device's name and temperature using the data in the list called readings
def list_devices(devices):
    for device in devices:
        print(f"Device Name: {device['name']}, Temperature: {device['temp']}°C")


list_devices(readings)