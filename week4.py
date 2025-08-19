# Read the file
with open("input.txt", "r") as file:
    content = file.read()

# Modify the content (example: make it uppercase)
modified_content = content.upper()

# Write the modified version to a new file
with open("modified_input.txt", "w") as file:
    file.write(modified_content)

print("Modified file created successfully!")

try:
    filename = input("Enter the filename: ")
    with open(filename, "r") as file:
        data = file.read()
    print("File read successfully!")
    print(data)

except FileNotFoundError:
    print("File not found. Please check the filename.")

except PermissionError:
    print("You don’t have permission to read this file.")
