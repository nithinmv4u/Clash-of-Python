person = {
    'name' : 'Tom',
    'age' : 14,
    'place' : 'Amsterdom'
}

print(person['place'])

for key, value in person.items():
    # print(key +" : "+ value)   ----concatenation is not possible since an integer is there as age
    print(key, " : ", value)

print(person)
person.clear()
print(person)
person['gender']='Male'
print(person)
person = {
    'name' : 'Tom',
    'age' : 14,
    'place' : 'Amsterdom',
    'gender' : 'Male'
}
print(person)
del person['gender']
print(person)
if 'age' in person:
    print(person['age'])

place = person.get('place')
if place:
    print(place)

print(len(person))
person_copy = person.copy()
print(person_copy)