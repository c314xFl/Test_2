class Program:
    def __init__(self):
        # Imports
        global PrettyTable, Path, os, random, sys, textwrap, time, subprocess, json
        from prettytable import PrettyTable
        from pathlib import Path
        import os, sys, time, subprocess, random, textwrap, json

        # Delays
        self.printing_delay = 0.01 # Default = 0.01
        self.processing_delay = 0.5 # Default 0.5

        # Get the file name, from local file
        self.file_name = Path(__file__).name # Current program file name
        self.about_txt = Path(__file__).parent / "About.txt" # Programm purpose
        self.sources_txt = Path(__file__).parent / "Sources.txt" # Information sources

        # Call class within class, class to other class
        self.alphabetically_sorter = self.AlpahbeticallySorter(self)
        self.anti_alphabetically_sorter = self.AntiAlpahbeticallySorter(self)
        self.random_sorter = self.RandomSorter(self)

    def logo(self):
        self.transition_effect()
        # Use Semantic Versioning
        logo = textwrap.dedent("""
            .d8888b.                   888                                                    
           d88P  Y88b                  888                                                    
           Y88b.                       888                                                    
            "Y888b.    .d88b.  888d888 888888 .d88b.  888d888               88888b.  888  888 
               "Y88b. d88""88b 888P"   888   d8P  Y8b 888P"                 888 "88b 888  888 
                 "888 888  888 888     888   88888888 888                   888  888 888  888 
           Y88b  d88P Y88..88P 888     Y88b. Y8b.     888          d8b      888 d88P Y88b 888 
            "Y8888P"   "Y88P"  888      "Y888 "Y8888  888          Y8P      88888P"   "Y88888 
                                                                            888           888 
                                                                            888      Y8b d88P 
                                                                            888       "Y88P"

                                                                             version 1.25.314
        """)
        (lambda: (self.printing_effect(logo), self.transition_effect()))()

    def printing_effect(self, message):
        for char in message:
            print(char, end='', flush=True)
            time.sleep(self.printing_delay)
        print(flush=True)
        time.sleep(self.printing_delay)

    def transition_effect(self):
        time.sleep(self.processing_delay)
        os.system('cls' if os.name == 'nt' else 'clear') # + " && echo.")
        time.sleep(self.processing_delay)

    def verification(self, question, isTrue_message, isFalse_message):
        while True:
            user_input = input(f"Bot >>> {question}").strip().lower()
            if user_input in ['y', 'yes']:
                self.printing_effect(isTrue_message)
                time.sleep(self.processing_delay)
                return True
            elif user_input in ['n', 'no']:
                (lambda: (self.printing_effect(isFalse_message), self.transition_effect()))()
                return False
            else:
                self.printing_effect("Invalid input. Please try again.")

    def main_menu(self):
        # Font name: 4Max
        elpepe = "-" * 68
        display_mm = textwrap.dedent(f"""
            .dP"Y8  dP"Yb  88""Yb 888888 888888 88""Yb             88""Yb Yb  dP 
            `Ybo." dP   Yb 88__dP   88   88__   88__dP             88__dP  YbdP  
            o.`Y8b Yb   dP 88"Yb    88   88""   88"Yb      .o.     88\"""    8P   
            8bodP'  YbodP  88  Yb   88   888888 88  Yb     `"'     88      dP    

            Welcome to the Text Sorter version 1.23.456!
            Still in development.
            {elpepe}
            [1] Alphabetically Text Sorter
            [2] Anti-Alphabetically Text Sorter
            [3] Random Text Sorter
            [4] About
            [5] Settings
            [6] Sources
            [7] Exit
            {elpepe}
            Choose an option between [1] and [7]
        """)
        return display_mm

    def user_input(self):
        while True:
            menu = self.main_menu()
            self.printing_effect(menu)
            cmds = {
                '1': self.alphabetically_sorter.user_input_AS,
                '2': self.anti_alphabetically_sorter.user_input_AAS,
                '3': self.random_sorter.user_input_RS,
                '4': self.about,
                '5': self.passing_arguements,
                '6': self.sources,
                '7': self.exit
            }
            user_request = input(f"{self.file_name}> ").strip().lower()
            if user_request in cmds:
                self.transition_effect()
                cmds[user_request]()
            elif not user_request:
                (lambda: (self.printing_effect("Missing input. Please try again."), self.transition_effect()))()
            else:
                (lambda: (self.printing_effect("Invalid input. Please try again."), self.transition_effect()))()

# The 7 main functions of the program

    # Momentary placeholder
    def passing_arguements(self):
        (lambda: (self.printing_effect("\nNot yet implemented."), input("\nPress [Enter] to return to the menu"), self.transition_effect()))()

    def about(self):
        if not self.about_txt.is_file():
            self.printing_effect(f"Error: The file '{self.about_txt}' does not exist.")
            return
        with open(self.about_txt, "r") as file:
            content = file.read()
            self.printing_effect(content)
        input("\nPress [Enter] to return to the menu")
        self.transition_effect()

    # If necessary
    def settings(self):
        pass

    def sources(self):
        if not self.sources_txt.is_file():
            self.printing_effect(f"Error: The file '{self.sources_txt}' does not exist.")
            return
        with open(self.sources_txt, "r") as file:
            contents = file.read()
            self.printing_effect(contents)
        input("\nPress [Enter] to return to the menu")
        self.transition_effect()

    def exit(self):
        question = "Are you sure you want to exit the program? (Y/N): "
        isTrue_message = f"Exiting {self.file_name}..."
        isFalse_message = "Returning to main menu..."
        if self.verification(question, isTrue_message, isFalse_message):
            sys.exit(0)

    def running(self):
        self.logo()
        while True:
            self.user_input()

# The 3 Main Programs

    class AlpahbeticallySorter:
        def __init__(self, parent):
            self.parent = parent

        def display_AS(self):
            while True:
                I = "-" * 100
                title_1 = '''
                       db    88     88""Yb 88  88    db    88""Yb 888888 888888 88  dP""b8    db    88     88     Yb  dP 
                      dPYb   88     88__dP 88  88   dPYb   88__dP 88__     88   88 dP   `"   dPYb   88     88      YbdP  
                     dP__Yb  88  .o 88""   888888  dP__Yb  88""Yb 88""     88   88 Yb       dP__Yb  88  .o 88  .o   8P   
                    dP""""Yb 88ood8 88     88  88 dP""""Yb 88oodP 888888   88   88  YboodP dP""""Yb 88ood8 88ood8  dP 
                    
                    .dP"Y8  dP"Yb  88""Yb 888888 888888 88""Yb 
                    `Ybo." dP   Yb 88__dP   88   88__   88__dP 
                    o.`Y8b Yb   dP 88"Yb    88   88""   88"Yb  
                    8bodP'  YbodP  88  Yb   88   888888 88  Yb 
                '''
                display_as = textwrap.dedent(f"""
                    {title_1}
                    {I}
                    [1] Simple Inline List (Comma-Separated)
                        Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : apple, banana, cherry

                    [2] Bullet Point List
                        Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : - apple
                                    - banana
                                    - cherry

                    [3] Numbered List
                        Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : 1. apple
                                    2. banana
                                    3. cherry

                    [4] Alphabetical List
                        Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : a. apple
                                    b. banana
                                    c. cherry

                    [5] Line-Breaked List
                        Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : apple
                                    banana
                                    cherry

                    [6] Parenthesized List
                        Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : (apple, banana, cherry)

                    [7] Bracketed List
                        Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : [apple, banana, cherry]

                    [8] Dash-Separated List
                        Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : apple - banana - cherry

                    [9] Return to Main Menu
                    {I}
                    Choose an option between [1] and [9]
                    """)
                return display_as

        def user_input_AS(self):
            while True:
                menu_1 = self.display_AS()
                self.parent.printing_effect(menu_1)
                cmds_AS = {
                    '1': self.SimpleInlineList,
                    '2': self.BulletPointList,
                    '3': self.NumberedList,
                    '4': self.AlphabeticalList,
                    '5': self.LineBreakedList,
                    '6': self.ParenthesizedList,
                    '7': self.BracketedList,
                    '8': self.DashSeparatedList,
                }
                user_request_AS = input(f"{self.parent.file_name}> ").strip().lower()
                if user_request_AS == '9':
                    (lambda: (self.parent.transition_effect(), self.parent.user_input()))()
                    break
                elif user_request_AS in cmds_AS:
                    to_be_sorted_1 = input("\nEnter items separated by commas: ").strip()
                    if not to_be_sorted_1:
                        (lambda: (self.parent.printing_effect("No items entered. Please try again."), self.parent.transition_effect()))()
                        continue
                    cmds_AS[user_request_AS](to_be_sorted_1)
                else:
                    (lambda: (self.parent.printing_effect("Invalid input. Please try again."), self.parent.transition_effect()))()

        def removebracketsandstuff(self, remove):
            # Removes "", '', [], () and {}
            remove = remove.replace("[", "").replace("]", "").replace('"', "").replace("'", "").replace("(", "").replace(")", "").replace("{", "").replace("}", "")
            return [item.strip() for item in remove.split(",")]

        def SimpleInlineList(self, remove):
            before_1 = self.removebracketsandstuff(remove)
            new_list_1 = sorted(before_1) 
            after_1 = ", ".join(new_list_1)
            result_1 = [
                f"Unsorted Inline list: {', '.join(before_1)}",
                f"Sorted Inline list without brackets: {after_1}"
            ]
            self.parent.printing_effect("\n".join(result_1))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AS()))()

        def BulletPointList(self, remove):
            before_2 = self.removebracketsandstuff(remove)
            before_2a = "\n" + "\n".join(f"- {item}" for item in before_2)
            new_list_2 = sorted(before_2)
            after_2 = "\n" + "\n".join(f"- {item}" for item in new_list_2)
            result_2 = [
                f"Unsorted list: {', '.join(before_2)}",
                f"\nUnorted bullet point list without brackets: {before_2a}",
                f"\nSorted bullet point list without brackets: {after_2}"
            ]
            self.parent.printing_effect("\n".join(result_2))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AS()))()

        def NumberedList(self, remove):
            before_3 = self.removebracketsandstuff(remove)
            before_3a = "\n" + "\n".join(f"{i+1}. {item}" for i, item in enumerate(before_3))
            new_list_3 = sorted(before_3)
            after_3 = "\n" + "\n".join(f"{i+1}. {item}" for i, item in enumerate(new_list_3))
            result_3 = [
                f"Unsorted list: {', '.join(before_3)}",
                f"\nUnsorted numbered list without brackets: {before_3a}",
                f"\nSorted numbered list without brackets: {after_3}"
            ]
            self.parent.printing_effect("\n".join(result_3))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AS()))()

        def AlphabeticalList(self, remove):
            before_4 = self.removebracketsandstuff(remove)
            before_4a = "\n" + "\n".join(f"{chr(97 + i)}. {item}" for i, item in enumerate(before_4)) # char(97) = a, char(97 + i) = a, b, c, ... for 97 + i > 97
            new_list_4 = sorted(before_4)
            after_4 = "\n" + "\n".join(f"{chr(97 + i)}. {item}" for i, item in enumerate(new_list_4))
            result_4 = [
                f"Unsorted list: {', '.join(before_4)}",
                f"\nUnsorted numbered list without brackets: {before_4a}",
                f"\nSorted numbered list without brackets: {after_4}"
            ]
            self.parent.printing_effect("\n".join(result_4))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AS()))()

        def LineBreakedList(self, remove):
            before_5 = self.removebracketsandstuff(remove)
            before_5a = "\n".join(before_5)
            new_list_5 = sorted(before_5)
            after_5 = "\n".join(new_list_5)

            result_3 = [
                f"Unsorted list: {', '.join(before_5)}",
                f"\nUnsorted line-breaked list:\n{before_5a}",
                f"\nSorted line-breaked list:\n{after_5}"
            ]
            self.parent.printing_effect("\n".join(result_3))

            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AS()))()

        def ParenthesizedList(self, remove):
            before_6 = self.removebracketsandstuff(remove)
            new_list_6 = sorted(before_6) 
            after_6 = ", ".join(new_list_6)
            result_6 = [
                f"Unsorted parenthesized list: ({', '.join(before_6)})",
                f"Sorted parenthesized list: ({after_6})"
            ]
            self.parent.printing_effect("\n".join(result_6))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AS()))()

        def BracketedList(self, remove):
            before_7 = self.removebracketsandstuff(remove)
            new_list_7 = sorted(before_7) 
            after_7 = ", ".join(new_list_7)
            result_7 = [
                f"Unsorted bracketed list: [{', '.join(before_7)}]",
                f"Sorted bracketed list: [{after_7}]"
            ]
            self.parent.printing_effect("\n".join(result_7))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AS()))()

        def DashSeparatedList(self, remove):
            before_8 = self.removebracketsandstuff(remove)
            new_list_8 = sorted(before_8) 
            after_8 = " - ".join(new_list_8)
            result_8 = [
                f"Unsorted bracketed list: {' - '.join(before_8)}",
                f"Sorted bracketed list: {after_8}"
            ]
            self.parent.printing_effect("\n".join(result_8))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AS()))()

    class AntiAlpahbeticallySorter:
        def __init__(self, parent):
            self.parent = parent

        def display_AAS(sort):
            J = "-" * 123
            title_2 = '''
                88   88 88b 88    db    88     88""Yb 88  88    db    88""Yb 888888 888888 88  dP""b8    db     dP""b8 88     88     Yb  dP 
                88   88 88Yb88   dPYb   88     88__dP 88  88   dPYb   88__dP 88__     88   88 dP   `"   dPYb   dP   `" 88     88      YbdP  
                Y8   8P 88 Y88  dP__Yb  88  .o 88"""  888888  dP__Yb  88""Yb 88""     88   88 Yb       dP__Yb  Yb      88  .o 88  .o   8P   
                `YbodP' 88  Y8 dP""""Yb 88ood8 88     88  88 dP""""Yb 88oodP 888888   88   88  YboodP dP""""Yb  YboodP 88ood8 88ood8  dP    
                
                .dP"Y8  dP"Yb  88""Yb 888888 888888 88""Yb 
                `Ybo." dP   Yb 88__dP   88   88__   88__dP 
                o.`Y8b Yb   dP 88"Yb    88   88""   88"Yb  
                8bodP'  YbodP  88  Yb   88   888888 88  Yb 
            '''
            display_aas = textwrap.dedent(f"""
                {title_2}
                {J}
                [1] Simple Inline List (Comma-Separated)
                    Example:
                    - Unsorted: cherry, apple, banana
                    - Sorted  : cherry, banana, apple

                [2] Bullet Point List
                    Example:
                    - Unsorted: cherry, apple, banana
                    - Sorted  : - cherry
                                - banana
                                - apple

                [3] Numbered List
                    Example:
                        - Unsorted: cherry, apple, banana
                        - Sorted  : 1. cherry
                                    2. banana
                                    3. apple
                
                [4] Alphabetical List
                    Example:
                    - Unsorted: cherry, apple, banana
                    - Sorted  : a. cherry
                                b. banana
                                c. apple

                [5] Line-Breaked List
                    Example:
                    - Unsorted: cherry, apple, banana
                    - Sorted  : cherry
                                banana
                                apple

                [6] Parenthesized List
                    Example:
                    - Unsorted: cherry, apple, banana
                    - Sorted  : (cherry, banana, apple)

                [7] Bracketed List
                    Example:
                    - Unsorted: cherry, apple, banana
                    - Sorted  : [cherry, banana, apple]

                [8] Dash-Separated List
                    Example:
                    - Unsorted: cherry, apple, banana
                    - Sorted  : cherry - banana - apple

                [9] Return to Main Menu
                {J}
                Choose an option between [1] and [9]
                """)
            return display_aas

        def user_input_AAS(self):
            while True:
                menu_2 = self.display_AAS()
                self.parent.printing_effect(menu_2)
                cmds_AAS = {
                    '1': self.ReverseSimpleInlineList,
                    '2': self.ReverseBulletPointList,
                    '3': self.ReverseNumberedList,
                    '4': self.ReverseAlphabeticalList,
                    '5': self.ReverseLineBreakedList,
                    '6': self.ReverseLineBreakedList,
                    '7': self.ReverseParenthesizedList,
                    '8': self.ReverseBracketedList,
                }
                user_request_AAS = input(f"{self.parent.file_name}> ").strip().lower()
                if user_request_AAS == '9':
                    (lambda: (self.parent.transition_effect(), self.parent.user_input()))()
                    break
                elif user_request_AAS in cmds_AAS:
                    to_be_sorted_2 = input("\nEnter items separated by commas: ").strip()
                    if not to_be_sorted_2:
                        (lambda: (self.parent.printing_effect("No items entered. Please try again."), self.parent.transition_effect()))()
                        continue
                    cmds_AAS[user_request_AAS](to_be_sorted_2)
                else:
                    (lambda: (self.parent.printing_effect("Invalid input. Please try again."), self.parent.transition_effect()))()

        def removebracketsandstuff(self, remove):
            # Removes "", '', [], () and {}
            remove = remove.replace("[", "").replace("]", "").replace('"', "").replace("'", "").replace("(", "").replace(")", "").replace("{", "").replace("}", "")
            return [item.strip() for item in remove.split(",")]

        def ReverseSimpleInlineList(self, remove):
            before_1 = self.removebracketsandstuff(remove)
            new_list_1 = sorted(before_1, reverse=True) 
            after_1 = ", ".join(new_list_1)
            result_1 = [
                f"Unsorted Inline list: {', '.join(before_1)}",
                f"Sorted Inline list without brackets: {after_1}"
            ]
            self.parent.printing_effect("\n".join(result_1))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AAS()))()

        def ReverseBulletPointList(self, remove):
            before_2 = self.removebracketsandstuff(remove)
            before_2a = "\n" + "\n".join(f"- {item}" for item in before_2)
            new_list_2 = sorted(before_2, reverse=True)
            after_2 = "\n" + "\n".join(f"- {item}" for item in new_list_2)
            result_2 = [
                f"Unsorted list: {', '.join(before_2)}",
                f"\nUnorted bullet point list without brackets: {before_2a}",
                f"\nSorted bullet point list without brackets: {after_2}"
            ]
            self.parent.printing_effect("\n".join(result_2))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AAS()))()

        def ReverseNumberedList(self, remove):
            before_3 = self.removebracketsandstuff(remove)
            before_3a = "\n" + "\n".join(f"{i+1}. {item}" for i, item in enumerate(before_3))
            new_list_3 = sorted(before_3, reverse=True)
            after_3 = "\n" + "\n".join(f"{i+1}. {item}" for i, item in enumerate(new_list_3))
            result_3 = [
                f"Unsorted list: {', '.join(before_3)}",
                f"\nUnsorted numbered list without brackets: {before_3a}",
                f"\nSorted numbered list without brackets: {after_3}"
            ]
            self.parent.printing_effect("\n".join(result_3))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AAS()))()

        def ReverseAlphabeticalList(self, remove):
            before_4 = self.removebracketsandstuff(remove)
            before_4a = "\n" + "\n".join(f"{chr(97 + i)}. {item}" for i, item in enumerate(before_4)) # char(97) = a, char(97 + i) = a, b, c, ... for 97 + i > 97
            new_list_4 = sorted(before_4, reverse=True)
            after_4 = "\n" + "\n".join(f"{chr(97 + i)}. {item}" for i, item in enumerate(new_list_4))
            result_4 = [
                f"Unsorted list: {', '.join(before_4)}",
                f"\nUnsorted numbered list without brackets: {before_4a}",
                f"\nSorted numbered list without brackets: {after_4}"
            ]
            self.parent.printing_effect("\n".join(result_4))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AAS()))()

        def ReverseLineBreakedList(self, remove):
            before_5 = self.removebracketsandstuff(remove)
            before_5a = "\n".join(before_5)
            new_list_5 = sorted(before_5, reverse=True)
            after_5 = "\n".join(new_list_5)

            result_3 = [
                f"Unsorted list: {', '.join(before_5)}",
                f"\nUnsorted line-breaked list:\n{before_5a}",
                f"\nSorted line-breaked list:\n{after_5}"
            ]
            self.parent.printing_effect("\n".join(result_3))

            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AAS()))()

        def ReverseParenthesizedList(self, remove):
            before_6 = self.removebracketsandstuff(remove)
            new_list_6 = sorted(before_6, reverse=True) 
            after_6 = ", ".join(new_list_6)
            result_6 = [
                f"Unsorted parenthesized list: ({', '.join(before_6)})",
                f"Sorted parenthesized list: ({after_6})"
            ]
            self.parent.printing_effect("\n".join(result_6))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AAS()))()

        def ReverseBracketedList(self, remove):
            before_7 = self.removebracketsandstuff(remove)
            new_list_7 = sorted(before_7, reverse=True) 
            after_7 = ", ".join(new_list_7)
            result_7 = [
                f"Unsorted bracketed list: [{', '.join(before_7)}]",
                f"Sorted bracketed list: [{after_7}]"
            ]
            self.parent.printing_effect("\n".join(result_7))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AAS()))()

        def ReverseDashSeparatedList(self, remove):
            before_8 = self.removebracketsandstuff(remove)
            new_list_8 = sorted(before_8, reverse=True) 
            after_8 = " - ".join(new_list_8)
            result_8 = [
                f"Unsorted bracketed list: {' - '.join(before_8)}",
                f"Sorted bracketed list: {after_8}"
            ]
            self.parent.printing_effect("\n".join(result_8))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_AAS()))()

    class RandomSorter:
        def __init__(self, parent):
            self.parent = parent

        def display_RS(sort):
            K = "-" * 47
            title_3 = '''
                88""Yb    db    88b 88 8888b.   dP"Yb  8b    d8 
                88__dP   dPYb   88Yb88  8I  Yb dP   Yb 88b  d88 
                88"Yb   dP__Yb  88 Y88  8I  dY Yb   dP 88YbdP88 
                88  Yb dP""""Yb 88  Y8 8888Y"   YbodP  88 YY 88

                .dP"Y8  dP"Yb  88""Yb 888888 888888 88""Yb 
                `Ybo." dP   Yb 88__dP   88   88__   88__dP 
                o.`Y8b Yb   dP 88"Yb    88   88""   88"Yb  
                8bodP'  YbodP  88  Yb   88   888888 88  Yb  
            '''
            display_rs = textwrap.dedent(f"""
                {title_3}
                {K}
                [1] Simple Inline List (Comma-Separated)
                    Example:
                    - Original: apple, banana, cherry
                    - Randomised: banana, cherry, apple

                [2] Bullet Point List
                    Example:
                    - Original: apple, banana, cherry
                    - Randomised: - banana
                                  - cherry
                                  - apple

                [3] Numbered List
                    Example:
                    Original: apple, banana, cherry
                    Randomised: 1. banana
                                2. cherry
                                3. apple

                [4] Alphabetical List
                    Example:
                    Original: apple, banana, cherry
                    Randomised: a. cherry
                                b. banana
                                c. apple

                [5] Line-Breaked List
                    Example:
                    Original: apple, banana, cherry
                    Randomised: banana
                                cherry
                                apple

                [6] Parenthesized List
                    Example:
                    Original: apple, banana, cherry
                    Randomised: (banana, apple, cherry)

                [7] Bracketed List
                    Example:
                    Original: apple, banana, cherry
                    Randomised: [banana, cherry, apple]

                [8] Dash-Separated List
                    Example:
                    Original: apple, banana, cherry
                    Randomised: apple - cherry - banana

                [9] Return to Main Menu
                {K}
                Choose an option between [1] and [9]
                """)
            return display_rs

        def user_input_RS(self):
            while True:
                menu_3 = self.display_RS()
                self.parent.printing_effect(menu_3)
                cmds_RS = {
                    '1': self.RandomisedSimpleInlineList,
                    '2': self.RandomisedBulletPointList,
                    '3': self.RandomisedNumberedList,
                    '4': self.RandomisedAlphabeticalList,
                    '5': self.RandomisedLineBreakedList,
                    '6': self.RandomisedParenthesizedList,
                    '7': self.RandomisedBracketedList,
                    '8': self.RandomisedDashSeparatedList
                }
                user_request_RS = input(f"{self.parent.file_name}> ").strip().lower()
                if user_request_RS == '9':
                    (lambda: (self.parent.transition_effect(), self.parent.user_input()))()
                    break
                elif user_request_RS in cmds_RS:
                    to_be_sorted_3 = input("\nEnter items separated by commas: ").strip()
                    if not to_be_sorted_3:
                        (lambda: (self.parent.printing_effect("No items entered. Please try again."), self.parent.transition_effect()))()
                        continue
                    cmds_RS[user_request_RS](to_be_sorted_3)
                else:
                    (lambda: (self.parent.printing_effect("Invalid input. Please try again."), self.parent.transition_effect()))()

        def removebracketsandstuff(self, remove):
            # Removes "", '', [], () and {}
            remove = remove.replace("[", "").replace("]", "").replace('"', "").replace("'", "").replace("(", "").replace(")", "").replace("{", "").replace("}", "")
            return [item.strip() for item in remove.split(",")]

        def RandomisedSimpleInlineList(self, remove):
            before_1 = self.removebracketsandstuff(remove)
            new_list_1 = random.sample(before_1, len(before_1))
            after_1 = ", ".join(new_list_1)
            result_1 = [
                f"Shuffled bracketed list: [{after_1}]"
            ]
            self.parent.printing_effect("\n".join(result_1))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_RS()))()

        def RandomisedBulletPointList(self, remove):
            before_2 = self.removebracketsandstuff(remove)
            new_list_2 = random.sample(before_2, len(before_2))
            after_2 = "\n" + "\n".join(f"- {item}" for item in new_list_2)
            result_2 = [
                f"Unsorted list: {', '.join(before_2)}",
                f"\nShuffled bullet point list without brackets: {after_2}"
            ]
            self.parent.printing_effect("\n".join(result_2))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_RS()))()

        def RandomisedNumberedList(self, remove):
            before_3 = self.removebracketsandstuff(remove)
            new_list_3 = random.sample(before_3, len(before_3))
            after_3 = "\n" + "\n".join(f"{i+1}. {item}" for i, item in enumerate(new_list_3))
            result_3 = [
                f"Unsorted list: {', '.join(before_3)}",
                f"\nShuffled numbered list without brackets: {after_3}"
            ]
            self.parent.printing_effect("\n".join(result_3))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_RS()))()

        def RandomisedAlphabeticalList(self, remove):
            before_4 = self.removebracketsandstuff(remove)
            new_list_4 = random.sample(before_4, len(before_4))
            after_4 = "\n" + "\n".join(f"{chr(97 + i)}. {item}" for i, item in enumerate(new_list_4)) # char(97) = a, char(97 + i) = a, b, c, ... for 97 + i > 97
            result_4 = [
                f"Unsorted list: {', '.join(before_4)}",
                f"\nShuffled numbered list without brackets: {after_4}"
            ]
            self.parent.printing_effect("\n".join(result_4))
            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_RS()))()

        def RandomisedLineBreakedList(self, remove):
            before_5 = self.removebracketsandstuff(remove)
            new_list_5 = random.sample(before_5, len(before_5))
            after_5 = "\n".join(new_list_5)

            result_5 = [
                f"Unsorted list: {', '.join(before_5)}",
                f"\nShuffled line-breaked list:\n{after_5}"
            ]
            self.parent.printing_effect("\n".join(result_5))

            returning_2 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_2 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_RS()))()

        def RandomisedParenthesizedList(self, remove):
            before_6 = self.removebracketsandstuff(remove)
            new_list_6 = random.sample(before_6, len(before_6))
            after_6 = ", ".join(new_list_6)
            result_6 = [
                f"Shuffled parenthesized list: ({after_6})"
            ]
            self.parent.printing_effect("\n".join(result_6))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_RS()))()

        def RandomisedBracketedList(self, remove):
            before_7 = self.removebracketsandstuff(remove)
            new_list_7 = random.sample(before_7, len(before_7))
            after_7 = ", ".join(new_list_7)
            result_7 = [
                f"Shuffled bracketed list: [{after_7}]"
            ]
            self.parent.printing_effect("\n".join(result_7))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_RS()))()

        def RandomisedDashSeparatedList(self, remove):
            before_8 = self.removebracketsandstuff(remove)
            new_list_8 = random.sample(before_8, len(before_8))
            after_8 = " - ".join(new_list_8)
            result_8 = [
                f"Shuffled bracketed list: {after_8}"
            ]
            self.parent.printing_effect("\n".join(result_8))
            returning_1 = input("\nPress [Enter] to return to the menu: ").strip()
            if returning_1 == "":
                (lambda: (self.parent.transition_effect(), self.user_input_RS()))()

# "Run only when the script is executed" - Real Python
if __name__ == "__main__":
    run = Program()
    run.running()