def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        sorted_word = ''.join(sorted(word))  # Sort the characters of the word
        print(sorted_word)
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)  # Add word to the list of anagrams
        else:
            anagram_dict[sorted_word] = [word]  # Create a new entry for the anagram

    return anagram_dict

# Example usage
word_list = ['cat', 'dog', 'tac', 'god', 'act', 'good']
anagram_groups = group_anagrams(word_list)
print(anagram_groups)

# Display the anagram groups
for anagram_group in anagram_groups.values():
    print(anagram_group)
