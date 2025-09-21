import random

def game():
    print("Snake 🐍  Water 💧  Gun 🔫")
    choices = ["snake", "water", "gun"]

    user = input("Enter your choice (snake/water/gun): ")

    if user not in choices:
        print("⚠️ Wrong input! Please choose snake, water, or gun.")
        return 
    comp = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a Draw!")
    elif (user == "snake" and comp == "water") or \
         (user == "water" and comp == "gun") or \
         (user == "gun" and comp == "snake"):
        print("🎉 You Win!")
    else:
        print("😢 You Lose!")

game()