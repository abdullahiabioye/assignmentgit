item = input("Enter your shopping list: ")

#appending user inputs
with open('file_handlingtask/shopping_list.txt', 'a') as file:
    file.write(f"\n{item}")

#reading the entire list
with open('file_handlingtask/shopping_list.txt', 'r') as file:
    content = file.read()
    print(content)