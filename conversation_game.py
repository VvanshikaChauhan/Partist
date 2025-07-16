import random
def conversation_game():
    print("\nCONVERSATION STARTER MODE 🗣️\n")
    print("What kind of question would you like to explore?")
    print("1. Light & Personal (Memories / Simple Things)")
    print("2. Thoughtful & Calm (Preferences / Ideas / Reflections)")
    print("3. Random Mix (Everyday Topics / Small Debates / Curiosities)")

    choice=input("Enter the number for the choice (from 1 to 3): ")
    if choice == "1":
        question = random.choice([
            "What’s a small childhood memory that still makes you smile?",
            "Is there a place you visited once that you’d love to go back to?",
            "What’s your favorite way to spend a calm weekend?",
            "Do you have a simple routine that brings you comfort?"])

    elif choice == "2":
        question = random.choice([
            "If you had to choose one skill to improve this year, what would it be?",
            "What’s something about your culture or hometown that you truly value?",
            "If you could slow down time for one thing in life, what would it be?",
            "What’s a thought or philosophy that stays with you even now?"])

    else:
        question = random.choice([
            "What’s one topic you think people should discuss more openly?",
            "Is there a book, movie, or song that changed your perspective in some way?",
            "What’s something people often overlook in daily life but shouldn’t?",
            "If you could remove one small inconvenience from daily life, what would it be?",
            "What’s something people often misunderstand about you?",
            "If you had to explain your personality using a season, which would it be and why?",
            "What’s one small thing that makes you feel unexpectedly proud?",
            "If you could invite three people from any era to a conversation, who would they be?"])
    print("\n💬 Here's your conversation starter:\n")
    print(f"'{question}'\n")
    print("- " * 40)
    print("\nThat's awesome for now... head back to the main menu whenever you're ready!\n")
    input("Press Enter to return to the main menu...")