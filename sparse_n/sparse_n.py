import json
import random
import time

start_time = time.time()

with open('user_data_sparse_n.json', 'r') as f:
    user_data = json.load(f)

connections = []

with open('connections_sparse_n.txt', 'r') as f:
    for line in f:
        st = line.rstrip()[1:-1]
        sts = st.split(", ")
        sts = [int(id[1:-1]) for id in sts]
        connections.append(sts)

print(f"Original length of connections : {len(connections)}")
E = (len(connections))
p = 0.1

n_edges_del = int(E * p)
random_edges = random.sample(connections, 2 * n_edges_del)
y_count = 0
n_count = 0

# randomly delete n_edges_del edges from connections
for edge in random_edges:
    connections.remove(edge)
    user1_id = edge[0]
    user2_id = edge[1]    
    flag = 0
    for idx, user in user_data.items():
        if user['id'] == str(user1_id):
            try:
                user['friend_ids'].remove(str(user2_id))
                print('Successfully removed connection between user 1 : {} and {}'.format(user1_id, user2_id))
                user_data[idx] = user
                y_count += 1
                flag = 1
            except ValueError:
                n_count += 1

        elif user['id'] == str(user2_id) and flag == 0:
            try:
                user['friend_ids'].remove(str(user1_id))
                print('Successfully removed connection between user 2 : {} and {}'.format(user2_id, user1_id))
                user_data[idx] = user
                y_count += 1
                flag = 1
            except ValueError:  
                n_count += 1                       
        
    # if successful edge deletions count reaches n_edges_del, break
    if y_count == n_edges_del:
        break

for idx, user in user_data.items():
    user.pop('id')
    user.pop('firstName')
    user_data[idx] = user

print(f"Final length of connections : {len(connections)}")
print(f"No. of connections deleted : {y_count}")
print(f"Total no. of connections couldn't be deleted : {n_count}")
print("\n\nTotal time taken : {} minutes".format((time.time() - start_time)/60))
print("sleeping for a minute ...")
time.sleep(60)

with open('connections_sparse_n.txt', 'w') as f:
    for connection in connections:
        f.write(f"{connection}\n")

with open('user_data_sparse_n.json', 'w') as f:
    json.dump(user_data, f)


