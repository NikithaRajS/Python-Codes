def count_substring(string, sub_string):
    c=0
    string.lower()
    sub_string.lower()
    l1=len(string)
    l2=len(sub_string)
    for i in range(l1):
        if string[i]==sub_string[0]:
            news=string[i:i+l2]
            if(news==sub_string):
                c+=1
    return(c)

