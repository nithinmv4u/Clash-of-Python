def matchingStrings(stringList, queries):
    result = [0] * len(queries)
    for i in range(len(queries)):
        for j in range(len(stringList)):
            if(queries[i]==stringList[j]):
                result[i]+=1
    return result
 
def main():
    stringList_count = int(input("Enter String length: ").strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input("Enter Query length: ").strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    print(res)

main()