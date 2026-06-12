import random
game = ['snake', 'water', 'gun']
C_choice = random.choice(game)

print("\n<~you are in snake, water and gun game~>")
your_choice = input("snake, water, gun choose one: ")

# snake > water
# snake < gun
# water > gun

print(f"\ncomputer choose: {C_choice}")
print(f"You choose: {your_choice}")

if (C_choice==your_choice):
    print("\nits a draw")

if (C_choice=="snake" and your_choice=="water"):
    print("\ncomputer wins")

if (C_choice=="water" and your_choice=="gun"):
    print("\ncomputer wins") 

if (C_choice=="gun" and your_choice=="snake"):
    print("\ncomputer wins")  

if (your_choice=="snake" and C_choice=="water"):
    print("\nyou wins")

if (your_choice=="water" and C_choice=="gun"):
    print("\nyou wins")

if (your_choice=="gun" and C_choice=="snake"):
    print("\nyou wins")    