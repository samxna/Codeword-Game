# Samina Ahmed | 220023354 | 05/2023
# IN0005 - Introduction to Python Programming | Individual Project Assessment
# Codeword Game

# Import relevant modules that will be used throughout the code
import getch
from hashlib import sha256

# The solution_grid and solution_key are essentially the complete puzzle that the players need to guess
solution_grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#'], 
                 ['#', '#', '#', 'B', 'U', 'R', 'G', 'E', 'R'],
                 ['#', 'S', '#', '#', '#', '#', '#', '#', 'E'],
                 ['#', 'K', 'I', 'T', 'T', 'E', 'N', '#', 'D'],
                 ['#', 'Y', '#', '#', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', 'S', 'U', 'S', 'H', 'I', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#']]

solution_key = [[0,'B'], [1,'U'], [2,'R'], [3,'G'], [4,'E'], 
                [5,'S'], [6,'K'], [7,'I'], [8,'T'], [9,'N'], 
                [10,'D'], [11,'Y'], [12,'H']]

# This is the initial state of the player_grid and player_key and is what the players will be displayed with to begin guessing from. 
player_grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#'], 
               ['#', '#', '#', 'B', '1', '2', '3', '4', '2'],
               ['#', '5', '#', '#', '#', '#', '#', '#', '4'],
               ['#', '6', '7', '8', '8', '4', '9', '#', '10'],
               ['#', 'Y', '#', '#', '#', '#', '#', '#', '#'], 
               ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
               ['#', '#', '#', '5', '1', '5', '12', '7', '#'],
               ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
               ['#', '#', '#', '#', '#', '#', '#', '#', '#']]

player_key = [[0,'B'], [1,' '], [2,' '], [3,' '], [4,' '], 
              [5,' '], [6,' '], [7,' '], [8,' '], [9,' '], 
              [10,' '], [11,'Y'], [12,' ']]

def display_grid(grid):
    """
    This function takes a parameter of a grid, in this case the solution_grid or player_grid 
    and displays it nice and clearly.
    """
    
    print('\n')  # Print a new line to separate from any previous output
    for row in grid:  # Loop over each row in the 2D grid
        for item in row:  # Loop over each item in the current row
            print("{:<5}".format(item), end='')  # Print the current item, left-aligned with a fixed width of 5 characters
        print('\n')  # Print a new line to move to the next row


def display_key(key):
    """
    This function takes a parameter of a key, in this case the solution_key or player_key and 
    displays it horizontally, making it clear and easy to understand for the players.
    """
    print('\n')
    max_width = max(len(str(item[0])) for item in key)  # Get the maximum width of any element in the grid
    print('  '.join(str(i).rjust(max_width) for i in range(len(key))))  # Print column indices with extra space
    print('  '.join(str(item[1]).rjust(max_width) for item in key))  # Print row elements with extra space
    print('\n')


def display_admin_menu():
    """
    This function is called once an admin is logged in successfully. 
    They are then displayed with the Admin Menu below, which they can choose from.
    After they select an option, it re-displays the admin menu until they choose to quit.  
    """
    print("\n------------------------------------------------\n")
    print("\n- ADMIN MENU -")
    print("\n1. Display the code word puzzle (solution grid)")
    print("2. Display the code word puzzle (player grid)")
    print("3. Display the key grid (solution key)")
    print("4. Display the key grid (player key)")
    print("5. Add a word to the puzzle")
    print("6. Delete a word from the puzzle")
    print("7. Edit the puzzle")
    print("8. Create a new puzzle")
    print("9. Back to main menu")
    print("10. Exit")
    admin_choice = input("\nEnter your choice: ")

    if admin_choice == "1":
        print("\nDisplaying the code word puzzle (solution grid)...")
        display_grid(solution_grid)
        display_admin_menu()
    elif admin_choice == "2":
        print("\nDisplaying the code word puzzle (player grid)...")
        display_grid(player_grid)
    elif admin_choice == "3":
        print("\nDisplaying the key grid (solution key)...")
        display_key(solution_key)
        display_admin_menu()
    elif admin_choice == "4":
        print("\nDisplaying the key grid (player key)...")
        display_key(player_key)
    elif admin_choice == "5":
        print("\nAdding a word to the puzzle...")
        display_admin_menu()
    elif admin_choice == "6":
        print("\nDeleting a word from the puzzle...")
        display_admin_menu()
    elif admin_choice == "7":
        print("\nEdit the puzzle...")
        display_admin_menu()
    elif admin_choice == "8":
        print("\nCreating a new puzzle...")
        display_admin_menu()
    elif admin_choice == "9":
        print("\nBack to main menu")
        boot_up()
    elif admin_choice == "10":
        exit()
    else:
        print("\nInvalid choice. Please select an option from the menu: ")


def create_admin():
    """
    This function allows a authorised admin user to create a new admin account. The 
    function reads a database file, prompts the admin for their name, desired username, 
    and desired password, and then prompts the admin for a special admin key without displaying 
    it on the screen.
    """
    # Open the database file for reading
    db = open("database.txt", "r")

    # Only those with the special admin key are authorised to create admin accounts
    admin_key = "addj347"

    print("\n------------------------------------------------\n")
    print("- CREATE ADMIN -")

    # Prompt the admin for their name, desired username, and desired password
    create_admin_name = input("\nAdmin, enter your name: ")
    create_admin_user = input("Create username: ")
    create_admin_pass = input("Create password: ")
    
    # Prompt the admin for the special admin key without displaying it on the screen
    print("\nEnter admin key: ", end="")
    input_admin_key = ""
    while True:
        # The 'getch' module is being used here to * out the input to hide the letters when entering the secret admin key
        ch = getch.getch()
        if ch == "\n":
            break
        input_admin_key += ch
        print("*", end="")
    print("\n")   
    
    # Hash the username and password for security purposes
    hashed_admin_user = sha256(create_admin_user.encode('utf-8')).hexdigest()
    hashed_admin_pass = sha256(create_admin_pass.encode('utf-8')).hexdigest()

    # Check if the username is too short, and if so, restart the function
    if len(create_admin_user) <=3 or len(create_admin_pass) <=3:
        print("Too short, restart: ")
        create_admin()
    else: 
        # Loop through the database file and check if the username already exists
        for line in db:
            if hashed_admin_user in line:
                print("\nUsername exists")
                create_admin()
                
        # If the admin key is correct, open the database file for appending and add the new admin account
        if input_admin_key == admin_key:
            db = open("database.txt", "a")
            db.write(create_admin_name+", "+hashed_admin_user+", "+hashed_admin_pass+"\n")
            print("\nAdmin account successfully created!")
        else:
            # If the admin key is incorrect, restart the function
            print("\nIncorrect admin key, restart: ")
            create_admin()


def login_admin():
    """
    This function prompts the admin to enter their credentials and admin key. 
    It then checks whether the entered credentials match any lines in the database and 
    whether the admin key is correct, and either displays a successful login message and 
    calls the admin menu function or prompts the user to try again.
    """
    # Open the database file
    db = open("database.txt", "r")

    # Those with the correct admin key can only login successfully
    admin_key = "addj347"

    print("\n------------------------------------------------\n")
    print("- ADMIN LOGIN -")

    login_admin_name = input("\nEnter administrator name: ")
    login_admin_user = input("Enter username: ")
    
    # The 'getch' module is being used for the password and admin key to * out the inputs in order to hide it on the screen
    print("Enter your password: ", end="")
    login_admin_pass = ""
    while True:
        ch = getch.getch()
        if ch == "\n":
            break
        login_admin_pass += ch
        print("*", end="")
    print("\n")

    print("\nEnter admin key: ", end="")
    input_admin_key = ""
    while True:
        ch = getch.getch()
        if ch == "\n":
            break
        input_admin_key += ch
        print("*", end="")
    print("\n")

    # Hash the username and password for security purposes
    hashed_login_admin_user = sha256(login_admin_user.encode('utf-8')).hexdigest()
    hashed_login_admin_pass = sha256(login_admin_pass.encode('utf-8')).hexdigest()


    # Check if entered credentials match any lines in the database
    with open("database.txt", "r") as db:
        for line in db:
            fields = line.strip().split(", ")
            if fields[1] == hashed_login_admin_user and fields[2] == hashed_login_admin_pass:
                # If credentials match, check if admin key is correct
                if input_admin_key == admin_key:
                    print("\nAdmin login successful. Welcome", login_admin_name + "!")
                    # Close the database file
                    db.close()
                    # Call the admin menu function
                    display_admin_menu()
                    return
            # If credentials don't match, continue iterating through the file
        print("\nLogin unsuccessful. Please try again.")
    # Close the database file
    db.close()
    # Call the login admin function recursively to prompt for login again
    login_admin()

def is_players_logged_in(player1, player2):
    """
    Checks if both players are logged in.
    Returns True if both players are logged in, False otherwise.
    """
    if player1 is not None and player2 is not None:
        return True
    else:
        return False 

def replace_guess(grid, key, guess):
    """
    This function takes in a grid, a key, and a guess, and replaces any matching letters in the 
    grid with the guess until there are no more matches to be made, and then returns the modified grid.
    """
    while True:
        found_match = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == str(key[j][0]):
                    if guess.upper() == key[j][1]:
                        grid[i][j] = guess.upper()
                        found_match = True
        if not found_match:
            break
    return grid

def play_game(solution_grid, solution_key):
    """
    This is the main game function. It takes two parameters: solution_grid and solution_key.

    The function is used to play the codeword game where two players take turns guessing the letters 
    that correspond to numbers on a grid.

    The function checks if there are two players logged in before beginning the game, and it keeps 
    track of player statistics such as correct and incorrect guesses and health.

    Once the puzzle is solved, it announces the winner which is the player that has the highest health value. 
    """
    # Declare global variables
    global player1, player2, logged_in_players, player_grid, player_key, winner, current_player

    # Create a list of players
    players = [player1, player2]
    # Initialize the number of players logged in to the game
    num_players_logged_on = 2

    # Check if both players are logged in
    if player1 is None or player2 is None:
        print("\nYou must have two logged-in players to play the game!")
        print("Select an option from below to continue...")
        boot_up()
        return
    
    # Check if both players are in the list of logged in players
    if player1 not in logged_in_players or player2 not in logged_in_players:
        print("\nOne or both of the players are not logged in. Please log in first!")
        print("Select an option from below to continue...")
        boot_up()
        return
    
    # Create a dictionary of player statistics
    player_stats = {
        player1: {"num": 1, "correct": 0, "incorrect": 0, "health": 0},
        player2: {"num": 2, "correct": 0, "incorrect": 0, "health": 0}
    }

    # Fetch starting health for each player from the database
    with open("database.txt", "r") as db:
        for line in db:
            fields = line.strip().split(", ")
            if fields[0] == player1:
                player1_health = int(fields[3])
                player_stats[player1]["health"] = player1_health
            elif fields[0] == player2:
                player2_health = int(fields[3])
                player_stats[player2]["health"] = player2_health

    # Set the winner to None
    winner = None
    # Set the current player to player1 to begin the guessing part of the game with
    current_player = player1

    while True:
            # Check if there are any players logged on
            if num_players_logged_on == 0:
                print("No players are logged on. Exiting game.")
                break

            # Determine current player's health based on whose turn it is
            if current_player == player1:
                player_health = player1_health
            else:
                player_health = player2_health

            # Check if player has enough health to continue playing
            if player_health < 2:
                print(f"\nPlayer {players.index(current_player) + 1} doesn't have enough health to continue playing.")
                continue
            # Print current player stats
            else:
                print("\n------------------------------------------------\n")
                print(f"- CURRENT PLAYER STATS -\n")
                for player in players:
                    print(f"Player {player_stats[player]['num']}: {player} \nCorrect guesses = {player_stats[player]['correct']}, Incorrect guesses = {player_stats[player]['incorrect']}, Health = {player_stats[player]['health']}\n")
                
                # Display game play options
                print("\n- GAME PLAY -\n")
                wants_to_play = input(f"\n{current_player}, do you want to play? (y/n): ")
                # Check if player wants to quit the game
                if wants_to_play.lower() == 'n':
                    print(f"\n{current_player} has quit the game.")
                    num_players_logged_on -= 1
                # If player wants to play, show player grid and key
                elif wants_to_play.lower() == 'y':
                    print("\n------------------------------------------------\n")
                    print('\nPLAYER GRID:')
                    display_grid(player_grid)
                    print('\nPLAYER KEY:')
                    display_key(player_key)
                else:
                    # Loop the question until user enters a valid answer
                    while wants_to_play != "y" and wants_to_play != "n":
                        print("\nInvalid input. Please enter 'y' or 'n' to indicate whether you want to play or not.")
                        # Prompt player to input again
                        wants_to_play = input(f"\n{current_player}, do you want to play? (y/n): ")

                        # Check if player wants to quit the game
                        if wants_to_play.lower() == 'n':
                            print(f"\n{current_player} has quit the game.")
                            num_players_logged_on -= 1

                        # If player wants to play, show player grid and key
                        elif wants_to_play.lower() == 'y':
                            print("\n------------------------------------------------\n")
                            print('\nPLAYER GRID:')
                            display_grid(player_grid)
                            print('\nPLAYER KEY:')
                            display_key(player_key)

                try:
                    # Take the player inputs of the row and column for the location of the number they want to guess
                    row = int(input("\nEnter the row number (0-8 going down): "))
                    col = int(input("Enter the column number (0-8 going across): "))
                    # Take the player input of the letter they want to guess for this location in the grid
                    letter_guess = input("Enter the letter you'd like to guess: ").upper()

                    # Loop the input prompts until player enters valid inputs for a guess
                    while row > 8 or col > 8:
                        print("\nIvalid input: Out of range, please enter a number from 0-8!")
                        row = int(input("\nEnter the row number (0-8 going down): "))
                        col = int(input("Enter the column number (0-8 going across): "))
                        # Take the player input of the letter they want to guess for this location in the grid
                        letter_guess = input("Enter the letter you'd like to guess: ").upper()

                    # Replace the value at the given row and column in player_grid with the player's guess
                    original_value = player_grid[row][col]
                    player_grid[row][col] = letter_guess

                    # Check if the guess matches the value at the given row and column in solution_grid
                    if player_grid[row][col] == solution_grid[row][col]:
                        for i in range(len(player_key)):
                            if player_key[i][0] == solution_key[i][0]:
                                if letter_guess.upper() == solution_key[i][1]:
                                    player_key[i][1] = letter_guess.upper()

                        # Let the player know their guess is correct and update the stats for this player
                        print("\nWell done, that is correct!")
                        player_stats[current_player]["correct"] += 1
                        player_stats[current_player]["health"] += 2

                        # Replace all occurrences of the same number with the correct letter in player grid
                        for i in range(len(player_grid)):
                            for j in range(len(player_grid[i])):
                                if player_grid[i][j] == str(original_value):
                                    if solution_grid[i][j] == letter_guess.upper():
                                        player_grid[i][j] = letter_guess.upper()

                        display_grid(player_grid)
                        display_key(player_key)
                                        
                        # Check if the puzzle has been solved and declare a winner
                        if all([key[1] != ' ' for key in player_key]):
                            print("\nWHOOPIE! You have solved the puzzle!\n")

                            # Update the player's stats
                            player_stats[current_player]["correct"] += 1
                            player_stats[current_player]["health"] += 5
                            # Display the player stats
                            print("\nPLAYER STATISTICS:\n")
                            for player in players:
                                print(f"Player {player_stats[player]['num']}: {player} \nCorrect guesses = {player_stats[player]['correct']}, Incorrect guesses = {player_stats[player]['incorrect']}, Health = {player_stats[player]['health']}\n")

                            # Determine the winner based on the player with the highest health
                            winner = max(player_stats, key=lambda x: player_stats[x]['health'])

                            print("\n-----------------------------------------------")
                            print(f"\nCongratulations {winner}! You are the winner!\n ")
                            print("-----------------------------------------------")
                            # Exit the game
                            exit()

                    # If the guess is incorrect, update player stats accordingly and display the grid and key
                    else:
                        player_grid[row][col] = original_value
                        for i in range(len(player_key)):
                            if player_key[i][0] == solution_key[i][0]:
                                if letter_guess.upper() == solution_key[i][1]:
                                    player_key[i][1] = ' '
                        print("\nBoo! That is incorrect.\n")
                        player_stats[current_player]["incorrect"] += 1
                        player_stats[current_player]["health"] -= 2
                        display_grid(player_grid)
                        display_key(player_key)

                # Output an error message if the player inputs invalid values
                except ValueError:
                    print("\nInvalid input. Please enter a valid row and column number.")
                    continue
                    
            # Update the current player index
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
            print("Player " + str(current_player) + "'s turn")


def create_player():
    """
    This function allows a user to create a new player account by taking in the user's name, 
    username, and password as input. The function checks if the username already exists in the 
    database, and if not, hashes the username and password before writing it to the database with 
    an initial health value of 5.
    """
    # Declare the variable logged_in_players and set it to an empty list
    global logged_in_players
    logged_in_players = []

    print("\n------------------------------------------------\n")
    print("- CREATE PLAYER -")
    # Ask the user to input their name, username, and password
    create_player_name = input("\nPlease enter your name: ")
    create_player_user = input("Create username: ")
    create_player_pass = input("Create password: ") 
    # Set the player's health to 5
    player_health = 5
    # Hash the username and password using SHA-256 algorithm
    hashed_player_user = sha256(create_player_user.encode('utf-8')).hexdigest()
    hashed_player_pass = sha256(create_player_pass.encode('utf-8')).hexdigest()

    # Check if username and password are at least 4 characters long
    if len(create_player_user) <=3 or len(create_player_pass) <=3:
        print("\nToo short, restart: ")
        create_player()
    else: 
        # Check if the username already exists in the database
        with open("database.txt", "r") as db:
            for line in db:
                if hashed_player_user in line:
                    print("\nUsername exists")
                    create_player()

        # Add the new player to the database
        with open("database.txt", "a") as db:
            db.write(create_player_name+", "+hashed_player_user+", "+hashed_player_pass+", "+str(player_health)+"\n")
            print("\nSuccess! Welcome", create_player_name + "!\n")
            # Ensure that the file is closed properly after writing and that the changes are saved
            db.close()
            print("\nYou can now login!")
            login_player()

# Initialize player variables and list of logged in players, which are global variables that can be accessed from anywhere
player1 = None
player2 = None
logged_in_players = []

def login_player():
    """
    This function prompts the user to input their username and password, checks them against the 
    database, and logs in the user if the credentials are valid. If two players have logged in, 
    the function calls the play_game() function.
    """
    global player1, player2, logged_in_players

    # Open database file in read mode
    db = open("database.txt", "r")

    print("\n------------------------------------------------\n")
    print("- PLAYER LOGIN -")
    # Prompt user for input
    player_name = input("\nEnter your name: ")
    player_username = input("Enter your username: ")
    # Hide password input
    print("Enter your password: ", end="")
    player_password = ""
    while True:
        ch = getch.getch()
        if ch == "\n":
            break
        player_password += ch
        print("*", end="")
    print("\n")

    # Hash username and password
    hashed_username = sha256(player_username.encode('utf-8')).hexdigest()
    hashed_password = sha256(player_password.encode('utf-8')).hexdigest()

    # Check username and password in database
    with open("database.txt", "r") as db:
        for line in db:
            fields = line.strip().split(", ")
            if fields[1] == hashed_username and fields[2] == hashed_password:
                # Successful login
                print("\nLogin successful, hello", player_name + "!")
                if player1 is None:
                    player1 = player_name
                    print(f"\n{player1} is now Player 1\n")
                    logged_in_players.append(player1)
                elif player2 is None:
                    player2 = player_name
                    print(f"\n{player2} is now Player 2\n")
                    # Check if both players have logged in
                    logged_in_players.append(player2)
                    
                    if len(logged_in_players) == 2:
                        play_game(solution_grid, solution_key)
                else:
                    print("\nOnly two players are allowed to play this game!")
                return

    # Prompt the user to try again if the credentials are invalid
    print("\nInvalid username or password. Please try again.")
    for i in range(2):
        response = input("\nDo you want to try again? (y/n) ").strip().lower()
        if response == "y":
            return login_player()
        elif response == "n":
            return None
        else:
            print("\nInvalid response. Please enter 'y' or 'n'.")
    print("\nMaximum login attempts reached.")
    return None

def boot_up():
    """
    This is the starting function that is the boot up of the game. 
    This function initializes the game and prompts the user to choose between being an administrator, 
    player, or exiting the game. If the user chooses to be a player, they will be prompted to log in 
    or create an account before being able to play the game. This is also the same for the admin. 
    """
    global logged_in_players
    logged_in_players = []
    # Print welcome message
    print("\n------------------------------------------------")
    print("       WELCOME TO SAMINA'S CODEWORD GAME!       ")
    print("------------------------------------------------")

    # Prompt user for input
    print("\nPlease choose an option from below to begin:\n")
    print("1. Administrator")
    print("2. Player")
    print("3. Exit the system")
    choice = input("\nEnter 1, 2, or 3: ")

    # Check user's choice
    if choice == "1":
        while True:
            print("\n------------------------------------------------\n")
            print("- ADMIN - ")
            print("\nPlease choose an option from below:\n")
            print("1. Login")
            print("2. Create admin account")
            print("3. Back to menu")
            print("4. Exit")
            choice2 = input("\nEnter 1, 2, 3 or 4: ")

            # Perform the corresponding action based on user's input
            if choice2 == "1":
                login_admin()
            elif choice2 == "2":
                create_admin() 
            elif choice2 == "3":
                boot_up()
            elif choice2 == "4":
                print("\nExiting the game... See you soon! \n")
                exit()
            else:
                print("\nInvalid choice. Please enter 1, 2, 3, or 4: ")

    elif choice == "2":
        # Call the player_login function
        if not is_players_logged_in(player1, player2):
            print("\nBoth players must be logged in to start the game!")
            while True:
                print("\n------------------------------------------------\n")
                print("- PLAYER - ")
                print("\nPlease choose an option from below:\n")
                print("1. Login")
                print("2. Create player account")
                print("3. Back to menu")
                print("4. Exit")
                choice3 = input("\nEnter 1, 2, 3 or 4: ")

                # Perform the corresponding action based on user's input
                if choice3 == "1":
                    if len(logged_in_players) < 2:
                        login_player()
                elif choice3 == "2":
                    if len(logged_in_players) < 2:
                        create_player() 
                elif choice3 == "3":
                    boot_up()
                elif choice3 == "4":
                    print("\nExiting the game... See you soon! \n")
                    exit()
                else:
                    print("\nInvalid choice. Please enter 1, 2, 3, or 4: ")

        # Check if both players are logged in
        if is_players_logged_in():
            play_game()
    elif choice == "3":
        # End the program
        print("\nGoodbye!")
        exit()
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3: ")
        # Call the boot_up function again to prompt for input
        boot_up()

# This is the starting function that is to be run to launch the game.  
boot_up()