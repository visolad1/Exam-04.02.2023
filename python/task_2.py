string = input("Enter the string : ")
substring = input("Iput the substring to search : ")

if substring in string:
    print("The substring exists in the string.")
else:
    print("Substring does not exist in string.")