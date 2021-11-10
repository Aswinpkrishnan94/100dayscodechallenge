PLACE_HOLDER = "[name]"
with open("./input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter.replace(PLACE_HOLDER, strip_name)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", "w") as completed_letter:
            completed_letter.write( new_letter)