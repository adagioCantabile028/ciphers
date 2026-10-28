import cleanup

alphabet = keystring = list('abcdefghijklmnopqrstuvwxyz')

def shuffle(key,char):
    blocka = key[:key.index(char)]
    blockb = key[key.index(char) + 1:]
    
    return blockb + [char] + blocka
    
def encrypt(keyword,plaintext,option):    
    global keystring
    ciphertext = ''
    
    for char in keyword:
        keystring = shuffle(keystring,char)

    for char in plaintext:
        if option == 'e':
            ciphertext += keystring[alphabet.index(char)]
            keystring = shuffle(keystring,char)
        elif option == 'd':
            ciphertext += alphabet[keystring.index(char)]
            keystring = shuffle(keystring,alphabet[keystring.index(char)])

    return ciphertext

if __name__ == '__main__':
    print('Welcome to the scrabble cipher encoder/decoder!')
    print()
    plaintext = cleanup.clean(input('Enter your message: '))
    keyword = cleanup.clean(input('Enter your keyword: '))
    option = input('Enter e for encrypt or d for decrypt: ')
    print()
    print(encrypt(keyword,plaintext,option))

