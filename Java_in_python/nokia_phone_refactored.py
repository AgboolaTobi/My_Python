def menu():
    user_menu = input("""
    ===List of Menu Functions===
    1. Phone book
    2. Message
    3. Chat
    4. Call register
    5. Tones
    6. Settings
    7. Call divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM Services
    """)
    if user_menu == "1":
        phone_book()
    elif user_menu == "2":
        message()
    elif user_menu == "3":
        chat()
    elif user_menu == "4":
        call_register()
    elif user_menu == "5":
        tones()
    elif user_menu == "6":
        setting()
    elif user_menu == "7":
        divert()
    elif user_menu == "8":
        games()
    elif user_menu == "9":
        calculator()
    elif user_menu == "10":
        reminders()
    elif user_menu == "11":
        clock()
    elif user_menu == "12":
        profiles()
    elif user_menu == "13":
        sim_services()
    else:
        menu()


def phone_book():
    input("""
    ===PHONEBOOK===
    1. Search
    2. Service Nos
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b'card
    8. Options
    9. Speed dials
    10. Voice tags
    11. Go back to phonebook
    12. Go back to main menu
    """)
    phonebook_selection = input("Select an option: ")
    if phonebook_selection == "1":
        print("search")
    elif phonebook_selection == "2":
        print("Service Nos")
    elif phonebook_selection == "3":
        print("Add name")
    elif phonebook_selection == "4":
        print("Erase")
    elif phonebook_selection == "5":
        print("Edit")
    elif phonebook_selection == "6":
        print("Assign tone")
    elif phonebook_selection == "7":
        print("Send b' card")
    elif phonebook_selection == "8":
        print("""
        Options
        1-> Type of view
        2-> Memory status
        3-> Go back to previous menu
        4 -> Exit
        """)
        options_selection = input("Select an option: ")
        if options_selection == "1":
            print("Type of view")
        elif options_selection == "2":
            print("Memory status")
        elif options_selection == "3":
            phone_book()
        elif options_selection == "4":
            menu()
        else:
            phone_book()
    elif phonebook_selection == "9":
        print("Speed dials")
    elif phonebook_selection == "10":
        print("Voice tags")
    elif phonebook_selection == "11":
        phone_book()
    elif phonebook_selection == "12":
        menu()
    else:
        phone_book()


def message():
    print("""
    == MESSAGES ==
    1. Write messages
    2. Inbox
    3. Outbox
    4. Picture messages
    5. Templates
    6. Smileys
    7. Message settings
    8. Info service
    9. Voice mailbox number
    10. Service command editor
    11. Go back to main menu
    """)
    message_selection = input("Select an option: ")
    if message_selection == "1":
        print("Write message")
    elif message_selection == "2":
        print("Inbox")
    elif message_selection == "3":
        print("Outbox")
    elif message_selection == "4":
        print("Picture messages")
    elif message_selection == "5":
        print("Templates")
    elif message_selection == "6":
        print("Smileys")
    elif message_selection == "7":
        print("""
        Message setting
        1->Set
        2->Common
        3->Go back
        4->main menu
        """)
        message_setting_selection = input("Select an option: ")
        if message_setting_selection == "1":
            print("""
            Set
            1. Message center Number
            2. Message sent as
            3. Message validity
            4. Go back
            5. Go to main menu
            """)
            set_selection = input("Select an option: ")
            if set_selection == "1":
                print("Message center Number")
            elif set_selection == "2":
                print("Message sent as")
            elif set_selection == "3":
                print("Message validity")
            elif set_selection == "4":
                message()
            elif set_selection == "5":
                menu()
        elif message_setting_selection == "2":
            print("""
            =-=Common=-=
            1.Delivery Report
            2.Reply Via Same Center
            3.Character support
            4.Go back message
            5.Go back main menu""")
            common_selection = input("Select an option: ")
            if common_selection == "1":
                print("Delivery Reports")
            elif common_selection == "2":
                print("Reply Via Same Center")
            elif common_selection == "3":
                print("Character support")
            elif common_selection == "4":
                message()
            elif common_selection == "5":
                menu()

    elif message_selection == "8":
        print("Info services")
    elif message_selection == "9":
        print("Voice mailbox number")
    elif message_selection == "10":
        print("Service command editor")
    elif message_selection == "11":
        message()
    else:
        message()


def chat():
    print(""""
    Chat
    1. Chat
    2. Go back to main menu
    """)
    chat_selection = input("Select an option: ")
    if chat_selection == "1":
        print("Chat")
    elif chat_selection == "2":
        menu()


def call_register():
    print(""""
    ==Call register
    1. Missed call
    2. Received call
    3. Dialled Numbers
    4. Erase recent call list
    5. Show Call Duration
    6. Show call Costs
    7. Call Cost Setting
    8. Prepaid Credit
    9. Go to main menu
    """)
    call_register_selection = input("Select an option: ")
    if call_register_selection == "1":
        print("Missed call")
    elif call_register_selection == "2":
        print("Received call")
    elif call_register_selection == "3":
        print("Dialled numbers")
    elif call_register_selection == "4":
        print("Erase recent call list")
    elif call_register_selection == "5":
        print("""
        Show Call Duration
        1. Last Call Duration
        2. All Call's Duration
        3. Receive Call's Duration
        4. Dialled Call Duration
        5. Clear Timers
        6. Go back to call register
        7. Go back to main menu""")
        show_call_duration_selection = input("Select an option: ")
        if show_call_duration_selection == "1":
            print("Last Call Duration")
        elif show_call_duration_selection == "2":
            print("All Call's Duration")
        elif show_call_duration_selection == "3":
            print("Receive Call's Duration")
        elif show_call_duration_selection == "4":
            print("Dialled Call Duration")
        elif show_call_duration_selection == "5":
            print("Clear Timers")
        elif show_call_duration_selection == "6":
            call_register()
        elif show_call_duration_selection == "7":
            menu()
    elif call_register_selection == "6":
        print("""
        Show call Costs
        1. Last Call Cost
        2. All Call Cost
        3. Clear Counters
        4. Back to call register
        5. Go back to main menu
        """)
        show_call_cost_selection = input("Select an option: ")
        if show_call_cost_selection == "1":
            print("Last Call Cost")
        elif show_call_cost_selection == "2":
            print("All Call Cost")
        elif show_call_cost_selection == "3":
            print("Clear Counters")
        elif show_call_cost_selection == "4":
            call_register()
        elif show_call_cost_selection == "5":
            menu()
    elif call_register_selection == "7":
        print("""
        Call Cost Setting
        1. Call Cost Limit
        2. Call Cost Limit
        3. Go back to call register
        4. Go back to main menu
        """)
        call_cost_setting_selection = input("Select an option: ")
        if call_cost_setting_selection == "1":
            print("Call Cost Limit")
        elif call_cost_setting_selection == "2":
            print("Call Cost Limit")
        elif call_cost_setting_selection == "3":
            call_register()
        elif call_register_selection == "4":
            menu()
    elif call_register_selection == "8":
        print("Prepaid Credit")
    elif call_register_selection == "9":
        menu()
    else:
        menu()


def tones():
    print("""
    ==TONES==
    1. Ringing tone
    2. Ringing volume
    3. Incoming call alert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. Warning tones
    8. Vibrating alert
    9. Screen saver
    10. Main Menu
    """)
    tones_selection = input("Select an option: ")
    if tones_selection == "1":
        print("Ringing tone")
    elif tones_selection == "2":
        print("Ringing volume")
    elif tones_selection == "3":
        print("Incoming call alert")
    elif tones_selection == "4":
        print("Composer")
    elif tones_selection == "5":
        print("Message alert tone")
    elif tones_selection == "6":
        print("Keypad tones")
    elif tones_selection == "7":
        print("Warning tones")
    elif tones_selection == "8":
        print("Vibrating alert")
    elif tones_selection == "9":
        print("Screen saver")
    elif tones_selection == "10":
        menu()
    else:
        tones()


def setting():
    print("""
    ==== Setting ====
    1-> Call settings
    2-> Phone settings
    3-> Security settings
    4-> Restore factory setting
    5. Main Menu
    """)
    setting_selection = input("Select an option: ")
    if setting_selection == "1":
        print("""
        Call setting
        1. Automatic Redial
        2. Speed Dialing
        3. Call Waiting Option
        4. Own Number Sending
        5. Phone line in use
        6. Automatic Answer
        7. Go back to settings
        8. Go back to main menu
        """)
        call_setting_selection = input("Select an option: ")
        if call_setting_selection == "1":
            print("Automatic Redial")
        elif call_setting_selection == "2":
            print("Speed Dialing")
        elif call_setting_selection == "3":
            print("Call Waiting Option")
        elif call_setting_selection == "4":
            print("Own Number Sending")
        elif call_setting_selection == "5":
            print("Phone line in use")
        elif call_setting_selection == "6":
            print("Automatic Answer")
        elif call_setting_selection == "7":
            setting()
        elif call_setting_selection == "8":
            menu()
    elif setting_selection == "2":
        print(""""
        Phone settings
        1. Language
        2. Cell info display
        3. Welcome note
        4. Network selection
        5. Lights
        6. Confirm sim service action
        7. Go back to Setting
        8. Go Back to Main Menu
        """)
        phone_setting_selection = input("Select an option: ")
        if phone_setting_selection == "1":
            print("Language")
        elif phone_setting_selection == "2":
            print("Cell info display")
        elif phone_setting_selection == "3":
            print("Welcome note")
        elif phone_setting_selection == "4":
            print("Network selection")
        elif phone_setting_selection == "5":
            print("Lights")
        elif phone_setting_selection == "6":
            print("Confirm sim service action")
        elif phone_setting_selection == "7":
            setting()
        elif phone_setting_selection == "8":
            menu()
    elif setting_selection == "3":
        print("""
        Security settings
        1. Pin code request
        2. Call barring service
        3. Fixed dialling
        4. Closed user group
        5. Phone security
        6. Change access code
        7. Go back to Setting
        8. Go back to Main Menu
        """)
        security_setting_selection = input("Select an option: ")
        if security_setting_selection == "1":
            print("Pin code request")
        elif security_setting_selection == "2":
            print("Call barring service")
        elif security_setting_selection == "3":
            print("Fixed dialling")
        elif security_setting_selection == "4":
            print("Closed user group")
        elif security_setting_selection == "5":
            print("Phone security")
        elif security_setting_selection == "6":
            print("Change access code")
        elif security_setting_selection == "7":
            setting()
        elif security_setting_selection == "8":
            menu()
    elif setting_selection == "4":
        print("""
        Restore factory settings
        1-> Restore factory settings
        2-> Go back to Setting
        3-> Go back to main menu
        """)
        restore_selection = input("Select an option: ")
        if restore_selection == "1":
            print("Restore factory settings")
        elif restore_selection == "2":
            setting()
        elif restore_selection == "3":
            menu()
    elif setting_selection == "5":
        menu()
    else:
        setting()


def divert():
    print("""
    Call divert
    1->Call divert
    2-> Go back to main menu
    """)
    call_divert_selection = input("Select an option: ")
    if call_divert_selection == "1":
        print("Call divert")
    elif call_divert_selection == "2":
        menu()
    else:
        divert()


def games():
    print("""
    Games
    1-> Games
    2-> Go back to main menu
    """)
    games_selection = input("Select an option: ")
    if games_selection == "1":
        print("Games")
    elif games_selection == "2":
        menu()
    else:
        games()


def addition(number1, number2):
    result = number1 + number2
    return result


def subtraction(number1, number2):
    result = number1 - number2
    return result


def multiplication(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def division(number1, number2):
    return number1 / number2 or number2 / number1


def square(number):
    return number * number


def square_root(number):
    if number != 0:
        return number / number ** (1 / 2)
    else:
        return 0


def calculator():
    print("""
    Calculator
    1. Addition
    2 Subtraction
    3. Multiplication
    4. Division
    5. Square
    6. Square_root
    7. Go back to main menu
    """)
    calculator_selection = input("Select an option: ")

    if calculator_selection == "1":
        number1 = int(input("Enter number: "))
        number2 = int(input("Enter number: "))
        print(number1, " + ", number2, " = ", addition(number1, number2))
        calculator()
    elif calculator_selection == "2":
        number1 = int(input("Enter number: "))
        number2 = int(input("Enter number: "))
        print(number1, " - ", number2, " = ", subtraction(number1, number2))
        calculator()
    elif calculator_selection == "3":
        number1 = int(input("Enter number: "))
        number2 = int(input("Enter number: "))
        print(number1, " multiplied by ", number2, " = ", multiplication(number1, number2))
        calculator()
    elif calculator_selection == "4":
        number1 = int(input("Enter number: "))
        number2 = int(input("Enter number: "))
        print(number1, " divided by ", number2, " = ", division(number1, number2))
        calculator()
    elif calculator_selection == "5":
        number = int(input("Enter number: "))
        print(number, " squared ", " = ", square(number))
        calculator()

    elif calculator_selection == "6":
        number = int(input("Enter number: "))
        print(square_root(number))
        calculator()
    elif calculator_selection == "7":
        menu()
    else:
        calculator()


def reminders():
    print("""
    Reminders
    1-> Reminders
    2-> Go back to main menu
    """)
    reminders_selection = input("Select an option: ")
    if reminders_selection == "1":
        print("Reminders")
    elif reminders_selection == "2":
        menu()
    else:
        reminders()


def clock():
    print(""""
    Clock
    1. Alarm Clock
    2. Clock Settings
    3. Date Setting
    4. Stop Watch
    5. CountDown timer
    6. Auto Update Of Date And Time
    7. Main Menu
    """)
    clock_selection = input("Select an option: ")
    if clock_selection == "1":
        print("Alarm Clock")
    elif clock_selection == "2":
        print("Clock Settings")
    elif clock_selection == "3":
        print("Date Setting")
    elif clock_selection == "4":
        print("Stop Watch")
    elif clock_selection == "5":
        print("CountDown timer")
    elif clock_selection == "6":
        print("Auto Update Of Date And Time")
    elif clock_selection == "7":
        menu()
    else:
        clock_selection


def profiles():
    print("""
    Profiles
    1-> Profiles
    2-> Go back to main menu
    """)
    profiles_selection = input("Select an option: ")
    if profiles_selection == "1":
        print("Profiles")
    elif profiles_selection == "2":
        menu()
    else:
        profiles()


def sim_services():
    print("""
    SIM Services
    1->SIM Services
    2. Go back to main menu
    """)
    sim_selection = input("Select an option: ")
    if sim_selection == "1":
        print("SIM Services")
    elif sim_selection == "2":
        menu()
    else:
        sim_services()


if __name__ == "__main__":
    menu()
