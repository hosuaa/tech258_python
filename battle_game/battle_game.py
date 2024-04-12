# Battle game
import random

classes = ["fighter", "archer", "mage"]
actions = ["attack", "parry", "heal"]

# Get user's class
user_class = input("Enter your chosen class (Fighter, Archer, Mage): ")
user_hp = 3

cpu_class = classes[random.randint(0, 2)]
cpu_hp = 3

while user_hp > 0 and cpu_hp > 0:
    print(f"Current hp: {user_hp}")
    print(f"Enemy hp: {cpu_hp}")

    user_action = input("Attack, Parry or Heal? ")
    cpu_action = actions[random.randint(0, 2)]
    print(f"Enemy used {cpu_action}")

    if user_action == "attack":
        if cpu_action == "attack":
            user_hp -= 1
            cpu_hp -= 1
            print("Both took damage")
        if cpu_action == "parry":
            user_hp -= 1
            print("Enemy parried")
        if cpu_action == "heal":
            cpu_hp -= 1
            print("Enemy heal failed")
    if user_action == "parry":
        if cpu_action == "attack":
            cpu_hp -= 1
            print("User parried")
        if cpu_action == "parry":
            user_hp -= 1
            cpu_hp -= 1
            print("Fail. Both take damage")
        if cpu_action == "heal":
            cpu_hp += 1
            print("Enemy healed")
    if user_action == "heal":
        if cpu_action == "attack":
            user_hp -= 1
            print("User heal failed")
        if cpu_action == "parry":
            user_hp += 1
            print("User healed")
        if cpu_action == "heal":
            user_hp += 1
            cpu_hp += 1
            print("Both healed")

if user_hp == 0 and cpu_hp == 0:
    print("Draw")
elif user_hp == 0:
    print("Enemy won")
else:
    print("You won")
