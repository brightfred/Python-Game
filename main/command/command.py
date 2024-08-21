class CommandParser:
    def __init__(self, game_state, monster_fight, inventory, status):
        self.game_state = game_state
        self.monster_fight = monster_fight
        self.inventory = inventory
        self.status = status

    def parse_command(self, command):
        command = command.lower()
        if command in ["north", "south"]:
            return self.move(command.capitalize())
        elif command == "fight":
            return self.monster_fight.start_fight()
        elif command == "inventory":
            return self.inventory.show_inventory()
        elif command == "status":
            return self.status.show_status()
        else:
            return "Invalid command."

    def move(self, direction):
        global game_state
        proposed_state = game_places[game_state][direction]
        if proposed_state == "":
            return f'You cannot go that way.\n{game_places[game_state]["Story"]}'
        else:
            game_state = proposed_state
            return game_places[game_state]["Story"]
