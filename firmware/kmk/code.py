print("Starting : Snowflake")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D9, board.D4, board.D5, board.D8)
keyboard.row_pins = (board.D10, board.D7, board.D3, board.D6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.NO,
        KC.N4, KC.N5, KC.N6, KC.NO,
        KC.N7, KC.N8, KC.N9, KC.NO,
        KC.N0, KC.A, KC.B, KC.C
    ]
]

if __name__ == '__main__':
    keyboard.go()