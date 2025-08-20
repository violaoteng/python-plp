file = open( "week4 challenge/input.txt", "r")
content = file.read()

#split content by whitespaces 
word_count = len(content.split())

uppercase_content = content.upper()



with open("week4 challenge/output.txt", "w") as file1:
    file1.write("Processed Text:\n")
    file1.write(uppercase_content + "\n\n")
    file1.write(f"Word Count: {word_count}\n")

    print("File written successfully.")    
    


