import json

count = 0

with open('collection.json', 'r') as f:
    data = json.load(f)

for obj in data:
    # Extract the id number from the name field
    id_num = obj['name'].split('#')[1]

    # Add the id field to the object
    obj['id'] = int(id_num)

    count += 1

# Write the updated data back to the file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Print the counter value
print(f"Processed {count} objects.")
