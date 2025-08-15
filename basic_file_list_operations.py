#reverse-file-content
def reverse_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        with open(filename, 'w') as file:
            file.write(content[::-1])

        print(f"Content of '{filename}' has been reversed and saved back to the file.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

filename = "USA.txt"
reverse_file_content(filename)


#Number-of-lines
def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count

    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."

filename = "USA.txt"
result = count_lines_in_file(filename)

if isinstance(result, int):
    print(f"The file '{filename}' contains {result} lines.")
else:
    print(result)


#reads content from a file
def print_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

filename = "USA.txt"  # Replace with the name of  file
print_file_content(filename)


#element at the specified index
def get_element_by_index(lst, index):
    try:
        if not isinstance(index, int):
            raise ValueError("Invalid input: Index must be an integer.")
        # Check if the index is within the valid range
        if 0 <= index < len(lst):
            return lst[index]
        else:
            raise IndexError("Index is out of range.")

    except ValueError as ve:
        return str(ve)

    except IndexError as ie:
        return str(ie)

my_list = [1, 2, 3, 4, 5, 6, 7]

try:
    index = int(input("Enter an index: "))
    result = get_element_by_index(my_list, index)
    print(result)
except ValueError:
    print("Invalid input: Index must be an integer.")


