# This Python file contains some incomplete and incorrect code.
# Using the comments as a guide, make changes to this script
# until running it provides complete results.

# When you're ready to work on the next exercise, increase this
# number by 1. There are 5 parts total, including a bonus!
parts_to_run = 5

# This is a list of some snack names.
snacks = ["ice cream", "fruit", "cookies", "salad", "falafel"] 
# Part 0: Solve the KeyError by finding and fixing the typo
# in this dictionary's keys.
flavor_levels = {
    "fruit": 100,
    "cookies": 125,
    "salad": 90,
    "ice cream": 200,
    "falafel": 300
}
# Leave this list empty for now.
# In Part 1, you will add some names from the snacks list.
favorites = []

for snack in snacks:
    if snack not in flavor_levels.keys():
        raise KeyError(f"Snack name '{snack}' is not in the flavor dictionary! Is there a typo?")

def Part1():
    print("=== WEEK 3 - PRACTICAL APPLICATION LAB: PART 1 ===")
    print("Define favorite snacks.")
    print()

    # Add some existing snacks to the list of favorites.
    # Hint: Use favorites.append()!
    favorites.append(snacks[0])
    favorites.append(snacks[2])

    if favorites:
        # Change pass into a print statement that will print
        # the length of the favorites list.
        print("There are",len(favorites),  "in the favorites list")
    else: 
        print("There are no snacks in the list of favorites.")
        print("Try adding some with favorites.append()!")

def Part2():
    print("=== WEEK 3 - PRACTICAL APPLICATION LAB: PART 2 ===")
    print("Find which snacks are favorites.")
    print()

    for snack in snacks:
        # This f-string will print the current snack.
        print(f"Considering {snack}...")

        # Change False to a comparison that will be True when the
        # current snack is in the list of favorites.
        if snack in favorites:
            # Change to an f-string and print the name of the snack, too.
            print(f"YUM! {snack}! I love it.")
        else:
            # This is not a favorite snack.
            # Replace "pass" with a print statement to say "No thanks".
            print("NO Thanks!") 

        # Print a newline after each snack, for some breathing room in the output.
        print()

def Part3():
    print("=== WEEK 3 - PRACTICAL APPLICATION LAB: PART 3 ===")
    print("Look up snack names in a dictionary object.")
    print()

    for snack in snacks:
        # Replace 0 with a lookup for this snack in the flavor_levels dictionary.
        # Hint: Use square brackets!
        flavor = flavor_levels.get(snack)

        # Change False to a comparison that will be True when the
        # current snack has a flavor value greater than 100.
        if flavor > 100:
            print(f"{snack} has a flavor value over 100!")
            print()

def Part4():
    print("=== WEEK 3 - PRACTICAL APPLICATION LAB: PART 4 ===")
    print("Find the secret code.")
    print()

    raw_data = [
        "W3820ELL UDZL",
        "DU? UONE!SCH3"
    ]
    for line in raw_data:
        # Reveal the secret message!
        # Use string slicing to print only certain characters from each line:
        # - The FIRST character in the line
        # - The characters from index 5-9
        # Concatenate the two slices together with the + operator.
        print(line[0] + line[5:9], end="")

def Bonus():
    # Sort the snacks by flavor level, and print them in order.
    print("=== WEEK 3 - PRACTICAL APPLICATION LAB: BONUS ===")
    print("Sorting snacks.")
    print()

    def mySortFunction(snack):
        return flavor_levels[snack]

    print("Unsorted:" + str(snacks))
    snacks.sort(key=mySortFunction)
    print("Sorted:" + str(snacks))

# Everything below this point is just for running the correct
# amount of exercises at a time, and can be safely ignored.

all_parts = [Part1, Part2, Part3, Part4, Bonus]
parts_run = 0
max_parts = 5

for part in all_parts:
    print()
    part()
    print()
    parts_run += 1
    if parts_run >= parts_to_run:
        print()
        if parts_to_run == max_parts:
            print(f"All exercises have been run.")
        else:
            print(f"Ran {parts_to_run} exercise(s). Increment parts_to_run to continue.")
        exit()