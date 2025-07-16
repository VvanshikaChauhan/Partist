def plan_vibe():
    print("\n\nAwesome! Let's figure out your vibe for today. Whether you are just looking to unwind, planning a small hangout or something a little louder. I'll help you with some easy suggestions for music, snacks, and all those little details that make it feel right.")
    print("-"*40)
    print("\n\nWhat kind of mood are you feeling right now?")
    print("1. Chill & Cozy [~]")
    print("2. Light & Fun [!]")
    print("3. Loud & Energetic [^]")
    print("4. Creative & Artsy [*]")
    print("5. Nostalgic & Sentimental [<3]")
    print("6. Productive but Relaxed [>>]")
    
    mood_choice=input("Enter the number to let me know your choice (from 1 to 6): ")

    print("\nHow many people are we talking about?")
    print("1. Just me, solo vibes(I love thiss..)")
    print("2. A few friends, around 5-6")
    print("3. A whole bunch, let's go big!")

    group=input("Enter the number for the group count (from 1 to 3): ")

    print("\nGotcha, here is your plan for today:\n")
    
    if mood_choice =='1':
        if group == '1':
            print("🎵 Playlist: Lo-fi or Jazz")
            print("☕ Snack: Tea, cookies")
            print("🛋️ Vibe: Dim lights, blanket, maybe journaling.")
        elif group == '2':
            print("🎵 Playlist: Acoustic Coffeehouse")
            print("🍰 Snack: Cake, tea, light convos")
            print("🕯️ Vibe: Slow games, comfy seats, warm lighting.")
        else:
            print("🎵 Playlist: Indie Chill")
            print("🍿 Snack: Finger food, mocktails")
            print("💬 Vibe: Calm but chatty, cozy gathering.")
    
    elif mood_choice == '2': 
        if group == '1':
            print("🎵 Playlist: Pop / Happy Indie")
            print("🍫 Snack: Ice cream, snacks")
            print("🎬 Activity: Light movie, comedy show.")
        elif group == '2':
            print("🎵 Playlist: Indie Pop / Throwbacks")
            print("🍕 Snack: Pizza, mocktails")
            print("🎲 Activity: Cards, light games, chats.")
        else:
            print("🎵 Playlist: Upbeat Mix / Bollywood")
            print("🍿 Snack: Popcorn, nachos")
            print("🎉 Activity: Casual games, everyone’s included.")
    
    elif mood_choice == '3':
        if group == '1':
            print("🎵 Playlist: Hype Beats, Dance Mix")
            print("🥤 Snack: Chips, soda")
            print("💃 Activity: Solo dance, fun playlist.")
        elif group == '2':
            print("🎵 Playlist: Club Remixes")
            print("🍹 Snack: Mocktails, chips")
            print("🎮 Activity: Karaoke battle, competitive games.")
        else:
            print("🎵 Playlist: Party Hits, Loud Pop")
            print("🍔 Snack: Fast food, energy drinks")
            print("🎉 Activity: Dance, karaoke, loud games.")
    
    elif mood_choice == '4':
        if group == '1':
            print("🎵 Playlist: Instrumental / Indie")
            print("☕ Snack: Coffee, light snacks")
            print("🎨 Activity: Painting, writing, DIY.")
        elif group == '2':
            print("🎵 Playlist: Indie Chill")
            print("🥐 Snack: Light snacks, tea")
            print("🖌️ Activity: Sketching, crafts, relaxed chats.")
        else:
            print("🎵 Playlist: Indie Pop, Background Beats")
            print("🍰 Snack: Cake, snacks")
            print("🎨 Activity: Group crafts, art games.")
    
    elif mood_choice == '5':
        if group == '1':
            print("🎵 Playlist: Old love songs / Throwbacks")
            print("🍫 Snack: Hot cocoa, popcorn")
            print("📺 Activity: Classic movies, photo albums.")
        elif group == '2':
            print("🎵 Playlist: Retro Pop / 90s Vibes")
            print("🍕 Snack: Pizza, soda")
            print("📷 Activity: Photo sharing, old games.")
        else:
            print("🎵 Playlist: Throwbacks, Anthems")
            print("🍰 Snack: Cake, snacks")
            print("🎉 Activity: Sharing stories, old songs.")
    
    elif mood_choice == '6':
        if group == '1':
            print("🎵 Playlist: Chill Beats / Lo-fi")
            print("🥤 Snack: Coffee, light snacks")
            print("💻 Activity: Reading, soft focus work.")
        elif group == '2':
            print("🎵 Playlist: Calm Pop, Study Playlist")
            print("🥪 Snack: Sandwiches, tea")
            print("🖥️ Activity: Co-working, light chat.")
        else:
            print("🎵 Playlist: Ambient, Focus Music")
            print("🥗 Snack: Light bites, water")
            print("👥 Activity: Group study, project work.")
    
    else:
        print("\nOops! That wasn't one of the options.")
        print("Let's just say: trust your own vibe today. 🙂")
        print("🎵 Playlist: Anything you like!")
        print("🍿 Snack: Whatever’s nearby.")
    print("- " * 40)
    print("\nThat's awesome for now... head back to the main menu whenever you're ready!\n")
    input("Press Enter to return to the main menu...")