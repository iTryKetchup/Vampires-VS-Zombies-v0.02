def show_instructions():
    print("Vampires VS Zombies Text Adventure v0.02")
    print("Instructions.")
    print("'go [north, south, east or west]' to move")
    print("'Inspect' to look around")
    print("'back' to return to prevoius room")
    print("'exit' to quit the game")
    print("\nType 'start' to begin your adventure or 'exit' to quit.")
    
    while True:
        command = input(">").strip().lower()
        if command == 'start':
            start_game()
            break
        elif command == 'exit':
            print("Too Hard? We get it! Goodbye!")
            break
        else:
            print("did you type that correctly? Please type 'start' to begin or 'exit' to quit.")

def start_game():
    print("Story Line 1")
    print("Story Line 2")
    print("Story Line 3")
    
    rooms = {
        'Rubble': {'east': 'Cliffs', 'west': 'Lake', 'south': 'Desert', 'north': 'Burning City'},
        'Cliffs': {'west': 'Rubble'},
        'Lake': {'east': 'Rubble'},
        'Desert': {'north': 'Rubble'},
        'Burning City': {'east': 'Sewers', 'west': 'Military Base', 'south': 'Rubble', 'north': 'Bowling Alley'},
    }
    
    current_room = 'Rubble'
    room_history = [current_room]

    while True:
        command = input(">").strip().lower()
        
        if command in ['go east', 'go west', 'go north', 'go south']:
            direction = command.split()[1]
            if direction in rooms[current_room]:
                room_history.append(current_room)
                current_room = rooms[current_room][direction]
            else:
                print("You cannot go that way. A zombie might be waiting!")
                if len(room_history) > 1:
                    current_room = room_history.pop()
        elif command == 'back':
            if len(room_history) > 1:
                current_room = room_history.pop()
            else:
                print("No way back!")
        elif command == 'inspect':
            print(f"You are in the {current_room}.")
            connections = rooms[current_room]
            for directions, room in connections.items():
                print(f"to the {direction}, there is {room}.")
        elif command == 'exit':
            break
        else:
            print("Unknown command! Try Again!")
            
        print(f"Current Room: {current_room}")
        
if __name__ == "__main__":
    show_instructions()         