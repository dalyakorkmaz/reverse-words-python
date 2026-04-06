def reverse(value):
    sentence = ""
    w = ""
    for i in value:
        if i != ' ':
            w += i
        else:
            if (len(w) > 0):
                r = ""
                for j in range(len(w) - 1, -1, -1):
                    r += w[j]
                sentence += r + " "
                w = ""
    if (len(w) > 0):
        r = ""
        for j in range(len(w) - 1, -1, -1):
            r += w[j]
        sentence += r + " "
        w = ""
    
    return sentence

a = "hello world"
print(reverse(a))
    

            
            


            
            
        


        