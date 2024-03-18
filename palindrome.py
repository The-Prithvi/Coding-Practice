def palindrome(str):
    str = str.lower()
    s = ""
    for i in str:
        s = i + s
    
    if str == s:
        print("\"" + str + "\"" +" is Palindrome")
    else:
        print("\"" + str + "\"" +" is Not Palindrome")

palindrome("Prithvi")
palindrome("MOM")

