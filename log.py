# Open the file in write mode
with open('file_handlingtask/user_input.log', 'w') as file:
    while True:
        # Prompt the user for input
        user_input = input("Enter something (type 'STOP' to end): ")

        # Check for the stop condition
        if user_input == "STOP":
            break

        # Write the user input to the file
        file.write(user_input + '\n')

# Open the file in read mode and print its contents line by line
with open('file_handlingtask/user_input.log', 'r') as file:
    print("\nContents of 'user_input.log':")
    for line in file:
        print(line, end='')
