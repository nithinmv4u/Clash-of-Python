data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Carol", "age": 20}]
data.sort(key=lambda x: x["age"])
print(data)