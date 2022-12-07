import random


class TicTacToe:
    def __init__(self):
        self.record = {'x': [], 'o': []}
        self.number = set(range(1, 10))
        self.start_mark = 'x'
        self.result = None

    def mark_position(self, mark: str, position: int):
        self.record[mark].append(position)
        self.number.remove(position)

    def run(self):
        found_winner = 0

        while self.number:
            # Simulate human input number
            auto_input_number = random.choice(tuple(self.number))
            print(f"You chose position: {auto_input_number}")
            self.mark_position('x', auto_input_number)
            print(self.record)
            if TicTacToe.claim_winner(self.record['x']):
                self.result = 'You Win'
                found_winner = 1
                break

            # Computer generated number
            if self.number:
                auto_select_number = random.choice(tuple(self.number))
                print(f"Computer chose position: {auto_select_number}")
                self.mark_position('o', auto_select_number)
                print(self.record)
                if TicTacToe.claim_winner(self.record['o']):
                    self.result = 'You Loose'
                    found_winner = 1
                    break
        if found_winner == 0:
            print(self.record)
            self.result = 'Draw Game'
        print(self.result)

    @staticmethod
    def _horizontal_win(record_list):
        if ((1 in record_list) and (2 in record_list) and (3 in record_list)) or ((4 in record_list) and (5 in record_list) and (6 in record_list)) or ((7 in record_list) and (8 in record_list) and (9 in record_list)):
            return True
        return False

    @staticmethod
    def _vertical_win(record_list):
        if ((1 in record_list) and (4 in record_list) and (7 in record_list)) or ((2 in record_list) and (5 in record_list) and (8 in record_list)) or ((3 in record_list) and (6 in record_list) and (9 in record_list)):
            return True
        return False

    @staticmethod
    def _diagonal_win(record_list):
        if ((1 in record_list) and (5 in record_list) and (9 in record_list)) or ((3 in record_list) and (5 in record_list) and (7 in record_list)):
            return True
        return False

    @staticmethod
    def claim_winner(record_list):
        if TicTacToe._vertical_win(record_list) or TicTacToe._horizontal_win(record_list) or TicTacToe._diagonal_win(record_list):
            return True
        return False
