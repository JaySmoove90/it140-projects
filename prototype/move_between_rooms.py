"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Set the player's starting room.
current_room = "Great Hall"

# Main gameplay loop.
while current_room != "exit":
    print()
    print("You are in the", current_room)

    # Ask the player for a command.
    command = input("Enter a command: ").lower().strip()

    # Exit the game.
    if command == "exit":
        current_room = "exit"

    # Handle movement commands.
    elif command.startswith("go "):
        direction = command[3:]

        # Check whether the direction is valid from the current room.
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You cannot go that way.")

    # Handle any other invalid command.
    else:
        print("Invalid command.")

# End-of-game message.
print()
print("Thanks for playing!")
