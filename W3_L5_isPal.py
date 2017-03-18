def isPalindrome(s):
    if len(s) >=0:
        return isPalindrome(s[1:-1])
    
s = 'saasdkljsajsd'
print isPalindrome(s)
