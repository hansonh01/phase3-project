from helpers import intro, show_menu, exit_program, find_item_by_ID, find_item_by_name, update_order, delete_order, view_order_history

def main():
    user = intro()
    while True:
        menu()
        choice = int(input("> "))
        if choice == 1:
            exit_program()
        elif choice == 2:
            show_menu(user)
        elif choice == 3:
            find_item_by_ID()
        elif choice == 4:
            find_item_by_name()
        elif choice == 5:
            update_order(user)
        elif choice == 6:
            delete_order(user)
        elif choice == 7:
            view_order_history(user)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("1. Exit the program")
    print("2. Place an Order")
    print("3. Find Item by ID")
    print("4. Find Item by Name")
    print("5. Update Existing Order")
    print("6. Delete Existing Order")
    print("7. View Order History")

if __name__ == '__main__':
    main()