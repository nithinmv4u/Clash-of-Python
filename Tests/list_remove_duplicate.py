def remove_duplicate(sorted_list):
    i=0
    while i < len(sorted_list)-1:
        if sorted_list[i] == sorted_list[i+1]:
            sorted_list.remove(sorted_list[i+1])
        else:
            i+=1
    print(sorted_list)

sorted_list = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9]
remove_duplicate(sorted_list)