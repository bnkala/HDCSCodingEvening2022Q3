def allAboutStrings(string):
    #empty list
    lst = [] 
    #length of the string
    len_string = len(string)
    #first character of the string
    first = string[0]
    #last character of the string
    last = string[-1]
    #characters added into the list
    lst.append(len_string)
    lst.append(first)
    lst.append(last)
    #determine whether the length of the character is even or odd
    mid = len_string % 2
    #get the index of the middle character
    div = len_string // 2
    
    if (mid == 0):
        div -= 1
        lst.append(string[div]+string[div+1])
    else:
        lst.append(string[div])

    for i in string:
        if (i not in string):
            lst.append("not found")    

    print(lst)

allAboutStrings("bryan")
