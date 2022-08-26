#print all permutations of string
def permute(s, a):
    if (len(s) == 0):
        print(a )
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, a + ch)
a = ""
s = input("Enter the string : ")
print("All possible strings are ")
permute(s, a)