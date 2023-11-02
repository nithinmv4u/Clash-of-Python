data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Carol", "age": 20}]
data.sort(key=lambda x: x["age"])
print(data)

# lambda regular function
def get_age(x):
    return x["age"]

print(get_age(data[0]))

print(data[0]["age"])