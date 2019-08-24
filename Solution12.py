def merge_the_tools(string, k):
    # your code goes here
    length=len(string)
    if(length%k==0 and length>=1 and length<=10**4 and k>=1 and k<=length):
        l=list(string)
        for i in range(0,length,k):
            newl=l[i:i+k]
            final=[]
            for j in range(k):
                if newl[j] not in final:
                    final.append(newl[j]) 
            print(''.join(final))

