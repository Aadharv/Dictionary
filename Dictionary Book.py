import json
from difflib import get_close_matches
from tkinter import W
data=json.load(open('Words.json'))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        y=input('Did you mean %s instead?Enter Y if yes and N if no.'%get_close_matches(w,data.keys())[0])
        y=y.lower()
        if y=='y':
            return data[get_close_matches(w,data.keys())[0]]
        elif y=='n':
            return "The word doesn't exist"
        else:
            return 'We didnt understand your entry'
    else:
        return "The word doesn't exist"

word=input("Please enter your word")
output=translate(word)

if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
input("Press ENTER to exit")