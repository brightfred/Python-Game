""" 
A comment describing the game module
"""

import PySimpleGUI as sg

# Brief comment about how the following lines work
game_state = "Forest"
game_places = {
    "Forest": {
        "Story": "You are in the forest. Paths lead in all directions.\n"
        "To the north is a cave entrance, to the south is a path to the castle.\n"
        "To the west, the ground rises toward a mountain, and to the east, you hear the sound of running water.",
        "North": "Cave Entrance",
        "South": "Castle",
        "East": "River",
        "West": "Mountain",
        "Image": "forest.png",
    },
    "Cave Entrance": {
        "Story": "You are at the entrance of a dark cave. The air is cold, brrrrrrrr , and you hear distant growls.\n"
        "To the south is the forest, and to the north is the cave’s interior.",
        "North": "Cave",
        "South": "Forest",
        "Image": "cave_entrance.png",
    },
    "Cave": {
        "Story": "You are inside the cave, facing a fearsome monster. It guards a key that might be useful later.\n"
        "Fight the monster or flee back to the cave entrance.",
        "South": "Cave Entrance",
        "Image": "cave.png",
        "Monster": True,
        "Item": "Key",
    },
    "Castle": {
        "Story": "You are at the castle. The gates are locked.\n"
        "Perhaps something in the forest can unlock them.",
        "North": "Forest",
        "Enter": "Treasure Hall",
        "Image": "castle.png",
        "Locked": True,
    },
    "Treasure Hall": {
        "Story": "You have entered the treasure hall inside the castle. The room is filled with ancient artifacts.\n"
        "However, the path to the treasure is blocked by a magical barrier. A key might be needed.",
        "Exit": "Castle",
        "Image": "treasure.png",
        "Locked": True,
    },
    "Mountain": {
        "Story": "You are at the base of a steep mountain. A narrow path winds up the mountain.\n"
        "To the east is the forest. You can climb up to explore the mountain peak.",
        "East": "Forest",
        "Climb": "Mountain Peak",
        "Image": "mountain.png",
    },
    "Mountain Peak": {
        "Story": "You are at the mountain peak. The view is breathtaking, and you find an old map pointing to the treasure hall in the castle.\n"
        "Climb down to the mountain base or follow the map to the castle.",
        "Down": "Mountain",
        "Image": "mountain_peak.png",
    },
    "River": {
        "Story": "You are at the edge of a fast-flowing river. There’s something shiny under the water.\n"
        "To the west is the forest. You can dive into the riverbed or return to the forest.",
        "West": "Forest",
        "Dive": "Riverbed",
        "Image": "river.png",
    },
    "Riverbed": {
        "Story": "You dive into the river and find a sunken chest. Inside, there’s a key that might unlock something important.\n"
        "Return to the riverbank with the key.",
        "Surface": "River",
        "Image": "riverbed.png",
        "Item": "Key",
    },
}


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state

    return game_places[game_state]["Story"]


def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South

    Returns:
        string: the story at the current place
    """
    global game_state

    if direction.lower() in "northsouth":  # is this a nasty check?
        game_place = game_places[game_state]
        proposed_state = game_place[direction]
        if proposed_state == "":
            return "You can not go that way.\n" + game_places[game_state]["Story"]
        else:
            game_state = proposed_state
            return game_places[game_state]["Story"]


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme("Dark Blue 3")  # please make your windows
    prompt_input = [
        sg.Text("Enter your command", font="Any 14"),
        sg.Input(key="-IN-", size=(20, 1), font="Any 14"),
    ]
    buttons = [sg.Button("Enter", bind_return_key=True), sg.Button("Exit")]
    command_col = sg.Column([prompt_input, buttons], element_justification="r")
    layout = [
        [
            sg.Image(r"forest.png", size=(100, 100), key="-IMG-"),
            sg.Text(show_current_place(), size=(100, 4), font="Any 12", key="-OUTPUT-"),
        ],
        [command_col],
    ]

    return sg.Window("Adventure Game", layout, size=(320, 200))


if __name__ == "__main__":
    # testing for now
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())

    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()
        print(event)
        if event == "Enter":
            if "North".lower() in values["-IN-"].lower():
                current_story = game_play("North")
                window["-OUTPUT-"].update(current_story)
            elif "South".lower() in values["-IN-"].lower():
                current_story = game_play("South")
                window["-OUTPUT-"].update(current_story)

            window["-IMG-"].update(game_places[game_state]["Image"], size=(100, 100))
            pass
        elif event == "Exit" or event is None or event == sg.WIN_CLOSED:
            break
        else:
            pass

    window.close()
