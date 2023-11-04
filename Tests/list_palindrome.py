def palindrome(list1):
    half_length = len(list1)//2
    count = 0
    for i in range(half_length):
        if list1[half_length:][half_length - i] == list1[:half_length][i]:
            count+=1
    if count == half_length:
        print("palindrome")
    else:print("not palindrome")

def is_palindrome(input_list):
    # Check if the list is equal to its reverse.
    return input_list == input_list[::-1]

palindrome_list = [1, 2, 3, 2, 1]
non_palindrome_list = [1, 2, 3, 4, 5]
palindrome(palindrome_list)
palindrome(non_palindrome_list)

print("Is the first list a palindrome:", is_palindrome(palindrome_list))
print("Is the second list a palindrome:", is_palindrome(non_palindrome_list))