import cleanup

alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = input('Input message: ')
keyword = input('Input keyword: ')

message = cleanup.clean(message)
keyword = cleanup.clean(keyword)

encryption = ''
counter = 0
for i in message:
    encryption += alphabet[(alphabet.find(i) + alphabet.find(keyword[counter % len(keyword)])) % 26]
    counter += 1
print(encryption)
