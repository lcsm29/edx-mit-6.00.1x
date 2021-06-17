# Table of Contents
- [Unit 1: Python Basics](#unit-1-python-basics)
  * [Problem Set 1](#problem-set-1)
    + [Problem 1](#problem-1)
    + [Problem 2](#problem-2)
    + [Problem 3](#problem-3)
- [Unit 2: Simple Programs](#unit-2-simple-programs)
  * [Problem Set 2](#problem-set-2)
    + [Introduction](#introduction)
    + [Problem 1 - Paying Debt off in a Year](#problem-1---paying-debt-off-in-a-year)
    + [Problem 2 - Paying Debt Off in a Year](#problem-2---paying-debt-off-in-a-year)
    + [Problem 3 - Using Bisection Search to Make the Program Faster](#problem-3---using-bisection-search-to-make-the-program-faster)
- [Unit 3: Structured Types](#unit-3-structured-types)
  * [Problem Set 3](#problem-set-3)
    + [Introduction](#introduction-1)
    + [Problem 1 - Is the Word Guessed](#problem-1---is-the-word-guessed)
    + [Problem 2 - Getting the User's Guess](#problem-2---getting-the-users-guess)
    + [Problem 3 - Printing Out all Available Letters](#problem-3---printing-out-all-available-letters)
    + [Problem 4 - The Game](#problem-4---the-game)

# Unit 1: Python Basics
## Problem Set 1
### Problem 1
[Solution for Problem Set 1, Problem 1](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps1/problem_1.py)
10.0/10.0 points (graded)

Assume `s` is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string `s`. Valid vowels are: `a`, `e`, `i`, `o`, and `u`. For example, if `s = 'azcbobobegghakl'`, your program should print:

`Number of vowels: 5`


### Problem 2
[Solution for Problem Set 1, Problem 2](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps1/problem_2.py)
10.0/10.0 points (graded)

Assume `s` is a string of lower case characters.

Write a program that prints the number of times the string `'bob'` occurs in `s`. For example, if `s = 'azcbobobegghakl'`, then your program should print

`Number of times bob occurs is: 2`


### Problem 3
[Solution for Problem Set 1, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps1/problem_3.py)
15.0/15.0 points (graded)

Assume `s` is a string of lower case characters.

Write a program that prints the longest substring of `s` in which the letters occur in alphabetical order. For example, if `s = 'azcbobobegghakl'`, then your program should print

`Longest substring in alphabetical order is: beggh`

In the case of ties, print the first substring. For example, if `s = 'abcbcd'`, then your program should print

`Longest substring in alphabetical order is: abc`

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

# Unit 2: Simple Programs
## Problem Set 2
### Introduction
Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, usually 2% of the balance due. However, the credit card company earns money by charging interest on the balance that you don't pay. So even if you pay credit card payments on time, interest is still accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate. If you only pay the minimum monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call <img src="https://render.githubusercontent.com/render/math?math=\color{white}b_0">  (***b*** for ***balance***; subscript ***0*** to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance. Let's call the payment you make in month 0, <img src="https://render.githubusercontent.com/render/math?math=\color{white}p_0">. Thus, your **unpaid balance** for month 0, <img src="https://render.githubusercontent.com/render/math?math=\color{white}ub_0">, is equal to <img src="https://render.githubusercontent.com/render/math?math=\color{white}b_0 - p_0">.

<center><img src="https://render.githubusercontent.com/render/math?math=\color{white}ub_0 = b_0 - p_0"></center>

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. So if your annual interest rate is , then at the beginning of month 1, your new balance is your previous unpaid balance <img src="https://render.githubusercontent.com/render/math?math=\color{white}ub_0">, **plus** the interest on this unpaid balance for the month. In algebra, this new balance would be

<center><img src="https://render.githubusercontent.com/render/math?math=\color{white}b_1 = ub_0 %2B r / 12.0 \cdot ub_0"></center>

In month 1, we will make another payment, <img src="https://render.githubusercontent.com/render/math?math=\color{white}p_1">. That payment has to cover some of the interest costs, so it does not completely go towards paying off the original charge. The balance at the beginning of month 2, <img src="https://render.githubusercontent.com/render/math?math=\color{white}b_2">, can be calculated by first calculating the unpaid balance after paying <img src="https://render.githubusercontent.com/render/math?math=\color{white}p_1">, then by adding the interest accrued:

<center><img src="https://render.githubusercontent.com/render/math?math=\color{white}ub_1 = b_1 - p_1">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}b_2 = ub_1 %2B r / 12.0 \cdot ub_1"></center>

If you choose just to pay off the minimum monthly payment each month, you will see that the compound interest will dramatically reduce your ability to lower your debt.

Let's look at an example. If you've got a $5,000 balance on a credit card with 18% annual interest rate, and the minimum monthly payment is 2% of the current balance, we would have the following repayment schedule if you only pay the minimum payment each month:

| Month |            Balance            |      Minimum Payment      |         Unpaid Balance         |             Interest             |
| :---: | :---------------------------: | :-----------------------: | :----------------------------: | :------------------------------: |
|   0   |            5000.00            |    100 (= 5000    * 0.02) |      4900 (= 5000    - 100)    |   73.50 (= 0.18/12.0 * 4900)     |
|   1   |  4973.50 (= 4900    + 73.50)  |  99.47 (= 4973.50 * 0.02) |   4874.03 (= 4973.50 - 99.47)  |   73.11 (= 0.18/12.0 * 4874.03)  |
|   2   |  4947.14 (= 4874.03 + 73.11)  |  98.94 (= 4947.14 * 0.02) |   4848.20 (= 4947.14 - 98.94)  |   72.72 (= 0.18/12.0 * 4848.20)  |

You can see that a lot of your payment is going to cover interest, and if you work this through month 12, you will see that after a year, you will have paid $1165.63 and yet you will still owe $4691.11 on what was originally a $5000.00 debt. Pretty depressing!

### Problem 1 - Paying Debt off in a Year
[Solution for Problem Set 2, Problem 1](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps2/problem_1.py)

### Problem 2 - Paying Debt Off in a Year
[Solution for Problem Set 2, Problem 2](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps2/problem_2.py)

### Problem 3 - Using Bisection Search to Make the Program Faster
[Solution for Problem Set 2, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps2/problem_3.py)


# Unit 3: Structured Types
## Problem Set 3
[Solution for the whole Problem Set 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/ps3_hangman.py)
### Introduction
Note: Do not be intimidated by this problem! It's actually easier than it looks. We will 'scaffold' this problem, guiding you through the creation of helper functions before you implement the actual game.

For this problem, you will implement a variation of the classic wordgame Hangman. For those of you who are unfamiliar with the rules, you may read all about it [here](https://en.wikipedia.org/wiki/Hangman_(game)). In this problem, the second player will always be the computer, who will be picking a word at random.

In this problem, you will implement a **function**, called `hangman`, that will start up and carry out an interactive Hangman game between a player and the computer. Before we get to this function, we'll first implement a few helper functions to get you going.

For this problem, you will need the code files [ps3_hangman.py](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/5820043834d84ad5f3a62e0a57cc97b4b1c6683c/ps3/ps3_hangman.py) and [words.txt](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/5820043834d84ad5f3a62e0a57cc97b4b1c6683c/ps3/words.txt). Right-click on each and hit "Save Link As". **Be sure to save them in same directory**. Open and run the file `ps3_hangman.py` without making any modifications to it, in order to ensure that everything is set up correctly. By "open and run" we mean do the following:

* Go to your IDE. From the File menu, choose "Open".
* Find the file ps3_hangman.py and choose it.
* The template ps3_hangman.py file should now be open. Run the file.

The code we have given you loads in a list of words from a file. If everything is working okay, after a small delay, you should see the following printed out:
```
Loading word list from file...
55909 words loaded.
```
If you see an `IOError` instead (e.g., "No such file or directory"), you should change the value of the `WORDLIST_FILENAME` constant (defined near the top of the file) to the **complete** pathname for the file `words.txt` (This will vary based on where you saved the file). Windows users, change the backslashes to forward slashes, like below.

For example, if you saved `ps3_hangman.py` and `ps3_words.txt` in the directory `"C:/Users/Ana/"` change the line: 

`WORDLIST_FILENAME = "words.txt"`  to something like

`WORDLIST_FILENAME = "C:/Users/Ana/words.txt"`

**This folder will vary depending on where you saved the files.**

The file `ps3_hangman.py` has a number of already implemented functions you can use while writing up your solution. You can ignore the code between the following comments, though you should read and understand how to use each helper function by reading the docstrings:
```
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
    .
    .
    .
# (end of helper code)
# -----------------------------------
```
You will want to do all of your coding for this problem within this file as well because you will be writing a program that depends on each function you write.

#### Requirements

Here are the requirements for your game:

1. The computer must select a word at random from the list of available words that was provided in words.txt. The functions for loading the word list and selecting a random word have already been provided for you in ps3_hangman.py.
2. The game must be interactive; the flow of the game should go as follows:
    * At the start of the game, let the user know how many letters the computer's word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
3. Some additional rules of the game:
    * A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).
    * A user loses a guess **only** when s/he guesses incorrectly.
    * If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try

#### Sample Output
<details>
<summary>The output of a winning game should look like this...</summary>
<br>

```
Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 4 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: _ a_ _
------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! You've already guessed that letter: _ a_ _
------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: s
Oops! That letter is not in my word: _ a_ _
------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
Please guess a letter: t
Good guess: ta_ t
------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqruvwxyz
Please guess a letter: r
Oops! That letter is not in my word: ta_ t
------------
You have 6 guesses left.
Available letters: bcdefghijklmnopquvwxyz
Please guess a letter: m
Oops! That letter is not in my word: ta_ t
------------
You have 5 guesses left.
Available letters: bcdefghijklnopquvwxyz
Please guess a letter: c
Good guess: tact
------------
Congratulations, you won!
```
</details>

<details>
<summary>And the output of a losing game should look like this...</summary>
<br>

```
Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 4 letters long.
-----------
You have 8 guesses left.
Available Letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! That letter is not in my word: _ _ _ _
-----------
You have 7 guesses left.
Available Letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: b
Oops! That letter is not in my word: _ _ _ _
-----------
You have 6 guesses left.
Available Letters: cdefghijklmnopqrstuvwxyz
Please guess a letter: c
Oops! That letter is not in my word: _ _ _ _
-----------
You have 5 guesses left.
Available Letters: defghijklmnopqrstuvwxyz
Please guess a letter: d
Oops! That letter is not in my word: _ _ _ _
-----------
You have 4 guesses left.
Available Letters: efghijklmnopqrstuvwxyz
Please guess a letter: e
Good guess: e_ _ e
-----------
You have 4 guesses left.
Available Letters: fghijklmnopqrstuvwxyz
Please guess a letter: f
Oops! That letter is not in my word: e_ _ e
-----------
You have 3 guesses left.
Available Letters: ghijklmnopqrstuvwxyz
Please guess a letter: g
Oops! That letter is not in my word: e_ _ e
-----------
You have 2 guesses left.
Available Letters: hijklmnopqrstuvwxyz
Please guess a letter: h
Oops! That letter is not in my word: e_ _ e
-----------
You have 1 guesses left.
Available Letters: ijklmnopqrstuvwxyz
Please guess a letter: i
Oops! That letter is not in my word: e_ _ e
-----------
Sorry, you ran out of guesses. The word was else.
```
</details>

### Problem 1 - Is the Word Guessed
[Solution for Problem Set 3, Problem 1](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_1_is_the_word_guessed.py)


### Problem 2 - Getting the User's Guess

[Solution for Problem Set 3, Problem 2](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_2_getting_the_users_guess.py)


### Problem 3 - Printing Out all Available Letters
[Solution for Problem Set 3, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_3_printing_out_all_available_letters.py)


### Problem 4 - The Game
[Solution for Problem Set 3, Problem 4](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_4_the_game.py)

