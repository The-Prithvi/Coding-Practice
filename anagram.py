def anagram(s1, s2):

    s1 = s1.strip()
    s1 = s1.lower()
    s2 = s2.strip()
    s2 = s2.lower()

    if len(s1) != len(s2):
        flag = 1
        return False

    else:
        return sorted(s1) == sorted(s2)
 


if anagram("Prithvi", "ivhtpusi"):
    print("Anagram")
else:
    print("Not Anagram")