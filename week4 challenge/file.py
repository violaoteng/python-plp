
filename = input("Enter the filename: ")

try:
    
    with open(filename, "r") as file:
        content = file.read()

    # Count words
    word_count = len(content.split())

    
    uppercase_content = content.upper()

    
    output_file = "output.txt"

    
    with open(output_file, "w") as file1:
        file1.write(content + "\n")
        file1.write(uppercase_content + "\n\n")
        file1.write(f"Word Count: {word_count}\n")

    print(f"File processed successfully! Output saved as {output_file}")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
