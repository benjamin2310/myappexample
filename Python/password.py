# while True:
#     print("Please enter your name: ")
#     userName = input()
#     if userName != "Joe":
#         continue
#         print("Hello, Joe.  what is your password?(It is a fish.)")
#     password = input()
#     if password == "swordfish":
#         break
# print("Access granted")

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')