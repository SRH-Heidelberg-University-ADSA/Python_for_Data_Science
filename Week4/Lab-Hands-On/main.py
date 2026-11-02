def create_dictionary(**kwargs):
    """
    Create and return a dictionary from keyword arguments.
    """
    return kwargs


def print_dictionary(data):
    """
    Print dictionary details.
    """
    print("The length of the dictionary is:", len(data))
    print("It is a dictionary, see:", type(data))
    print("Let's print the dictionary:")
    for key, value in data.items():
        print(" * key:", key, "==>", "value:", value)
    return data 


def main():
    person = create_dictionary(
        first_name = input("Enter your first name: "),
        last_name = input("Enter your last name: "),
        age = int(input("Enter your age: ")),
        country = input("Enter your country: ")
    )

    print_dictionary(person)
    print("\nSaved dictionary:")
    print(person)


'''__name__ is a special built-in variable.

When the file is run directly, __name__ equals "__main__".

Therefore, main() executes. This is professional Python structure.'''
if __name__ == "__main__":
    main()