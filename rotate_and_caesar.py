def rotate (text, key) :
    
    alp = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    new_text = text.replace(" ","")
    i = 0
    a = len(new_text)
    b = len(key)
    
    while len(key) < len(new_text):
        key += key
    key = key[:len(new_text)]
    
    print(new_text)
    print(key)
    
    while i<a :
        out = out + caesar(alp.index(key[i].lower()), new_text[i])
        i = i+1
        
    result = list(out)
    
    for i, char in enumerate(text):
        if char == " ":
            result.insert(i, " ")
    result = "".join(result)
                
    return result
    
def caesar (key, string) :
    
    out = ""
    alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    if key>0 :
        key = key%26
    else :
        key = -key%26
        key = -key
    
    for i in range (len(string)) :
        for j in range (len(alp)) :
            if string[i].lower() == alp[j]:
                    if string[i].isupper() == True:
                       var = (alp[(j + key) % 26]).upper()
                    else :
                       var = alp[(j + key) % 26]
                    out = out + var
    
    return out