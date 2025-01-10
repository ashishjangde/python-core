age = int(input("Enter your age: "))

match age:
    case 0:
        print("You are a new born baby")
    case _ if 0 < age < 3:
        print("You are a toddler")
    case _ if 3 <= age < 6:
        print("You are a preschooler")
    case _ if 6 <= age < 12:
        print("You are a kid")
    case _ if 12 <= age < 18:
        print("You are a teenager")
    case _ if 18 <= age < 21:
        print("You are a young adult")
    case _ if 21 <= age < 60:
        print("You are an adult")
    case _ if 60 <= age < 100:
        print("You are a senior citizen")
    case _:
        print("You are a centenarian")
        
        