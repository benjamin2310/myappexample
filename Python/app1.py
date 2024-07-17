spam = 9

if spam < 5:
    print("Hello World")
    spam = spam + 1
else:
    print('None of the above')
spam = 0

while spam < 5:
    print("Newmont Ghana")
    spam = spam + 1
    print(spam)


nameOfAgent = ""

while nameOfAgent != 'Benjamin':
    print("please type your name: ")
    nameOfAgent = input()
print('Thank you')

while True:
    print('Please enter your name')
    nameOfAgent = input()
    if nameOfAgent == 'your name':
        break
print("Not it, try again later!")
