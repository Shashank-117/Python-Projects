#TODO: Create a letter using starting_letter.txt
with open('Input/Letters/starting_letter.txt', mode='r') as letter:
    content = letter.read()


with open('Input/Names/invited_names.txt', mode='r') as names:
    list = names.readlines()

i = 0
for name in list:
    list[i] = name.strip()
    i += 1

for person in list:
    with open(f'Output/ReadyToSend/{person}_invitation', mode='w') as invitation:
        x = content.replace('[name]', person)
        invitation.write(x)
