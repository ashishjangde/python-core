a = True
print(a:=False)

b = [1, 2, 3 , 4 , 5, 6 , 7 , 8]

while (n := len(b)) > 0:
    print(b.pop())\
        

lis = list()
while(n := input("Enter the name of fruits you would like to eat: ") ) != "quit":
    lis.append(n)
    
print(lis)