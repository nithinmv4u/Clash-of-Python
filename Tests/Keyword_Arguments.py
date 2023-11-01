def car(speed, color='red', company='Tata'):
    print(f"This car is from {company} with color {color} and a speed of {speed}")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw]) #------key - value pair---------

car(speed=130)
car(speed=150)
car(color='blue', speed=120)
car(company='Mahindra', speed=160)
# speed is required argument here-------


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")