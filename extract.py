# Prompt the user for the keyword
keyword = input("Enter the keyword to search for: ")

# Read the content of data.txt
with open('file_handlingtask/data.txt', 'r') as infile:
    lines = infile.readlines()

# Filter lines that contain the keyword
filtered_lines = [line for line in lines if keyword in line]

# Write the filtered lines to filtered_data.txt
with open('file_handlingtask/filtered_data.txt', 'w') as outfile:
    outfile.writelines(filtered_lines)

# Open and print the content of filtered_data.txt to verify
with open('file_handlingtask/filtered_data.txt', 'r') as outfile:
    print(outfile.read())
