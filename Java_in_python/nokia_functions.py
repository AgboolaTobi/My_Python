

def phoneBook():
    print("""
           ===PHONEBOOK===
           1. Search
           2. Service Nos
           3.Add name
           4. Erase
           5. Edit
           6. Assign tone
           7. Send b'card
           8. Options
           9. Speed dials
           10. Voice tags
           11. Go back to main menu
           """)
    phonebook_selection = int(input("Select an option: "))
    if phonebook_selection == 1:
        print("search")
    elif phonebook_selection == 2:
        print("Service Nos")
    elif phonebook_selection == 3:
        print("Add name")
    elif phonebook_selection == 4:
        print("Erase")
    elif phonebook_selection == 5:
        print("Edit")
    elif phonebook_selection == 6:
        print("Assign tone")
    elif phonebook_selection == 7:
        print("Send b'card")
    elif phonebook_selection == 8:
        print("""
               Options
               1-> Type of view
               2-> Memory status
               3.-> Go back phoneBook
               """)
        options_selection = int(input("Select an option: "))
        if options_selection == 1:
            print("Type of view")
        elif options_selection == 2:
            print("Memory status")
        elif options_selection == 3:
            phoneBook()
    elif phonebook_selection == 9:
        print("Speed dials")
    elif phonebook_selection == 10:
        print("Voice tags")
    elif phonebook_selection == 11:
        pass
