def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        # Add Item
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to your list.")
            else:
                print("⚠️ Item name cannot be empty.")

        # Remove Item
        elif choice == '2':
            if not shopping_list:
                print("🛒 Your list is empty — nothing to remove.")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"❌ '{item}' has been removed.")
                else:
                    print(f"⚠️ '{item}' is not in your list.")

        # View List
        elif choice == '3':
            if not shopping_list:
                print("🛍️ Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")

        # Exit
        elif choice == '4':
            print("Goodbye!")
            break

        # Invalid Option
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
