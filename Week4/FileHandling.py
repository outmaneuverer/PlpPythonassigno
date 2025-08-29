def modify_content(text):
    return text.upper()


try:
    # user input filename
    input_filename = input("Enter the filename to read: ")

    # Open file in read mode
    with open(input_filename, "r") as infile:
        content = infile.read()

    # Modification the content
    modified_content = modify_content(content)

    # new output filename
    output_filename = "modified_" + input_filename

    # modified content into new file
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"File processed successfully! Modified file saved as: {output_filename}")

# error handling
except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
