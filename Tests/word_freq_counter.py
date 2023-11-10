def count_word(para):
    counter = {}
    para_list = para.lower().strip().split()
    para_list = [word.replace(".", "").replace(",", "") for word in para_list]
    print(para_list)
    for word in para_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

# paragraph = input("Enter paragraph: ")
# print(paragraph)
counter = count_word("""
        Once, there was a tiger striped cat. This cat
        """)
print("counter",counter)
for key, value in counter.items():
    print(key)
# total_count=0
# for word,count in counter.items():
#     print(word+" : ",count)
#     total_count = total_count + count
# print(f"total count of words = {total_count}")