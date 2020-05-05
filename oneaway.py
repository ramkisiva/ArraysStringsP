s1 = input("Enter first String:")
s2 = input("Enter second string:")
def oneaway(s1,s2):
    if (abs(len(s1)-len(s2))>1):
        return False
    if len(s1)>len(s2):
        largerString = s1
        smallerString = s2
    else:
        largerString = s2
        smallerString = s1
    mismatchFound = False
    sIndex=0
    lIndex=-1
    sameLength = False
    if len(s1)==len(s2):
        sameLength = True  
    while sIndex<len(smallerString):
        lIndex = lIndex + 1
        if(smallerString[sIndex]!= largerString[lIndex]):
            if not mismatchFound :
                mismatchFound = True
                if not sameLength:
                    continue
            else:
                return False
        sIndex = sIndex + 1
        
    return True

print("Strings are one character away :",oneaway(s1,s2))
