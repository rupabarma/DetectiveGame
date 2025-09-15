import time
import sys


def slow_print(text, delay = 0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def intro():
    slow_print("🕵️ Welcome, Detective!")
    slow_print("You’ve been called to investigate a murder at the Ravenwood Mansion.")
    slow_print("The victim: Mr. Archibald Crane, a wealthy recluse.")
    slow_print("Three suspects are present in the mansion.")
    slow_print("Your job: find out who did it, how, and why.\n")

def investigate_scene():
    slow_print("You enter the study where Mr. Crane was found dead.")
    slow_print("There is a broken vase, a torn piece of cloth, and a faint smell of perfume.")

    clues = []
    while True:
        print("\nWhat would you like to examine?")
        print("1: The broken vase")
        print("2. The torn cloth")
        print("3. The smell of perfume")
        print("4. Finish investigation")

        choice = input("> ")

        if (choice == "1" and "vase" not in clues):
            print("The vase seems to have been broken during a struggle.")
            clues.append("vase")
        elif (choice == "2" and "cloth" not in clues):
            print("The cloth is from a fancy dress — maybe from a woman’s gown?")
            clues.append("cloth")
        elif (choice == "3" and "perfume" not in clues):
            print("The perfume smells expensive. Possibly Miss Scarlet’s?")
            clues.append("perfume")
        elif (choice == "4") :
            break
        else:
            slow_print("You already checked that or made an invalid choice.")

    return clues

def interview_suspects():
    suspects = {
        "Miss Scarlet": {
            "alibi": "I was in the garden reading. I didn’t hear anything.",
            "motive": "He promised to fund my fashion line, then backed out.",
        },
        "Colonel Mustard": {
            "alibi": "I was polishing my antique guns in the trophy room.",
            "motive": "He accused me of stealing from the war collection!",
        },
        "Professor Plum": {
            "alibi": "I was in the library, working on my novel.",
            "motive": "He claimed I plagiarized my last book. Outrageous!",
        }
    }

    interviewed = set()
    while len(interviewed) < 3:
        print("\nWho would you like to interview?")
        for name in suspects:
            if name not in interviewed:
                print(f"- {name}")
        choice = input("> ").title()

        if (choice in suspects and choice not in interviewed):
            slow_print(f"\nInterviewing {choice}....")
            slow_print(f"Alibi : {suspects[choice]["alibi"]}....")
            slow_print(f"Motive : {suspects[choice]["motive"]}....")
            interviewed.add(choice)
        else:
            slow_print("Invalide or already interviewed.")

    return suspects

def make_accusation(suspects):
    print("\nTime to make your accusation.")
    print("Who do you think did it?")
    for name in suspects:
        print(f"- {name}")
    accused = input("> ").title()

    if (accused == "Miss Scarlet"):
        slow_print("\nYou accuse Miss Scarlet...")
        slow_print("You mention the perfume and the torn fabric.")
        slow_print("Under pressure, she confesses!")
        slow_print("✅ Case Closed! Well done, Detective.")
    elif (accused in suspects):
        slow_print(f"\nYou accuse {accused}...")
        slow_print("But the evidence doesn’t support your claim.")
        slow_print("❌ Wrong accusation. The killer walks free...")
    else:
        slow_print("That's not a valid suspect.")

def play_game():
    intro()
    clues = investigate_scene()
    suspects = interview_suspects()
    make_accusation(suspects)

if (__name__ == "__main__"):
    play_game()
