import random

words_list = ["harry potter", "lord of the ring", "spiderman", "the dark knight"]

secret_word = random.choice(words_list) 

dashed_word = ["_" for char in secret_word if char != " "]

secret_word = [char for char in secret_word if char != " "]

wrong_gusses = 0

chosed_letters = set()


print("*" * 20)
print("Welcom To Hang-Man Game")
print("*" * 20)


while wrong_gusses != 6 :

    print(" ".join(dashed_word))

    choice = input("please select a letter (a-z) ").lower()

    if (len(choice)) != 1 or choice.isalpha == False :

        print("InValid Input")

        continue

    if choice in chosed_letters :

        print("you already chosed this letter")

        continue

    chosed_letters.add(choice)

    if choice in secret_word :

        print("you guessed correctly ")

        for i in range(len(secret_word)) :

            if secret_word[i] == choice :

                dashed_word[i] = choice

    elif choice not in secret_word :

        print("sorry, you gussed wrong")

        wrong_gusses += 1

    if "_" not in dashed_word :

        print(f"you guessed the secret word : {" ".join(dashed_word)} : coreectly")

        print("Congrats You WIN!!!")

        break
    
    if wrong_gusses == 6 :

        print("sorry, You LOST!!!")

        print("Better Luch Next Time")

        print(f"The Word Was : {" ".join(secret_word)}")

print("*" * 30)
print("Thanks For Playing..")
print("*" * 30)







