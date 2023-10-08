def nokia_function():
    print("""===list of menu function===
    1. Phone book
    2. Messages
    3. Chat
    4. Call Register
    5. Tones
    6. Settings
    7. Call Divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM services
    """)
    response = int(input("Enter options:"))
    if response == 1:
        print("""==Phonebook==
        1. Search
        2. Service Nos. 1
        3. Add name
        4. Erase
        5. Edit
        6. Assign tone
        7. Send b’card
        8. Options
        9. Speed dials
        10. Voice tags 
        11. Go back to main menu""")
        phonebook_response = int(input("Enter options"))
        if phonebook_response == 1:
            print("search")
        elif phonebook_response == 2:
            print("service Nos. 1")
        elif phonebook_response == 3:
            print("Add name")
        elif phonebook_response == 4:
            print("Erase")
        elif phonebook_response == 5:
            print("Edit")
        elif phonebook_response == 6:
            print("Assign tone")
        elif phonebook_response == 7:
            print("Send b'card ")
        elif phonebook_response == 8:
            print("""option
            1.Type of view 
            2.Memory status
            3. Go back to previous menu
            4 .Exit
            """)
            option_response = int(input("Enter option:"))
            if option_response == 1:
                print("Type of view")
            elif option_response == 2:
                print("Memory status")
            elif option_response == 3:
                print("option")
            elif option_response == 4:
                nokia_function()
        elif phonebook_response == 9:
            print("Speed dials")
        elif phonebook_response == 10:
            print("Voice tags")
        elif phonebook_response == 11:
            nokia_function()
    elif response == 2:
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
        11. Go back to main menu""")
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
                4. Go back to main menu""")
                set_selection = input("Select an option: ")
                if set_selection == "1":
                    print("Message center Number")
                elif set_selection == "2":
                    print("Message sent as")
                elif set_selection == "3":
                    print("Message validity")
                elif set_selection == "4":
                    nokia_function()
            elif message_setting_selection == "2":
                print("""
                =-=Common=-=
                 1.Delivery Report
                 2.Reply Via Same Center
                 3.Character support
                 4.Go back main menu""")
                common_selection = input("Select an option: ")
                if common_selection == "1":
                    print("Delivery Reports")
                elif common_selection == "2":
                    print("Reply Via Same Center")
                elif common_selection == "3":
                    print("Character support")
                elif common_selection == "4":
                    nokia_function()
        elif message_selection == "8":
            print("Info services")
        elif message_selection == "9":
            print("Voice mailbox number")
        elif message_selection == "10":
            print("Service command editor")
        elif message_selection == "11":
            nokia_function()
    elif response == 3:
        print("""
        chat
        1. Chat
        2.Go back to menu""")
    chat_response = input("Enter Option:")
    if chat_response == 1:
        print("Chat")
    elif chat_response == 2:
        nokia_function()
    elif response == 4:
        print("""===Call register===
        1. Missed calls
        2. Received calls
        3. Dialled numbers
        4. Erase recent call lists
        5. Show call duration
        6.Show call costs
        7.Call cost settings
        8.prepaid credit
        9. go back to main menu
        """)
        callregister_response = int(input("Enter options"))
        if callregister_response == 1:
            print("Missed calls")
        elif callregister_response == 2:
            print("Received calls")
        elif callregister_response == 3:
            print("Dialled numbers")
        elif callregister_response == 4:
            print("Erase recent call lists")
        elif callregister_response == 5:
            print("""Show Call Duration
            1. Last call duration
            2. All calls’ duration
            3. Received calls’ duration
            4. Dialled calls’ duration
            5. Clear timers 
            6.Go back to Show call duration
            7.Go back to menu
            """)
            show_call_duration_response = input("Enter option:")
            if show_call_duration_response == 1:
                print("Last call duration")
            elif show_call_duration_response == 2:
                print("All calls’ duration")
            elif show_call_duration_response == 3:
                print("Received calls’ duration")
            elif show_call_duration_response == 4:
                print("Dialled calls’ duration")
            elif show_call_duration_response == 5:
                print("Clear timers ")
            elif show_call_duration_response == 6:
                print("Show call duration")
            elif show_call_duration_response == 7:
                nokia_function()
        elif callregister_response == 6:
            print("""Show call cost
            1. Last call cost
            2. All calls’ cost
            3. Clear counters 
            4. Go back to show call cost
            5. Go back menu
            """)
            show_call_cost_response = input("enter option:")
            if show_call_cost_response == 1:
                print("Last call cost")
            elif show_call_cost_response == 2:
                print("All calls’ cost")
            elif show_call_cost_response == 3:
                print("Clear counters ")
            elif show_call_cost_response == 4:
                print("show call cost")
            elif show_call_cost_response == 5:
                nokia_function()
        elif callregister_response == 7:
            print("""
            Call cost settings
            1. Call cost limit
            2. Show costs in
            3.go back to call cost settings
            4.menu
            """)
            call_cost_settings_response = input("enter option")
            if call_cost_settings_response == 1:
                print("Call cost limit")
            elif call_cost_settings_response == 2:
                print("Show costs in")
            elif call_cost_settings_response == 3:
                print("call cost settings")
            elif call_cost_settings_response == 4:
                nokia_function()
        elif callregister_response == 8:
            print("prepaid credit")
    elif response == 5:
        print("""===Tones===
        1. Ringing tone
        2. Ringing volume
        3. Incoming call alert
        4. Composer
        5. Message alert tone
        6. Keypad tones
        7. Warning and game tones
        8. Vibrating alert
        9. Screen saver
        """)
        tones_response = int(input("Enter options"))
        if tones_response == 1:
            print("Ringing tone")
        elif tones_response == 2:
            print("Ringing volume")
        elif tones_response == 3:
            print("Incoming call alert")
        elif tones_response == 4:
            print("Composer")
        elif tones_response == 5:
            print("Message alert tone")
        elif tones_response == 6:
            print("Keypad tones")
        elif tones_response == 7:
            print("Warning and game tones")
        elif tones_response == 8:
            print("Vibrating alert")
        elif tones_response == 9:
            print("Screen saver")
    elif response == 6:
        print("""===settings===
        1.Call settings
        2.Phone settings
        3.Security settings
        4.Restore factory settings
        """)
        settings_response = input("Enter options")
        if settings_response == 1:
            print("""Call settings
            1. Automatic redial
            2. Speed dialling
            3. Call waiting options
            4. Own number sending
            5. Phone line in use
            6. Automatic answer 
            7. Go back to call settings
            8. Go to menu
            """)
            call_settings_response = input("Enter options")
            if call_settings_response == 1:
                print("Automatic redial")
            elif call_settings_response == 2:
                print("Speed dialling")
            elif call_settings_response == 3:
                print("Call waiting options")
            elif call_settings_response == 4:
                print("Own number sending")
            elif call_settings_response == 5:
                print(" Phone line in use")
            elif call_settings_response == 6:
                print("Automatic answer ")
            elif call_settings_response == 7:
                print("call settings")
            elif call_settings_response == 8:
                nokia_function()
        elif settings_response == 2:
            print("""Phone settings
            1. Language
            2. Cell info display
            3. Welcome note
            4. Network selection
            5. Lights2
            6. Confirm SIM service actions
            7. go back phone settings
            8. go to menu
            """)
            phone_settings_response = input("enter option:")
            if phone_settings_response == 1:
                print("language")
            elif phone_settings_response == 2:
                print("Cell info display")
            elif phone_settings_response == 3:
                print("Welcome note")
            elif phone_settings_response == 4:
                print("Network selection")
            elif phone_settings_response == 5:
                print("Lights2")
            elif phone_settings_response == 6:
                print("Confirm SIM service actions")
            elif phone_settings_response == 7:
                print("phone settings")
            elif phone_settings_response == 8:
                nokia_function()

        elif settings_response == 3:
            print("""
            Security settings
            1. PIN code request
            2. Call barring service
            3. Fixed dialling
            4. Closed user group
            5. Phone security
            6. Change access codes
            7. Go back to security settings
            8.Go to menu 
            """)
            security_settings_response = input("Enter option:")
            if security_settings_response == 1:
                print("PIN code request")
            elif security_settings_response == 2:
                print("Call barring service")
            elif security_settings_response == 3:
                print("Fixed dialling")
            elif security_settings_response == 4:
                print("Closed user group")
            elif security_settings_response == 5:
                print("Phone security")
            elif security_settings_response == 6:
                print("Change access codes")
            elif security_settings_response == 7:
                print("security settings")
            elif security_settings_response == 8:
                nokia_function()
        elif settings_response == 4:
            print("Restore factory settings")

    elif response == 7:
        print("""Call divert
        1. Call divert
        2.Go back to menu""")
        call_divert_response = input("Enter Option:")
        if call_divert_response == 1:
            print("Call divert")
        elif call_divert_response == 2:
            nokia_function()
    elif response == 8:
        print("""Games
        1. Games
        2.Go back to menu""")
        games_response = input("Enter Option:")
        if games_response == 1:
            print("Games")
        elif games_response == 2:
            nokia_function()

    elif response == 9:
        print("""calculator
        1. calculator
        2.Go back to menu""")
        calculator_response = input("Enter Option:")
        if calculator_response == 1:
            print("calculator")
        elif calculator_response == 2:
            nokia_function()

    elif response == 10:
        print("""reminder
        1. reminder
        2.Go back to menu""")
        reminder_response = input("Enter Option:")
        if reminder_response == 1:
            print("reminder")
        elif reminder_response == 2:
            nokia_function()

    elif response == 11:
        print("""===Clock===
        1. Alarm clock
        2. Clock settings
        3. Date setting
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        """)
        clock_response = int(input("Enter options"))
        if clock_response == 1:
            print("Alarm clock")
        elif clock_response == 2:
            print("Clock settings")
        elif clock_response == 3:
            print("Date setting")
        elif clock_response == 4:
            print("Stopwatch")
        elif clock_response == 5:
            print("Countdown timer")
        elif clock_response == 6:
            print("Auto update of date and time")
    elif response == 12:
        print("Profiles")
    elif response == 13:
        print("Sim services")


nokia_function()
