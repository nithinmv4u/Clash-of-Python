class Account_holder():
    def __init__(self,name,account_num):
        self.name=name
        self.account_num=account_num

    def __str__(self):
        return f"Name: {self.name}\nAccount Number: {self.account_num}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name=name

    @property #--------GETTER--------
    def account_num(self):
        return self._account_num
    @account_num.setter  #--------SETTER---------
    def account_num(self,account_num):
        print('Caution : Accessing account number........!!!')
        self._account_num=account_num


def main():
    account_holder=get_account_holder()
    print(account_holder)

def get_account_holder():
    name=input('Enter name: ')
    account_num=input('Enter account number: ')
    account_holder=Account_holder(name,account_num)
    return account_holder

main()