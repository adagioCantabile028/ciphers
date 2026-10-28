# cleans up strings before encryption
# converts to lowercase, and removes non-alphabetic characters

def clean(message):
    cleaned = ""
    for i in message:
        if i.isalpha():
            cleaned += i.lower() 
    return cleaned
