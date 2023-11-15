def print_unique_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()  
            words = content.split()

            unique_words = sorted(set(words))

            print("Unique words in alphabetical order:")
            for word in unique_words:
                print(word)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

print_unique_words('c:\\pavan:\\document.txt')
