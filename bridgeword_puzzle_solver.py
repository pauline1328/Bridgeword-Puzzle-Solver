import sys
from german_nouns.lookup import Nouns

userstarts = []
userends = []
gap_counts = []

nouns = Nouns()

try:

    print("\n\nWelcome to the \"Bridgeword Puzzle Solver\"!!!\n")

    t = 0

    while True:
        try:
            total = int(input("Number of total words to look for: "))
            break
        except ValueError:
            continue


    while t != total: 

        t += 1

        print(f"\n{t}")

        us, ue, gc = "", "", ""

        while us.isalpha() == False or " " in us:
            us = input("Begin word: ").lower()
        while ue.isalpha() == False or " " in ue:
            ue = input("End word: ").lower()
        while gc.isdigit() == False:
            gc = input("Gap between count: ")


        userstarts.append(str(us))
        userends.append(str(ue))
        gap_counts.append(int(gc))

    z = 0
    print("\n\nSolutions: ")

    for userstart, userend, gap_count in zip(userstarts, userends, gap_counts):

        candidates1 = []
        candidates2 = []

        z += 1

        first_part = len(userstart) + gap_count

        with open("german_words.txt", encoding="utf-8") as f:
            german_words = {line.strip() for line in f if line.strip().isalpha()}

            for compound in german_words:
                if len(compound) == first_part:
                    if compound.lower().startswith(userstart):

                        word = compound[len(userstart):]

                        if len(word) == gap_count:
                            candidates1.append(word)

            for word in candidates1:

                compound1 = (userstart + word).lower()

                if compound1 in german_words:
                    candidates2.append(word)

            print(f"\n\033[1;4m{z}. \"{userstart.capitalize()}\" & \"{userend.capitalize()}\":\033[0m")

            i = 0
            for word in candidates2:

                compound2 = (word + userend).lower()

                if compound2 in german_words:
                    i += 1
                    print(word.capitalize())

            print("Number of solutions:", i)
            if i == 0 and candidates2 != []:
                print(f"Here are the most likely words that could potentially make a compound with the words \"{userstart.capitalize()}\" and \"{userend.capitalize()}\" but are not found in the dicitonary used: ")
                for w in sorted(candidates2):
                    print(f"{userstart.capitalize()} - {w.capitalize()} - {userend.capitalize()}")

    sys.exit()


except (KeyboardInterrupt, SystemError):
    sys.exit()
