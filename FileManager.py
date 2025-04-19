def modify_content(content):
    return content.upper()  # Convert every letter to uppercase

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file: # Attempt to open the provided filename
            content = file.read()

        modified = modify_content(content)

        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified)

        print(f"File successfully modified and saved as: {new_filename}")

    except FileNotFoundError:    # Notify the user that the file has not been found
        print(f"The file '{filename}' does not exist.")
    except PermissionError: # Notify the user of a permission error
        print(f"You don't have permission to read '{filename}'.")
    except Exception as e: # Notify the of any error encountered
        print(f"❌ Unexpected error: {e}")


main()
