# Tic Tac Toe
Test driven design

This is a demo project on how to use test driven design (TDD) to guide us through software development. Drastically
different from traditional way of software development, TDD treats test as a design and fundamental of 
software development, so it advocates starting from writing test cases, and coding should serve as the implementation 
of test cases and address the errors of test cases if possible. 

## Test Design
There is a simple test file test_tic_tac_toe.py for pytest. The design of the tic tac toe game will be (thus as
reflected in the test file)
1. There should be a class that can do object-oriented programming
2. The game should have run method and get some results of win, lose, or draw
3. The class should be able to check win, lose, draw based on the distribution of 'x' and 'o'
4. The class should be able to record the inputs from both parties

## Code Implementation
The tictactoe.py file is to implement the design from test case. Herein, I used a dictionary to record the input positions for
'x' and 'o', and based on the input positions, we can tell if 'x' or 'o' wins the game during the process. And if 
the numbers from 1 to 9 are used up with no winners, we will claim it is a draw game. Since it is a demo project, there
is no human input, numbers from 1 to 9 are randomly chosen until they are used up.

## How to run the test
1. Install pytest
2. pytest or pytest -s (if you want to see all console outputs)

## How to run the program
python main.py

