def count_word(para):
    counter = {}
    for word in para:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

paragraph = input("Enter paragraph: ").strip().split()
print(paragraph)
counter = count_word(paragraph)
for word,count in counter.items():
    print(word+" : ",count)