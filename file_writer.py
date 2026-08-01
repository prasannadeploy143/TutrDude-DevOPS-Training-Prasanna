# The 'with' statement handles opening and closing automatically
with open("training_notes.txt", "w") as file:
    file.write("Line 1: Learning Python on AWS.\n")
    file.write("Line 2: Tutedude is Best Platform to Learn.\n")
    file.write("Line 3: My Goal is to be a Successful Devops Engineer in Market.\n")
print("File written successfully using the professional method!")
