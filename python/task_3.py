string = input("Enter the string: ").lower()
c = 0

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for l in letters:
    if l in string:
        c += 1

if c == 26 : print("true")
else: print('false')