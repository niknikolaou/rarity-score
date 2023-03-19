import json
import re

with open('collection.json', 'r') as f:
    data = json.load(f)

# Regular expression pattern to match "id" field
pattern = r'"id": \d+'

# Loop through items in data and replace "id" value with number following "name"
for item in data:
    name = item['name']
    match = re.search(r'#(\d+)$', name)
    if match:
        new_id = int(match.group(1))
        item['id'] = new_id

# Save the modified data to a new JSON file
with open('modified_file.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Done!")