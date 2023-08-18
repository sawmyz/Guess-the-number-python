import random

random_number = random.randint(0,100)
user_numbr = int(input("hii, my developer is SamanRezagholi , please send me a number between 0 to 100:"))

while user_numbr != random_number :
# if userNumberInput not equal with randNumber :
    if user_number > random_number :
        print (f"nooo :( , {user_numbr} is big")
        user_number = int(input("please send me a number:"))

    else : 
        print (f"nooo :( , {user_numbr} is small")
        user_number = int(input("please send me a number:"))

print (f"good, correctNumber is {random_number} and your answer is {user_numbr}")                  