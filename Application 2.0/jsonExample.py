import json
data = {}
for tab in range(5):
    step = {}
    conditions = {}
    step['name'] = "AAAAAAAA"
    for condition in range(2):
        conditions[condition] = True
    step['conditions'] = conditions
    data[tab] = step
    json_data = json.dumps(data)

print(json_data)

