def saved_combo():
    print("\nYOUR SAVED COMBOS\n")
    print("Here’s a list of the playlists, snack ideas, or vibe suggestions you’ve saved before.")
    print("Use this as a quick inspiration board when planning your next vibe.\n")

    try:
        with open("custom_suggestions.txt", "r") as file:
            combos = file.readlines()
            if combos:
                for item in combos:
                    print(f"- {item.strip()}")
            else:
                print("(No saved combos yet)")
    except FileNotFoundError:
        print("(No saved combos yet)")
    print("- " * 40)
    print("\nThat's awesome for now... head back to the main menu whenever you're ready!\n")
    input("Press Enter to return to the main menu...")