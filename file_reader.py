# Reading line-by-line using 'with' (highly efficient for large files)
with open("training_notes.txt", "r") as file:
    print("--- Reading Line by Line ---")
    for line in file:
        # strip() removes extra blank lines from the file's '\n' characters
        print(line.strip()) 
