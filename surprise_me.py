import random
def surprise_me():
    print("\n🎲 Welcome to 'Surprise Me' Mode!\n")
    print("Not sure where to start? Let me suggest a simple combination for you.\n")
    print("-" * 40)

    playlists = [
        "Indie Pop Hits",
        "Retro Bollywood Classics",
        "Chill Lo-fi Beats",
        "90s Rock Anthems",
        "Jazz & Coffeehouse Vibes",
        "Upbeat Dance Mix"]

    snacks = [
        "Popcorn & Mocktails",
        "Nachos & Cheese Dip",
        "Tea & Cookies",
        "Pizza Slices",
        "Chips & Dip",
        "Hot Chocolate & Cake"]

    activities = [
        "A quick karaoke session 🎤",
        "A short dance break 💃",
        "Watch a light-hearted movie",
        "Doodle or sketch for fun~~",
        "Play a game of 'Would You Rather?' 🤔",
        "Plant a time capsule just for fun"]

    ambience = [
        "Soft fairy lights and candles",
        "Bright lights with cheerful energy",
        "Open windows and fresh air",
        "Blankets and pillows in a quiet corner",
        "Background music and soft lighting"]

    cheat_preferences = [
        "A peaceful mix of tea, soft music, and a cozy seat rarely goes wrong.",
        "Music and snacks with a familiar movie can make any day feel lighter.",
        "Warm lighting, light conversation, and soft music often create the right mood.",
        "A calm playlist and something small to enjoy often work best when unsure.",
        "A few favorite songs and your comfort snack might be all you need today."]

    print(f"🎵 Playlist: {random.choice(playlists)}")
    print(f"🍿 Snack: {random.choice(snacks)}")
    print(f"🎉 Activity: {random.choice(activities)}")
    print(f"✨ Ambience: {random.choice(ambience)}")
    print("\n💡 Personal Cheat Preference:")
    print(random.choice(cheat_preferences))
    print("- " * 40)
    print("\nThat's awesome for now... head back to the main menu whenever you're ready!\n")
    input("Press Enter to return to the main menu...")