a = eval(input())  # takes input from user
ls = eval(input())  # user will input a list with certain elements
b = []
for i in ls:
    if i.startswith(a)==True:
        b.append(i)
print(b)