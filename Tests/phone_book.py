def phone_entry(contacts):
    name = input("Enter Name: ")
    phone_number = int(input("Enter phone number: "))
    if name in contacts and contacts[name]:
        print(f"{name} has already phone number: {contacts[name]}")
    else:
        contacts[name] = phone_number
    return contacts

def show_number(contacts, name):
    if name in contacts:
        print(f"Phone number of {name} is {contacts[name]}")
    else:
        print("no contact found...!")

if __name__ == '__main__':
    contacts = {}
    while(True):
        option = int(input("1.Add Contact\n2.View Contact\nPress any other key to exit..!\nSelect Option:").strip().split()[0])
        # print(option==1)
        if (option==1 or option==2) :
            match option:
                case 1:contacts = phone_entry(contacts)
                case 2:
                    name = input("Enter name: ")
                    show_number(contacts, name)
        else:break