# Password breaker and password generator
import random
import time
ch = "abcdefghijklmnopqurstuvwxyz1234567890!@#$%^&*()--+=AVCDEFGHIJKLMNOPQRSTUVWXYZ"
guess=''
password=""
length = int(input("Enter the length"))
lngth_half=int(length/2)
for i in range(lngth_half):
    password += random.choice(ch[:4])
for i in range(0,length-lngth_half):
    password += random.choice(ch)
print(password)
user_inpt=input("You want to know if your password is easily breakable? (Yes/No)\n")
def passbrk():
    while True:    
        guess=random.choices(ch, k=len(password))
        guess=''.join(guess)
        print(guess)
        if guess==password:
            print(f"Your pass is {guess}")
            break
init = time.time()
strong =time.time()-init         
if user_inpt=="Yes":
    a = passbrk()
    print(f"Time taken in is {strong}s")
else:
    print("You didn't choose your password to be broken")
if strong >= 100:
    print("Your password was stronger and was tough to break")
else:
    print("Your pass was easily breakable")
