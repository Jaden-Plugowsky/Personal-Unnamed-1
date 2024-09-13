#!/usr/bin/env python3
"""
Created by: Jaden Plugowsky
Created on: Oct 2023
This program adds two user-inputted integers together.
"""


numberRow = "\n--1--2--3--"
ARow = "\nA-_--_--_--"
BRow = "\nB-_--_--_--"
CRow = "\nC-_--_--_--\n-----------\n"

def main() -> None:
    """Tic-tac-toe"""

    # Input
    print("Let's play tic-tac-toe. You are X.")
    print("Enter where you wish to go based on the coordinates system.")
    print("Type the letter, then a space, then the number. Ex: A 3")

    renderSquare()

    # Process

    # Output


def renderSquare() -> None:
    square = numberRow + ARow + BRow + CRow
    print(square)


if __name__ == "__main__":
    main()
