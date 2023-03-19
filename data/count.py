import json

# Open the JSON file and load its contents
with open('collection.json', 'r') as file:
    data = json.load(file)

# Initialize a counter for Durkon's name
count = 0

# Iterate over the list of objects in the JSON data
for item in data:
    # Iterate over the attributes of each object
    for attribute in item["attributes"]:
        # If the attribute's "trait_type" is "Tribe" and its "value" is "Durkon", increment the counter
        if attribute["trait_type"] == "Tribe" and attribute["value"] == "Renian":
            count += 1

# Print the total count of Durkon's name
print(f"Durkon's name appears {count} times in the JSON file.")