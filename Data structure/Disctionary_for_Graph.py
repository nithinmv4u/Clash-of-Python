adj_list = {}
adj_list['A'] = []
adj_list['B'] = []
adj_list['C'] = []
adj_list['D'] = []
adj_list['F'] = []
print(adj_list)
adj_list['A'].append('B')
adj_list['B'].append('A')

adj_list['B'].append('C')
adj_list['C'].append('B')

adj_list['C'].append('D')
adj_list['D'].append('C')

adj_list['D'].append('A')
adj_list['A'].append('D')
adj_list['A'].append('E')

print(adj_list)

if 'E' not in adj_list:
    print("True")

if 'F' in adj_list:
    print("True")

adj_list['A'].remove('D')
print(adj_list)
for key in adj_list:
    print(key)
    if 'B' in adj_list[key]:
        adj_list[key].remove('B')
print(adj_list)
