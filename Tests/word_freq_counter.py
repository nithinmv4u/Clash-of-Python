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
total_count=0
for word,count in counter.items():
    print(word+" : ",count)
    total_count = total_count + count
print(f"total count of words = {total_count}")