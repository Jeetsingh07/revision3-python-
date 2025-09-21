def print_numbers():
    for num in range(1, 101):
        print(num)
        user_input = input("Press 'q' to quit or Enter to continue: ")
        if user_input.lower() == 'q':
            print("Loop terminated by the user.")
            break

# Call the function
print_numbers()
