import json

with open('user_data_naive_n.json', 'r') as f:
    user_data = json.load(f)

for idx, user in user_data.items():
    user.pop('id')
    user.pop('firstName')
    user_data[idx] = user

with open('user_data_naive_n.json', 'w') as f:
    json.dump(user_data, f)