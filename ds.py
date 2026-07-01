def revrese_words(sentence):
    words = sentence.split()
    result = []
    for i in range(len(words) -1,-1,-1):
        result.append(words[i])
    return" ".join (result)
# text ="Python is awesome" 
print(revrese_words("Python is awesome"))

def repeating(str):


def inpt_str():
    s1 = input("Enter first string 1: ")
    s2 = input("Enter first string 2: ")
    return s1, s2

def rot_str(s1,s2):
    if len(s1) != len(s2):
        return False
    s= s1 +s1
    if s2 in s:
        return True 
    
s1,s2 = inpt_str()
rot_str(s1,s2)

                    