def ispalindrome(a):
    return a == a[::-1]

string = str(input("enter the string:"))

result = ispalindrome(string)

print(result)

if result:
    print("it is an palindrome string")
else:
    print("it is not an palindrome string")