#Tier 1 Answers
root_question = ("I'm proud of myself for...\n"
                "1. Stepping out of my comfort zone\n"
                "2. Learning new things about myself\n")
is_stepping_out_comfort_zone = False
is_learning_new_things = False

#Tier 2 Answers
tier_2_question_1 = ("I think it's important too...\n"
        "1. fight for what I believe in\n"
        "2. explore new places\n"
        "3. create my own path\n")
will_fight_for_what_I_believe_in = False
will_explore_new_places = False
will_create_my_own_path = False

tier_2_question_2 = ("My biggest strength is that I'm...\n"
        "1. a leader\n"
        "2. a visionary\n"
        "3. determined\n")
is_a_leader = False
is_a_visionary = False
is_determined = False

#Tier 3 Answers
is_loyal_and_courageous = False
is_creative_and_artistic = False

pet_is_scary = False #Spelling mistake
pet_is_fuzzy = False

life_plan_ahead = False
life_go_flow = False

find_me_adventutres = False #Spelling mistake
find_me_dreams = False

spend_time_cooking = False
spend_time_sports = False

#Tier 1 Questions
answer = input(root_question)
if answer == "1":
    is_stepping_out_comfort_zone = True
elif answer == "2":
    is_learning_new_things = True

#Tier 2 Questions
#Left Side
if is_stepping_out_comfort_zone == True:
    answer = input(tier_2_question_1)
    if answer == "1":
        will_fight_for_what_I_believe_in = True
    elif answer == "2":
        will_explore_new_places = True
    elif answer == "3":
        will_create_my_own_path = True
#Right Side
elif is_learning_new_things == True:
    answer = input(tier_2_question_2)
    if answer == "1":
        is_a_leader = True
    elif answer == "2":
        is_a_visionary = True
    elif answer == "3":
        is_determined = True

#Tier 3 Questions
if will_fight_for_what_I_believe_in == True:
    answer = input("""People think I'm...
            1. loyal and courageous
            2. creative and artistic\n""")
    if answer == "1":
        is_loyal_and_courageous = True
    elif answer == "2":
        is_creative_and_artistic = True
elif will_explore_new_places == True:
    answer = input("""I'd want my pet to be...
            1. something scaly
            2. something fuzzy\n""")
    if answer == "1":
        pet_is_scary = True
    if answer == "2":
        pet_is_fuzzy = True
elif will_create_my_own_path == True or is_a_leader:
    answer = input("""In life, I prefer to...
                   1. plan ahead
                   2. go with the flow\n""")
    if answer == "1":
        life_plan_ahead = True
    elif answer == "2":
        life_go_flow = True
elif is_a_visionary == True:
    answer = input("""You'll find me...
            1. going on new adventures
            2. working towards my dreams\n""")
    if answer == "1":
        find_me_adventutres = True
    elif answer == "2":
        find_me_dreams = True
elif is_determined == True:
    answer = input("""I like to spend time...
           1. cooking
           2. playing sports\n""")
    if answer == "1":
        spend_time_cooking = True
    elif answer == "2":
        spend_time_sports = True

if is_loyal_and_courageous:
    print("You are Mulan!!")
elif is_creative_and_artistic or pet_is_scary:
    print("You are Rapunzel!!")
elif pet_is_fuzzy or life_plan_ahead:
    print("You are Moana!!")
elif life_go_flow or find_me_adventutres:
    print("You are Jasmine!!!")
elif find_me_dreams or spend_time_cooking:
    print("You are Tiana!!")
elif spend_time_sports:
    print("You are Merida!!")


