def revrese_words(sentence):
    words = sentence.split()
    result = []
    for i in range(len(words) -1,-1,-1):
        result.append(words[i])
    return" ".join (result)
# text ="Python is awesome" 
print(revrese_words("Python is awesome"))

def repeating(str):
    

                    