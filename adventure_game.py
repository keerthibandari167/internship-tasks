def start_adventure():
    print("🏕️ Welcome to the Jungle Adventure!")
    print("You're exploring a mysterious jungle and come across two paths.\n")

    choice1 = input("Do you want to go left towards the river or right into the dark cave? (left/right): ").lower()

    if choice1 == "left":
        river_path()
    elif choice1 == "right":
        cave_path()
    else:
        print("❌ Invalid choice. The jungle swallows you. Game over.")

def river_path():
    print("\n🌊 You follow the river and hear something splashing.")
    choice2 = input("Do you want to investigate the noise or keep walking along the river? (investigate/walk): ").lower()

    if choice2 == "investigate":
        print("\n🐊 Oh no! It was a crocodile! You tried to run, but it was too late.")
        print("💀 You died. Game over.")
    elif choice2 == "walk":
        print("\n🏞️ You find a small boat tied to a tree.")
        choice3 = input("Do you take the boat or continue on foot? (boat/foot): ").lower()

        if choice3 == "boat":
            print("\n🚣 You paddle downstream and reach a friendly village. You're safe!")
            print("🎉 You survived the adventure!")
        elif choice3 == "foot":
            print("\n🐍 A snake bites you while walking through thick grass. You collapse.")
            print("💀 You died. Game over.")
        else:
            print("❌ Invalid choice. You hesitated too long and got lost.")
    else:
        print("❌ Invalid choice. You got confused and wandered off the path.")

def cave_path():
    print("\n🕳️ You walk into the dark cave. It's cold and echoey.")
    choice2 = input("You see a glowing light. Do you approach it or hide behind a rock? (approach/hide): ").lower()

    if choice2 == "approach":
        print("\n🧙 A wise old hermit greets you and shows you a secret exit.")
        print("🎉 You escaped safely. You win!")
    elif choice2 == "hide":
        print("\n👹 A monster finds you hiding and attacks!")
        print("💀 You died. Game over.")
    else:
        print("❌ Invalid choice. You panic and run into a dead end.")

if __name__ == "__main__":
    start_adventure()
