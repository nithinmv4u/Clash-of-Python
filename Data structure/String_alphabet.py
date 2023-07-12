def replace_char(text, old_char, new_char):
    new_text = ""
    for char in text:
        if char == old_char:
            new_text += new_char
        else:
            new_text += char
    return new_text

def main():
    text = input("Enter the text: ")
    old_char = input("Enter character to be replaced: ").strip().split()[0]
    new_char = input("Enter character to replace: ").strip().split()[0]
    new_text = replace_char(text, old_char, new_char)
    print(new_text)

main()