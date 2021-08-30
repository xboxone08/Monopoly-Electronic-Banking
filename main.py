from tkinter import Tk, Label
from profile import Profile
import buttons

root = Tk()
root.geometry("1920x100")
root.resizable(False, False)

players = [Profile(), Profile()]
operation = ""
current_player = 0
player_display = Label(root, text="P" + str(current_player + 1))
player_display.pack(side="top")

text = Label(root)
text.pack(side="left")


def handle_buttons(dev):
    global current_player
    global operation
    global players

    if dev == buttons.ADD_PLAYER:
        players.append(Profile())
    elif dev == buttons.NEXT_PLAYER:
        current_player = current_player + \
            1 if current_player + 1 < len(players) else 0
        # Reset operation and display balance
        operation = ""
        text.config(text=players[current_player].money)
    elif dev == buttons.GO:
        players[current_player]
    elif dev == buttons.ADD:
        operation = '+'
    elif dev == buttons.SUBTRACT:
        operation = '-'
    elif dev == buttons.COMMIT:
        if operation == '+':
            players[current_player].add(int(text["text"]))
        elif operation == '-':
            players[current_player].subtract(int(text["text"]))
    else:
        if operation != "":  # Can only type when operating
            text.config(text=text["text"] +
                        buttons.STR_NUMS.get(dev))  # Typing


for b in buttons.BUTTONS:
    b.when_pressed = handle_buttons
    b.when_held = handle_buttons

root.mainloop()
