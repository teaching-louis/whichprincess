answer = input("""I'm proud of myself for...
1. Stepping out of my comfort zone
2. Learning new things about myself\n""")
if answer == "1":
    answer = input("""I think it's important too...
    1. fight for what I believe in
    2. explore new places
    3. create my own path\n""")
    if answer == "1":
        answer = input("""People think I'm...
        1. loyal and courageous
        2. creative and artistic\n""")
        if answer == "1":
            print("You're Mulan!")
        elif answer == "2":
            print("You're Rapunzel")
    elif answer == "2":
        answer = input("""I'd want my pet to be...
        1. something scaly
        2. something fuzzy\n""")
        if answer == "1":
            print("You're Rapunzel")
        elif answer == "2":
            print("You're Moana")
    elif answer == "3":
        answer = input("""In life, I prefer to...
        1. plan ahead
        2. go with the flow\n""")
        if answer == "1":
            print("You're Moana")
        elif answer == "2":
            print("You're Jasmine")
elif answer == "2":
    answer = input("""My biggest strength is that I'm...
    1. a leader
    2. a visionary
    3. determined\n""")
    if answer == "1":
        answer = input("""In life, I prefer to...
                1. plan ahead
                2. go with the flow\n""")
        if answer == "1":
            print("You're Moana")
        elif answer == "2":
            print("You're Jasmine")
    elif answer == "2":
        answer = input("""You'll find me...
        1. going on new adventures
        2. working towards my dreams\n""")
        if answer == "1":
            print("You're Jasmine")
        elif answer == "2":
            print("You're Tiana")
    elif answer == "3":
        answer = input("""I like to spend time...
        1. cooking
        2. playing sports\n""")
        if answer == "1":
            print("You're Tiana")
        elif answer == "2":
            print("You're Merida")