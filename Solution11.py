def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    new=''.join(l)
    return(new)

