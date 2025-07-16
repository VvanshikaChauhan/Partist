import os
os.system('cls')
def menu():
    print("🎨 WELCOME TO PARTIST!!!🎉\n",)
    print("Your all-time party prep companion\n")
    print("You pick the v~i~b~e... I'll cue the rest\n")
    print("- ~ "*40)
    print("\nWhat would you like to do today?\n")
    print("1. Plan a Vibe 🎧🍿")
    print("2. Surprise Me! 😮")
    print("3. Emergency Chill Mode 🕯️")
    print("4. Conversation Game 🎲")
    print("5. View Saved Combos 📁")
    print("6. Add Your Own Suggestions ✍️")
    print("7. Exit ❌")

from plan_vibe import plan_vibe
from surprise_me import surprise_me
from emergency_chill_mode import emergency_chill_mode
from conversation_game import conversation_game
from saved_combo import saved_combo
from add_suggestion import add_suggestion

while True:
    menu()
    choice=input("Enter your choice (from 1 to 7): ")

    if choice == '1':
        plan_vibe()
    elif choice == '2':
        surprise_me()
    elif choice == '3':
        emergency_chill_mode()
    elif choice == '4':
        conversation_game()
    elif choice == '5':
        saved_combo()
    elif choice == '6':
        add_suggestion()
    elif choice == '7':
        print("\nThanks for using Partist! See you at the next hangout. 👋\n")
        break
    else:
        print("\n!!! Invalid input. Please enter a number from 1 to 7 !!!\n")