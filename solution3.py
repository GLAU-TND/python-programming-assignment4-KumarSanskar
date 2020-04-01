ls = eval(input("enter a list "))  # user enter a list with elements
a = eval(input("enter the query string "))  # user enters a query-string to find element starting with it as a prefix in list
b = []
for i in ls:
    if i.startswith(a)==True:
        b.append(i)
print(b)
