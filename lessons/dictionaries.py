"""Demonstrations of dictionary capabilities."""


# Declaring the type of dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dicitonary literal representation
print(schools)

# Access a vlue by its key -- "lookup"
print(f"UNC has {schools['UNC']} studnets")

# Remove a key-value pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools.")
else:
    print("No key 'Duke' in schools")

# Update / Reassign a key-valye pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literals
schools = {} # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400,
    "Dukie": 6717,
    "NCSU": 26150
}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")