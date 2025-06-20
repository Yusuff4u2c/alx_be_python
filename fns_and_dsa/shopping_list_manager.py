def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []
    print("DEBUG:", shopping_list)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\nShopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print(f"Your shopping list is empty.")

        elif choice == '4':
            print(f"Goodbye!")
            break

        else:
            print(f"Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
