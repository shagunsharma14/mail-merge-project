with open("Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        striped_name = name.strip("\n")
        new_letter = letter_contents.replace("[name]", striped_name)
        with open(f"Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
