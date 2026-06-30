#!/usr/bin/env python3
"""
Unbeatable Tic-Tac-Toe AI using Minimax with Alpha-Beta Pruning.

Run:
    python3 tic_tac_toe_ai.py
"""

from __future__ import annotations

from math import inf
from typing import List, Optional, Tuple

Board = List[str]
Move = Tuple[int, int]

HUMAN = "X"
AI = "O"
EMPTY = " " 

WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
)


def print_board(board: Board) -> None:
    """Display the board. Empty cells are shown as their move numbers."""
    cells = [board[i] if board[i] != EMPTY else str(i + 1) for i in range(9)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()


def winner(board: Board) -> Optional[str]:
    """Return 'X' or 'O' if either player has won; otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board: Board) -> bool:
    return EMPTY not in board


def game_over(board: Board) -> bool:
    return winner(board) is not None or is_full(board)


def available_moves(board: Board) -> List[int]:
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def score_terminal(board: Board, depth: int) -> int:
    """
    Score terminal states from the AI's perspective.

    Faster AI wins receive a larger score, and slower AI losses receive a
    less negative score. This makes the AI choose the shortest win or the
    longest survival if losing is unavoidable.
    """
    win = winner(board)
    if win == AI:
        return 10 - depth
    if win == HUMAN:
        return depth - 10
    return 0


def minimax(board: Board, depth: int, maximizing: bool, alpha: int, beta: int) -> int:
    """Minimax search with alpha-beta pruning."""
    if game_over(board):
        return score_terminal(board, depth)

    if maximizing:
        best_score = -inf
        for move in available_moves(board):
            board[move] = AI
            best_score = max(best_score, minimax(board, depth + 1, False, alpha, beta))
            board[move] = EMPTY
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return int(best_score)

    best_score = inf
    for move in available_moves(board):
        board[move] = HUMAN
        best_score = min(best_score, minimax(board, depth + 1, True, alpha, beta))
        board[move] = EMPTY
        beta = min(beta, best_score)
        if beta <= alpha:
            break
    return int(best_score)


def best_ai_move(board: Board) -> int:
    """Return the board index of the AI's optimal move."""
    best_score = -inf
    best_move = -1

    # Preferred order improves play style and pruning: center, corners, edges.
    preferred_order = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for move in preferred_order:
        if board[move] != EMPTY:
            continue
        board[move] = AI
        score = minimax(board, depth=0, maximizing=False, alpha=-inf, beta=inf)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def ask_yes_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y or n.")


def human_turn(board: Board) -> None:
    while True:
        raw = input("Choose your move (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        move = int(raw) - 1
        if move < 0 or move > 8:
            print("Please enter a number from 1 to 9.")
            continue
        if board[move] != EMPTY:
            print("That square is already occupied. Try again.")
            continue

        board[move] = HUMAN
        return


def ai_turn(board: Board) -> None:
    move = best_ai_move(board)
    board[move] = AI
    print(f"AI chooses {move + 1}.")


def announce_result(board: Board) -> None:
    win = winner(board)
    if win == HUMAN:
        print("You win! This should not happen if the AI is working correctly.")
    elif win == AI:
        print("AI wins!")
    else:
        print("It's a draw!")


def play_game() -> None:
    board: Board = [EMPTY] * 9

    print("Tic-Tac-Toe")
    print("You are X. The AI is O.")
    print("Enter the number of an empty square to move.")

    human_first = ask_yes_no("Do you want to go first? (y/n): ")

    while not game_over(board):
        print_board(board)

        if human_first:
            human_turn(board)
            if game_over(board):
                break
            print_board(board)
            ai_turn(board)
        else:
            ai_turn(board)
            if game_over(board):
                break
            print_board(board)
            human_turn(board)

    print_board(board)
    announce_result(board)


def main() -> None:
    while True:
        play_game()
        if not ask_yes_no("Play again? (y/n): "):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
