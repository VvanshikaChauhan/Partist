import random
def emergency_chill_mode():
    quotes = [
        "“Almost everything will work again if you unplug it for a few minutes... including you.” — Anne Lamott",
        "“Rest is not idle, it’s not wasteful. Sometimes rest is the most productive thing you can do.”",
        "“You do not have to be ready for everything. You only have to take this one moment slowly.”",
        "“Quiet moments are not empty. They’re quietly refilling you.”",
        "“Pause. Breathe. Somewhere, soft things are waiting for you to notice them again.”"]

    book_inspo = [
        "Try reading a few pages of *The Little Prince* — sometimes small stories help big feelings.",
        "Open a poetry book. Even one gentle line can give you space to breathe again.",
        "Reread something familiar. Comfort often lives in pages we already know.",
        "Pick a calm, quiet short story. The goal isn’t to finish, only to soften the moment."]

    print("\n🕯️ EMERGENCY CHILL MODE ACTIVATED 🕯️\n")
    print("We all have those moments when things feel too loud, too fast, or simply too much.")
    print("This isn't about fixing everything. It's just a small pause to help you reset.")
    print("Breathe. Slow down. Let’s keep this simple and gentle.\n")
    print("- " * 40)

    print("🎵 Playlist: Calm Lo-fi or Soft Instrumentals")
    print("Snack: Herbal tea or light cookies")
    print("Activity: Light reading, a short journal entry, or simply sitting quietly")
    print("✨ Ambience: Soft lighting, phone on silent, take 10 slow breaths")
    print("- " * 40)

    print("\n💭 A Small Thought for You:\n")
    print(random.choice(quotes))

    print("\nA Gentle Suggestion:\n")
    print(random.choice(book_inspo))
    print("- " * 40)
    print("\nThat's awesome for now... head back to the main menu whenever you're ready!\n")
    input("Press Enter to return to the main menu...")