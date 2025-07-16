def add_suggestion():
    print("\nADD YOUR OWN SUGGESTION ✏️\n")
    print("If you have your own playlist idea, snack combo, or vibe you'd like to save for later, just type it below and I'll keep it safe for you!\n")

    suggestion = input("Write your suggestion or idea: ")
    with open("custom_suggestions.txt", "a") as file:
        file.write(suggestion + "\n")

    print("\n✅ Your suggestion has been saved!\n")
    print("- " * 40)
    print("\nThat's awesome for now... head back to the main menu whenever you're ready!\n")
    input("Press Enter to return to the main menu...")