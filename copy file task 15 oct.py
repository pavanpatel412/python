def main():
    input_file_name = input("enter the name:")
    output_file_name = input("enter the name:")
    try:
        with open(input_file_name, "r") as input_file:
            file_content = input_file.read()
        with open(output_file_name, "w") as output_file:
            output_file.write(file_content)
        print(f"content capital from{input_file_name} to {output_file_name } successfully.")
    except FileNotFoundError:
        with open(output_file_name,"w+") as output_file:
            output_file.write(file_content)
    except Exception as e:
        print("en error accured:",e)
main()