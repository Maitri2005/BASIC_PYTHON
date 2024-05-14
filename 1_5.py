def palindrome(str):
    str2 = str[::-1]
    if(str2==str):
        return True
    else:
        return False
print(palindrome("mahi"))