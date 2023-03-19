import json

with open('collection.json', 'r') as f:
    data = json.load(f)

for i, d in enumerate(data):
    d = {'id': i, **d}  # add 'id' field to the beginning of the dictionary
    data[i] = d  # replace original dictionary with new one
    print(i)

for i, d in enumerate(data):
    d = {'id': i, **d}  # add 'id' field to the beginning of the dictionary
    d['compiler'] = 'UW'  # change 'compiler' field to 'UW'
    data[i] = d  # replace original dictionary with new one
    print(i)

for i, d in enumerate(data):
    d = {'id': i, **d}  # add 'id' field to the beginning of the dictionary
    if d['name'] == 'Some Condition':  # change 'compiler' only if 'name' meets some condition
        d['compiler'] = 'UW'
    data[i] = d  # replace original dictionary with new one
    print(i)

# Save the modified data to a new JSON file
with open('modified_file.json', 'w') as f:
    json.dump(data, f, indent=0)

print("Done!")