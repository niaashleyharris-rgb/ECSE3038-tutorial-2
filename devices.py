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

#write a function called average_temp(devices) — return the average temperature
def average_temp(devices):
    total = sum(device['temp'] for device in devices)
    return total / len(devices)

print(f"Average Temperature: {average_temp(readings):.2f}°C")

#write a function called hottest(devices) — return the whole dictionary of the hottest device
def hottest(devices):
    return max(devices, key=lambda device: device['temp'])

print(f"Hottest Device: {hottest(readings)['name']}, Temperature: {hottest(readings)['temp']}°C")

#write a function called to_status(device) — take one device, return a new dictionary

def to_status(device):
    # Determine status string based on the boolean online field
    if device["online"]:
        status_str = "ok"
    else:
        status_str = "offline"

    # Return the new dictionary structure
    return {
        "device": device["name"],
        "status": status_str,
        "celsius": device["temp"],
    }

# Testing Task 4 with the fridge 
print(f"Status readings for fridge: {to_status(readings[3])}")

#write a function Stretch. by_room(devices) — return a dictionary of room names to lists of device names
def by_room(devices):
    room_dict = {}
    for device in devices:
        room = device["room"]
        if room not in room_dict:
            room_dict[room] = []
        room_dict[room].append(device["name"])
    return room_dict

print(f"Devices by room:{by_room(readings)}")