from gpiozero import Button

ONE = Button(4, hold_repeat=True)
TWO = Button(17, hold_repeat=True)
THREE = Button(27, hold_repeat=True)
FOUR = Button(22, hold_repeat=True)
FIVE = Button(10, hold_repeat=True)
SIX = Button(9, hold_repeat=True)
SEVEN = Button(11, hold_repeat=True)
EIGHT = Button(5, hold_repeat=True)
NINE = Button(6, hold_repeat=True)
ZERO = Button(13, hold_repeat=True)
ADD_PLAYER = Button(23, hold_repeat=True)
NEXT_PLAYER = Button(24, hold_repeat=True)
ADD = Button(8)
SUBTRACT = Button(7)
PAY = Button(12)
GO = Button(26)
COMMIT = Button(25)

BUTTONS = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, ZERO, GO)

STR_NUMS = {ONE: "1", TWO: "2", THREE: "3", FOUR: "4", FIVE: "5",
             SIX: "6", SEVEN: "7", EIGHT: "8", NINE: "9", ZERO: "10"}
