# Open the input file and read lines
with open('file_handlingtask/lines.txt', 'r') as infile:
    lines = infile.readlines()

# Reverse each line's content
reversed_lines = [line.strip()[::-1] for line in lines]

# Write the reversed lines to the output file
with open('file_handlingtask/reversed_lines.txt', 'w') as outfile:
    outfile.write('\n'.join(reversed_lines))

# Open and print the content of reversed_lines.txt to verify
with open('file_handlingtask/reversed_lines.txt', 'r') as outfile:
    print(outfile.read())
