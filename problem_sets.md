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
- [Unit 4: Good Programming Practices](#unit-4-good-programming-practices)
  * [Problem Set 4](#problem-set-4)
    + [Introduction](#introduction-2)
    + [Getting Started](#getting-started)
    + [Problem 1 - Word Scores](#problem-1---word-scores)
    + [Problem 2 - Dealing with Hands](#problem-2---dealing-with-hands)
    + [Problem 3 - Valid Words](#problem-3---valid-words)
    + [Problem 4 - Hand Length](#problem-4---hand-length)
    + [Problem 5 - Playing a Hand](#problem-5---playing-a-hand)
    + [Problem 6 - Playing a Game](#problem-6---playing-a-game)
    + [Problem 7 - You and your Computer](#problem-7---you-and-your-computer)
- [Unit 5: Object Oriented Programming](#unit-5-object-oriented-programming)
  * [Problem Set 5](#problem-set-5)
    + [Introduction](#introduction-3)
    + [Problem 1 - Build the Shift Dictionary and Apply Shift](#problem-1---build-the-shift-dictionary-and-apply-shift)
    + [Problem 2 - PlaintextMessage](#problem-2---plaintextmessage)
    + [Problem 3 - CiphertextMessage](#problem-3---ciphertextmessage)
    + [Problem 4 - Decrypt a Story](#problem-4---decrypt-a-story)
- [Unit 6: Algorithmic Complexity](#unit-6-algorithmic-complexity)
  * [Problem Set 6](#problem-set-6)
    + [Problem 1](#problem-1-1)
    + [Problem 2](#problem-2-1)
    + [Problem 3](#problem-3-1)
    + [Problem 4](#problem-4)
    + [Problem 5](#problem-5)
    + [Problem 6](#problem-6)

# Unit 1: Python Basics
## Problem Set 1
### Problem 1
[Solution for Problem Set 1, Problem 1](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps1/problem_1.py)
10.0/10.0 points (graded)

Assume `s` is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string `s`. Valid vowels are: `a`, `e`, `i`, `o`, and `u`. For example, if `s = 'azcbobobegghakl'`, your program should print:

`Number of vowels: 5`
<br><br>

### Problem 2
[Solution for Problem Set 1, Problem 2](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps1/problem_2.py)
10.0/10.0 points (graded)

Assume `s` is a string of lower case characters.

Write a program that prints the number of times the string `'bob'` occurs in `s`. For example, if `s = 'azcbobobegghakl'`, then your program should print

`Number of times bob occurs is: 2`
<br><br>

### Problem 3
[Solution for Problem Set 1, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps1/problem_3.py)
15.0/15.0 points (graded)

Assume `s` is a string of lower case characters.

Write a program that prints the longest substring of `s` in which the letters occur in alphabetical order. For example, if `s = 'azcbobobegghakl'`, then your program should print

`Longest substring in alphabetical order is: beggh`

In the case of ties, print the first substring. For example, if `s = 'abcbcd'`, then your program should print

`Longest substring in alphabetical order is: abc`

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
<br><br>

# Unit 2: Simple Programs
## Problem Set 2
### Introduction
Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, usually 2% of the balance due. However, the credit card company earns money by charging interest on the balance that you don't pay. So even if you pay credit card payments on time, interest is still accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate. If you only pay the minimum monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call <img src="https://render.githubusercontent.com/render/math?math=\color{white}b_0">  (*b* for *balance*; subscript *0* to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance. Let's call the payment you make in month 0, <img src="https://render.githubusercontent.com/render/math?math=\color{white}p_0">. Thus, your **unpaid balance** for month 0, <img src="https://render.githubusercontent.com/render/math?math=\color{white}ub_0">, is equal to <img src="https://render.githubusercontent.com/render/math?math=\color{white}b_0 - p_0">.

<p align="center"><img align="center" src="https://render.githubusercontent.com/render/math?math=\color{white}ub_0 = b_0 - p_0"></p>

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. So if your annual interest rate is , then at the beginning of month 1, your new balance is your previous unpaid balance <img src="https://render.githubusercontent.com/render/math?math=\color{white}ub_0">, **plus** the interest on this unpaid balance for the month. In algebra, this new balance would be

<p align="center"><img src="https://render.githubusercontent.com/render/math?math=\color{white}b_1 = ub_0 %2B r / 12.0 \cdot ub_0"></p>

In month 1, we will make another payment, <img src="https://render.githubusercontent.com/render/math?math=\color{white}p_1">. That payment has to cover some of the interest costs, so it does not completely go towards paying off the original charge. The balance at the beginning of month 2, <img src="https://render.githubusercontent.com/render/math?math=\color{white}b_2">, can be calculated by first calculating the unpaid balance after paying <img src="https://render.githubusercontent.com/render/math?math=\color{white}p_1">, then by adding the interest accrued:

<p align="center"><img src="https://render.githubusercontent.com/render/math?math=\color{white}ub_1 = b_1 - p_1"></p>

<p align="center"><img src="https://render.githubusercontent.com/render/math?math=\color{white}b_2 = ub_1 %2B r / 12.0 \cdot ub_1"></p>

If you choose just to pay off the minimum monthly payment each month, you will see that the compound interest will dramatically reduce your ability to lower your debt.

Let's look at an example. If you've got a $5,000 balance on a credit card with 18% annual interest rate, and the minimum monthly payment is 2% of the current balance, we would have the following repayment schedule if you only pay the minimum payment each month:

| Month |            Balance            |      Minimum Payment      |         Unpaid Balance         |             Interest             |
| :---: | :---------------------------: | :-----------------------: | :----------------------------: | :------------------------------: |
|   0   |            5000.00            |    100 (= 5000    * 0.02) |      4900 (= 5000    - 100)    |   73.50 (= 0.18/12.0 * 4900)     |
|   1   |  4973.50 (= 4900    + 73.50)  |  99.47 (= 4973.50 * 0.02) |   4874.03 (= 4973.50 - 99.47)  |   73.11 (= 0.18/12.0 * 4874.03)  |
|   2   |  4947.14 (= 4874.03 + 73.11)  |  98.94 (= 4947.14 * 0.02) |   4848.20 (= 4947.14 - 98.94)  |   72.72 (= 0.18/12.0 * 4848.20)  |

You can see that a lot of your payment is going to cover interest, and if you work this through month 12, you will see that after a year, you will have paid $1165.63 and yet you will still owe $4691.11 on what was originally a $5000.00 debt. Pretty depressing!
<br><br>

### Problem 1 - Paying Debt off in a Year
[Solution for Problem Set 2, Problem 1](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps2/problem_1.py)
10.0/10.0 points (graded)

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

1. `balance` - the outstanding balance on the credit card
2. `annualInterestRate` - annual interest rate as a decimal
3. `monthlyPaymentRate` - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
```
Remaining balance: 813.41
```
instead of
```
Remaining balance: 813.4141998135 
```
So your program only prints out one thing: the remaining balance at the end of the year in the format:
```
Remaining balance: 4784.0
```
A summary of the required math is found below:

* **Monthly interest rate** = (Annual interest rate) / 12.0
* **Minimum monthly payment** = (Minimum monthly payment rate) x (Previous balance)
* **Monthly unpaid balance** = (Previous balance) - (Minimum monthly payment)
* **Updated balance each month** = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

**We provide sample test cases below**. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.

<details>
<summary>Click to See Problem 1 Test Cases</summary>
<br>

1. 
```
# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Result Your Code Should Generate Below:
Remaining balance: 31.38
        
# To make sure you are doing calculation correctly, this is the 
# remaining balance you should be getting at each month for this example
Month 1 Remaining balance: 40.99
Month 2 Remaining balance: 40.01
Month 3 Remaining balance: 39.05
Month 4 Remaining balance: 38.11
Month 5 Remaining balance: 37.2
Month 6 Remaining balance: 36.3
Month 7 Remaining balance: 35.43
Month 8 Remaining balance: 34.58
Month 9 Remaining balance: 33.75
Month 10 Remaining balance: 32.94
Month 11 Remaining balance: 32.15
Month 12 Remaining balance: 31.38
```
2. 
```
Test Case 2:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Result Your Code Should Generate Below:
Remaining balance: 361.61
```
</details>
<br><br>

### Problem 2 - Paying Debt Off in a Year
[Solution for Problem Set 2, Problem 2](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps2/problem_2.py)
15.0/15.0 points (graded)

Now write a program that calculates the minimum **fixed** monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

1. `balance` - the outstanding balance on the credit card
2. `annualInterestRate` - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
```
Lowest Payment: 180
```
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

* **Monthly interest rate** = (Annual interest rate) / 12.0
* **Monthly unpaid balance** = (Previous balance) - (Minimum fixed monthly payment)
* **Updated balance each month** = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

**We provide sample test cases below**. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.

<details>
<summary>Click to See Problem 2 Test Cases</summary>
<br>

1. 
```
Test Case 1:
balance = 3329
annualInterestRate = 0.2

Result Your Code Should Generate:
-------------------
Lowest Payment: 310
```
2. 
```
Test Case 2:
balance = 4773
annualInterestRate = 0.2

Result Your Code Should Generate:
-------------------
Lowest Payment: 440
```
3. 
```
Test Case 3:
balance = 3926
annualInterestRate = 0.2

Result Your Code Should Generate:
-------------------
Lowest Payment: 360
```
</details>
<br><br>

### Problem 3 - Using Bisection Search to Make the Program Faster
[Solution for Problem Set 2, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps2/problem_3.py)
20.0/20.0 points (graded)

You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

1. `balance` - the outstanding balance on the credit card
2. `annualInterestRate` - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable **lower bound** for this payment value? $0 is the obvious answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good **upper bound**? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

In short:
* **Monthly interest rate** = (Annual interest rate) / 12.0
* **Monthly payment lower bound** = Balance / 12
* **Monthly payment upper bound** = (Balance x (1 + Monthly interest rate)**12) / 12.0

<details>
<summary>Click to See Problem 3 Test Cases</summary>
<br>

**Note**: The automated tests are leinient - if your answers are off by a few cents in either direction, your code is OK.

Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Test Cases:
1. 
```
Test Case 1:
balance = 320000
annualInterestRate = 0.2

Result Your Code Should Generate:
-------------------
Lowest Payment: 29157.09
```
2. 
```
Test Case 2:
balance = 999999
annualInterestRate = 0.18

Result Your Code Should Generate:
-------------------
Lowest Payment: 90325.03
```
</details>
<br><br>

# Unit 3: Structured Types
## Problem Set 3
[Solution for Problem Set 3, Problem 1-4 (ps3_hangman.py)](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/ps3_hangman.py)
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
<br><br>

### Problem 1 - Is the Word Guessed
[Solution for Problem Set 3, Problem 1](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_1_is_the_word_guessed.py)
10.0/10.0 points (graded)

Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function `isWordGuessed` that takes in two parameters - a string, `secretWord`, and a list of letters, `lettersGuessed`. This function returns a boolean - `True` if `secretWord` has been guessed (ie, all the letters of `secretWord` are in `lettersGuessed`) and `False` otherwise.

Example Usage:
```
>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False
```
For this function, you may assume that all the letters in `secretWord` and `lettersGuessed` are lowercase.
<br><br>

### Problem 2 - Getting the User's Guess
[Solution for Problem Set 3, Problem 2](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_2_getting_the_users_guess.py)
10.0/10.0 points (graded)

Next, implement the function `getGuessedWord` that takes in two parameters - a string, `secretWord`, and a list of letters, `lettersGuessed`. This function returns a string that is comprised of letters and underscores, based on what letters in `lettersGuessed` are in `secretWord`. This shouldn't be too different from `isWordGuessed`!

Example Usage:
```
>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'
```

When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of `____` with `_ _ _ _` ). This is called *usability* - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

For this function, you may assume that all the letters in `secretWord` and `lettersGuessed` are lowercase.
<br><br>

### Problem 3 - Printing Out all Available Letters
[Solution for Problem Set 3, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_3_printing_out_all_available_letters.py)
10.0/10.0 points (graded)

Next, implement the function `getAvailableLetters` that takes in one parameter - a list of letters, `lettersGuessed`. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are **not** in `lettersGuessed`.

Example Usage:
```
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
```
Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in `lettersGuessed` are lowercase.

**Hint**: You might consider using `string.ascii_lowercase`, which is a string comprised of all lowercase letters:
```
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
```
<br><br>

### Problem 4 - The Game
[Solution for Problem Set 3, Problem 4](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_4_the_game.py)
15.0/15.0 points (graded)

Now you will implement the function `hangman`, which takes one parameter - the `secretWord` the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, `isWordGuessed`, `getGuessedWord`, and `getAvailableLetters`, that you've defined in the previous part.

**Hints:**
* You should start by noticing where we're using the provided functions (at the top of `ps3_hangman.py`) to load the words and pick a random one. Note that the functions `loadWords` and `chooseWord` should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your `hangman` function.
* Consider using `lower()` to convert user input to lower case. For example:
```
guess = 'A'
guessInLowerCase = guess.lower()
```
* Consider writing additional helper functions if you need them!
* There are four important pieces of information you may wish to store:
    1. `secretWord`: The word to guess.
    2. `lettersGuessed`: The letters that have been guessed so far.
    3. `mistakesMade`: The number of incorrect guesses made so far.
    4. `availableLetters`: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from `availableLetters` (and if they guess a letter that is not in `availableLetters`, you should print a message telling them they've already guessed that - so try again!).
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

Note that if you choose to use the helper functions `isWordGuessed`, `getGuessedWord`, or `getAvailableLetters`, you do not need to paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the problem. If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to `input` to get the user's guess.

<details>
<summary>Why does my Output Have None at Various Places?</summary>
<br>

`None` is a keyword and it comes from the fact that you are printing the result of a function that does not return anything. For example:
```
def foo(x):
    print(x)
```
If you just call the function with `foo(3)`, you will see output:
```
3   #-- because the function printed the variable
```
However, if you do `print(foo(3))`, you will see output:
```
3     #-- because the function printed the variable
None  #-- because you printed the function (and hence the return)
```
All functions return something. If a function you write does not return anything (and just prints something to the console), then the default action in Python is to `return None`
</details>
<br><br>

# Unit 4: Good Programming Practices
## Problem Set 4
[Solution for Problem Set 4, Problem 1-6 (ps4a.py)](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/ps4a.py), [Problem 7 (ps4b.py)](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/ps4b.py)
### Introduction
In this problem set, you'll implement two versions of a wordgame!

Don't be intimidated by the length of this problem set. There is a lot of reading, but it can be done with a reasonable amount of thinking and coding. It'll be helpful if you start this problem set a few days before it is due!

Let's begin by describing the 6.00 wordgame: This game is a lot like Scrabble or Words With Friends, if you've played those. Letters are dealt to players, who then construct one or more words out of their letters. Each **valid** word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:

**Dealing**
* A player is dealt a hand of `n` letters chosen at random (assume `n=7` for now).
* The player arranges the hand into as many words as they want out of the letters, using each letter at most once.
* Some letters may remain unused (these won't be scored).

**Scoring**
* The score for the hand is the sum of the scores for each word formed.
* The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all `n` letters are used on the first word created.
* Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary `SCRABBLE_LETTER_VALUES` that maps each lowercase letter to its Scrabble letter value.
* For example, `'weed'` would be worth `32` points (`(4+1+1+2)` for the four letters, then multiply by `len('weed')` to get `(4+1+1+2)*4 = 32`). Be sure to check that the hand actually has 1 `'w'`, 2 `'e'`s, and 1 `'d'` before scoring the word!
* As another example, if n=7 and you make the word `'waybill'` on the first try, it would be worth `155` points (the base score for `'waybill'` is `(4+1+4+3+1+1+1)*7=105`, plus an additional `50` point bonus for using all `n` letters).

#### Sample Output
<details>
<summary>Here is how the game output will look!</summary>
<br>

```
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points

Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points

Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points

Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points.

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```
</details>
<br><br>

### Getting Started
1. Download and save [ps4a.py](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/9da82a3e931aa0c762f1fc501ced072ecc49017a/ps4/ps4a.py), [ps4b.py](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/9da82a3e931aa0c762f1fc501ced072ecc49017a/ps4/ps4b.py), [test_ps4a.py](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/9da82a3e931aa0c762f1fc501ced072ecc49017a/ps4/test_ps4a.py) and [words.txt](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/9da82a3e931aa0c762f1fc501ced072ecc49017a/ps4/words.txt), which are the skeleton code you'll be filling in, the test functions, and a text file that contains a list of valid words. Make sure to save all the files  - `ps4a.py`, `ps4b.py`, `test_ps4a.py` and `words.txt` - in the **same folder**. We recommend creating a folder in your Documents folder called 6001x, and inside the 6001x folder, creating a separate folder for each problem set. If you don't follow this instruction, you may end up with issues because the files for this problem set depend on one another.

2. Run the file ps4a.py, without making any modifications to it, in order to ensure that everything is set up correctly (this means, open the file in IDLE, and use the Run command to load the file into the interpreter). The code we have given you loads a list of valid words from a file and then calls the `playGame` function. You will implement the functions it needs in order to work. If everything is okay, after a small delay, you should see the following printed out:

```
Loading word list from file...
      83667 words loaded.
playGame not yet implemented.
```

If you see an `IOError` instead (e.g., "No such file or directory"), you should change the value of the `WORDLIST_FILENAME` constant (defined near the top of the file) to the **complete pathname** for the file `words.txt` (This will vary based on where you saved the files).

For example, if you saved all the files including this `words.txt` in the directory `"C:/Users/Ana/6001x/PS4"` change the line: 

`WORDLIST_FILENAME = "words.txt"`  to something like 

`WORDLIST_FILENAME = "C:/Users/Ana/6001x/PS4/words.txt"`

Windows users, if you are copying the file path from Windows Explorer, you will have to change the backslashes to forward slashes.

3. The file `ps4a.py` has a number of already implemented functions you can use while writing up your solution. You can ignore the code between the following comments, though you should read and understand how to use each helper function by reading the docstrings:

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

4. This problem set is structured so that you will write a number of modular functions and then glue them together to form the complete word playing game. Instead of waiting until the entire game is ready, you should test each function you write, individually, before moving on. This approach is known as unit testing, and it will help you debug your code.

We have provided several test functions to get you started. After you've written each new function, unit test by running the file `test_ps4a.py` to check your work.

If your code passes the unit tests you will see a `SUCCESS` message; otherwise you will see a `FAILURE` message. These tests aren't exhaustive. You will want to test your code in other ways too.

Try running `test_ps4a.py` now (before you modify the `ps4a.py` skeleton). You should see that all the tests fail, because nothing has been implemented yet.

These are the provided test functions:

* **test_getWordScore()**: Test the getWordScore() implementation.
* **test_updateHand()**: Test the updateHand() implementation.
* **test_isValidWord()**: Test the isValidWord() implementation.
<br><br>

### Problem 1 - Word Scores
[Solution for Problem Set 4, Problem 1](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/problem_1.py)
10.0/10.0 points (graded)

The first step is to implement some code that allows us to calculate the score for a single word. The function getWordScore should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.

<details>
<summary>A Reminder of the Scoring Rules</summary>
<br>

**Scoring**
* The score for the hand is the sum of the scores for each word formed.
* The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all `n` letters are used on the first word created.
* Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary `SCRABBLE_LETTER_VALUES` that maps each lowercase letter to its Scrabble letter value.
* For example, `'weed'` would be worth `32` points (`(4+1+1+2)` for the four letters, then multiply by `len('weed')` to get `(4+1+1+2)*4 = 32`). Be sure to check that the hand actually has 1 `'w'`, 2 `'e'`s, and 1 `'d'` before scoring the word!
* As another example, if n=7 and you make the word `'waybill'` on the first try, it would be worth `155` points (the base score for `'waybill'` is `(4+1+4+3+1+1+1)*7=105`, plus an additional `50` point bonus for using all `n` letters).
</details>

#### Hints
* You may assume that the input `word` is always either a string of lowercase letters, or the empty string `""`.
* You will want to use the `SCRABBLE_LETTER_VALUES` dictionary defined at the top of `ps4a.py`. You should not change its value.
* Do **not** assume that there are always `7` letters in a hand! The parameter `n` is the number of letters required for a bonus score (the maximum number of letters in the hand). Our goal is to keep the code modular - if you want to try playing your word game with `n=10` or `n=4`, you will be able to do it by simply changing the value of `HAND_SIZE`!
* **Testing**: If this function is implemented properly, and you run `test_ps4a.py`, you should see that the `test_getWordScore()` tests pass. Also test your implementation of `getWordScore`, using some reasonable English words.

Fill in the code for `getWordScore` in `ps4a.py` and be sure you've passed the appropriate tests in `test_ps4a.py` before pasting your function definition here.
<br><br>

### Problem 2 - Dealing with Hands
[Solution for Problem Set 4, Problem 2](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/problem_2.py)
10.0/10.0 points (graded)

<span style="color:red">**Please read this problem entirely!!**</span> The majority of this problem consists of learning how to read code, which is an incredibly useful and important skill. At the end, you will implement a short function. Be sure to take your time on this problem - it may seem easy, but reading someone else's code can be challenging and this is an important exercise.

#### **Representing hands**
A **hand** is the set of letters held by a player during the game. The player is initially dealt a set of random letters. For example, the player could start out with the following hand: `a, q, l, m, u, i, l`. In our program, a hand will be represented as a dictionary: the keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand. For example, the above hand would be represented as:

```python:
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}    
```

Notice how the repeated letter `'l'` is represented. Remember that with a dictionary, the usual way to access a value is `hand['a']`, where `'a'` is the key we want to find. However, this only works if the key is in the dictionary; otherwise, we get a `KeyError`. To avoid this, we can use the call `hand.get('a', 0)`. This is the "safe" way to access a value if we are not sure the key is in the dictionary. `d.get(key,default)` returns the value for `key` if `key` is in the dictionary `d`, else `default`. If `default` is not given, it returns `None`, so that this method never raises a `KeyError`. For example:
```
>>> hand['e']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'e'
>>> hand.get('e', 0)
0
```

#### **Converting words into dictionary representation**
One useful function we've defined for you is `getFrequencyDict`, defined near the top of `ps4a.py`. When given a string of letters as an input, it returns a dictionary where the keys are letters and the values are the number of times that letter is represented in the input string. For example:
```shell:
>>> getFrequencyDict("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```
As you can see, this is the same kind of dictionary we use to represent hands.

#### **Displaying a hand**
Given a hand represented as a dictionary, we want to display it in a user-friendly way. We have provided the implementation for this in the `displayHand` function. Take a few minutes right now to read through this function carefully and understand what it does and how it works.

#### **Generating a random hand**
The hand a player is dealt is a set of letters chosen at random. We provide you with the implementation of a function that generates this random hand, `dealHand`. The function takes as input a positive integer `n`, and returns a new object, a hand containing `n` lowercase letters. Again, take a few minutes (right now!) to read through this function carefully and understand what it does and how it works.

#### **Removing letters from a hand (you implement this)**
The player starts with a hand, a set of letters. As the player spells out words, letters from this set are used up. For example, the player could start out with the following hand: `a, q, l, m, u, i, l`. The player could choose to spell the word `quail`. This would leave the following letters in the player's hand: `l, m`. Your task is to implement the function `updateHand`, which takes in two inputs - a `hand` and a `word` (string). `updateHand` uses letters from the hand to spell the word, and then returns a copy of the `hand`, containing only the letters remaining. For example:
```shell:
>>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
>>> displayHand(hand) # Implemented for you
a q l l m u i
>>> hand = updateHand(hand, 'quail') # You implement this function!
>>> hand
{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
>>> displayHand(hand)
l m
```
Implement the `updateHand` function. Make sure this function has no side effects: i.e., it must not mutate the hand passed in. Before pasting your function definition here, be sure you've passed the appropriate tests in `test_ps4a.py`.

#### Hints
<details>
<summary>Testing</summary>
<br>

**Testing**: Make sure the `test_updateHand()` tests pass. You will also want to test your implementation of `updateHand` with some reasonable inputs.
</details>

<details>
<summary>Copying Dictionaries</summary>
<br>

You may wish to review the ".copy" method of Python dictionaries (review this and other Python dictionary methods [here](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)).
</details>

Your implementation of updateHand should be short (ours is 4 lines of code). It does not need to call any helper functions.
<br><br>

### Problem 3 - Valid Words
[Solution for Problem Set 4, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/problem_3.py)
10.0/10.0 points (graded)

At this point, we have written code to generate a random hand and display that hand to the user. We can also ask the user for a word (Python's `input`) and score the word (using your `getWordScore`). However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game. A *valid* word is in the word list; **and** it is composed entirely of letters from the current hand. Implement the `isValidWord` function.

**Testing**: Make sure the `test_isValidWord` tests pass. In addition, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behavior be? Additionally, the empty string (`''`) is not a valid word - if you code this function correctly, you shouldn't need an additional check for this condition.

Fill in the code for `isValidWord` in `ps4a.py` and be sure you've passed the appropriate tests in `test_ps4a.py` before pasting your function definition here.
<br><br>

### Problem 4 - Hand Length
[Solution for Problem Set 4, Problem 4](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/problem_4.py)
10.0/10.0 points (graded)

We are now ready to begin writing the code that interacts with the player. We'll be implementing the `playHand` function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper `calculateHandlen` function, which can be done in under five lines of code.
<br><br>

### Problem 5 - Playing a Hand
[Solution for Problem Set 4, Problem 5](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/problem_5.py)
10.0/10.0 points (graded)

In `ps4a.py`, note that in the function `playHand`, there is a bunch of *pseudocode*. This pseudocode is provided to help guide you in writing your function. Check out the [Why Pseudocode?](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/WhyPseudocode.pdf) resource to learn more about the What and Why of Pseudocode before you start coding your solution.

**Note**: Do **not** assume that there will always be 7 letters in a hand! The parameter `n` represents the size of the hand.

**Testing**: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of `playHand`:

#### **Test Cases**
<details>
<summary>Case #1</summary>
<br>

Function Call:
```
wordList = loadWords()
playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
```
Output:
```
Current Hand:  a c i h m m z
Enter word, or a "." to indicate that you are finished: him
"him" earned 24 points. Total: 24 points

Current Hand:  a c m z
Enter word, or a "." to indicate that you are finished: cam
"cam" earned 21 points. Total: 45 points

Current Hand:  z
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 45 points.    
```
</details>
<details>
<summary>Case #2</summary>
<br>

Function Call:
```
wordList = loadWords()
playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
```
Output:
```
Current Hand:  a s t t w f o
Enter word, or a "." to indicate that you are finished: tow
"tow" earned 18 points. Total: 18 points

Current Hand:  a s t f
Enter word, or a "." to indicate that you are finished: tasf
Invalid word, please try again.

Current Hand:  a s t f
Enter word, or a "." to indicate that you are finished: fast
"fast" earned 28 points. Total: 46 points 

Run out of letters. Total score: 46 points.  
```
</details>
<details>
<summary>Case #3</summary>
<br>

Function Call:
```
wordList = loadWords()
playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)
```
Output:
```
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points

Run out of letters. Total score: 99 points.
```
</details>
<details>
<summary>Additional Testing</summary>
<br>

Be sure that, in addition to the listed tests, you test the same basic test conditions with varying values of `n`. `n` will never be smaller than the number of letters in the hand.
</details>
<br><br>

### Problem 6 - Playing a Game
[Solution for Problem Set 4, Problem 6](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/problem_6.py)
15.0/15.0 points (graded)

A game consists of playing multiple hands. We need to implement one final function to complete our word-game program. Write the code that implements the `playGame` function. You should remove the code that is currently uncommented in the `playGame` body. Read through the specification and make sure you understand what this function accomplishes. For the game, you should use the `HAND_SIZE` constant to determine the number of cards in a hand.

**Testing**: Try out this implementation as if you were playing the game. Try out different values for `HAND_SIZE` with your program, and be sure that you can play the wordgame with different hand sizes by modifying only the variable `HAND_SIZE`.

#### **Sample Output**
<details>
<summary>Here is how the game output should look...</summary>
<br>

```
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points

Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points

Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points

Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points.

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```
</details>
<details>
<summary>Hints about the output</summary>
<br>

Be sure to inspect the above sample output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in `playHand` - be sure that your code is modular and uses function calls to the `playHand` helper function!

You should also make calls to the `dealHand` helper function. You shouldn't make calls to any other helper function that we've written so far - in fact, this function can be written in about 15-20 lines of code.

Here is the above output, with the output from `playHand` obscured:
```
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```
</details>
<details>
<summary>Entering Your Code</summary>
<br>

Be sure to only paste your definition for `playGame` in the following box. Do not include any other function definitions.
</details>
<details>
<summary>A cool trick about 'print'</summary>
<br>

A cool trick about `print`: you can make two or more print statements print to the same line! Try out the following code. It will separate the first and second line with a space, and the second and third line with a "?" rather than putting each on a new line.
```
print('Hello', end = " ")
print('world', end="?")
print('!')
```
</details>
<br><br>

### Problem 7 - You and your Computer
[Solution for Problem Set 4, Problem 7](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps4/problem_7.py)
20.0/20.0 points (graded)

Now that your computer can choose a word, you need to give the computer the option to play. Write the code that re-implements the `playGame` function. You will modify the function to behave as described below in the function's comments. As before, you should use the `HAND_SIZE` constant to determine the number of cards in a hand. Be sure to try out different values for `HAND_SIZE` with your program.

#### **Sample Output and Hints**
<details>
<summary>Here is how the game output should look...</summary>
<br>

```
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Current Hand: a s r e t t t
Enter word, or a "." to indicate that you are finished: tatters
"tatters" earned 99 points. Total: 99 points

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a s r e t t t
"stretta" earned 99 points. Total: 99 points

Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: me
Invalid command.

Enter u to have yourself play, c to have the computer play: you
Invalid command.

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a c e d x l n
"axled" earned 65 points. Total: 65 points

Current Hand:  c n
Total score: 65 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Current Hand: a p y h h z o
Enter word, or a "." to indicate that you are finished: zap 
"zap" earned 42 points. Total: 42 points

Current Hand: y h h o
Enter word, or a "." to indicate that you are finished: oy
"oy" earned 10 points. Total: 52 points

Current Hand: h h
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 52 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a p y h h z o
"hypha" earned 80 points. Total: 80 points

Current Hand:  z o
Total score: 80 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```
</details>
<details>
<summary>Hints about the output</summary>
<br>

Be sure to inspect the above sample output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in `playHand` and `compPlayHand` - be sure that your code is modular and uses function calls to these helper functions!

You should also make calls to the `dealHand` helper function. You shouldn't make calls to any other helper function that we've written so far - in fact, this function can be written in about 15-20 lines of code.

Here is the above output, with the output from `playHand` and `compPlayHand` obscured:
```
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!
            
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

<call to compPlayHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: me
Invalid command.

Enter u to have yourself play, c to have the computer play: you
Invalid command.

Enter u to have yourself play, c to have the computer play: c

<call to compPlayHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

<call to compPlayHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```
</details>
<details>
<summary>A Note On Runtime</summary>
<br>

You may notice that things run slowly when the computer plays. This is to be expected. If you want (totally optional!), feel free to investigate ways of making the computer's turn go faster - one way is to preprocess the word list into a dictionary (string -> int) so looking up the score of a word becomes much faster in the `compChooseWord` function.

Be careful though - you only want to do this preprocessing one time - probably right after we generate the wordList for you (at the bottom of the file). If you choose to do this, you'll have to modify what inputs your functions take (they'll probably take a word dictionary instead of a word list, for example).

**IMPORTANT**:Don't worry about this issue when running your code in the checker below! We load a very small sample wordList (*much* smaller than 83667 words!) to avoid having your code time out. Your code will work even if you don't implement a form of pre-processing as described.
</details>
<details>
<summary>Entering Your Code</summary>
<br>

Be sure to only paste your definition for playGame from `ps4b.py` in the following box. Do not include any other function definitions.
</details>
<br><br>

# Unit 5: Object Oriented Programming
## Problem Set 5
[Solution for Problem Set 5, Problem 1-3 (ps5.py)](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps5/ps5.py), [Problem 4 (problem_4.py)](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps5/problem_4.py)
### Introduction
Encryption is the process of obscuring information to make it unreadable without special knowledge. For centuries, people have devised schemes to encrypt messages - some better than others - but the advent of the computer and the Internet revolutionized the field. These days, it's hard not to encounter some sort of encryption, whether you are buying something online or logging into a shared computer system. Encryption lets you share information with other trusted people, without fear of disclosure.

A cipher is an algorithm for performing encryption (and the reverse, decryption). The original information is called plaintext. After it is encrypted, it is called ciphertext. The ciphertext message contains all the information of the plaintext message, but it is not in a format readable by a human or computer without the proper mechanism to decrypt it; it should resemble random gibberish to those for whom it is not intended.

A cipher usually depends on a piece of auxiliary information, called a key. The key is incorporated into the encryption process; the same plaintext encrypted with two different keys should have two different ciphertexts. Without the key, it should be difficult to decrypt the resulting ciphertext into readable plaintext.

This assignment will deal with a well-known (though not very secure) encryption method called the Caesar cipher. Some vocabulary to get you started on this problem:

* *Encryption* - the process of obscuring or encoding messages to make them unreadable until they are decrypted
* *Decryption* - making encrypted messages readable again by decoding them
* *Cipher* - algorithm for performing encryption and decryption
* *Plaintext* - the original message
* *Ciphertext* - the encrypted message. Note: a ciphertext still contains all of the original message information, even if it looks like gibberish.

#### **The Caesar Cipher**

The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer. In other words, suppose the shift is k . Then, all instances of the i-th letter of the alphabet that appear in the plaintext should become the (i+k)-th letter of the alphabet in the ciphertext. You will need to be careful with the case in which i + k > 26 (the length of the alphabet). Here is what the whole alphabet looks like shifted three spots to the right:
```
Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
 3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c
```
Using the above key, we can quickly translate the message "happy" to "kdssb" (note how the 3-shifted alphabet wraps around at the end, so x -> a, y -> b, and z -> c).

**Note!!** We are using the English alphabet for this problem - that is, the following letters in the following order:
```
>>> import string
>>> print string.ascii_lowercase
abcdefghijklmnopqrstuvwxyz
```
We will treat uppercase and lowercase letters individually, so that uppercase letters are always mapped to an uppercase letter, and lowercase letters are always mapped to a lowercase letter. If an uppercase letter maps to "A", then the same lowercase letter should map to "a". Punctuation and spaces should be retained and not changed. For example, a plaintext message with a comma should have a corresponding ciphertext with a comma in the same position.

|    plaintext    |   shift   |    ciphertext    |
| :-------------: | :-------: | :--------------: |
|    'abcdef'     |     2     |     'cdefgh'     |
| 'Hello, World!' |     5     | 'Mjqqt, Btwqi!'  |
|       ''        | any value |        ''        |

We implemented for you two helper functions: `load_words` and `is_word`. You may use these in your solution and you do not need to understand them completely, but should read the associated comments. You should read and understand the helper code in the rest of the file and use it to guide your solutions.

Getting Started

To get started, download the following files in your working directory.

* [ps5.py](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/d10619867caf650ce88f0a4721eae658ea585078/ps5/ps5.py) - a file containing three classes that you will have to implement.
* [words.txt](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/d10619867caf650ce88f0a4721eae658ea585078/ps5/words.txt) - a file containing valid English words (should be in the same folder as your `ps5.py` file).
* [story.txt](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/d10619867caf650ce88f0a4721eae658ea585078/ps5/story.txt) - a file containing an encrypted message that you will have to decode (should be in the same folder as your `ps5.py` file).

This will be your first experience coding with classes! We will have a `Message` class with two subclasses `PlaintextMessage` and `CiphertextMessage`.
<br><br>

### Problem 1 - Build the Shift Dictionary and Apply Shift
[Solution for Problem Set 5, Problem 1](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps5/problem_1.py)
20.0/20.0 points (graded)

The `Message` class contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action).

In the next two questions, you will fill in the methods of the `Message` class found in `ps5.py` according to the specifications in the docstrings. The methods in the `Message` class already filled in are:

* `__init__(self, text)`
* The getter method `get_message_text(self)`
* The getter method `get_valid_words(self)`, notice that this one returns a copy of `self.valid_words` to prevent someone from mutating the original list.

In this problem, you will fill in two methods:

1. Fill in the `build_shift_dict(self, shift)` method of the `Message` class. Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".

If you are unfamiliar with the ordering or characters of the English alphabet, we will be following the letter ordering displayed by `string.ascii_lowercase` and `string.ascii_uppercase`:

```shell:
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
>>> print(string.ascii_uppercase)
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

A reminder from the introduction page - characters such as the space character, commas, periods, exclamation points, etc will not be encrypted by this cipher - basically, all the characters within `string.punctuation`, plus the space (`' '`) and all numerical characters (0 - 9) found in `string.digits`.

2. Fill in the `apply_shift(self, shift)` method of the `Message` class. You may find it easier to use `build_shift_dict(self, shift)`. Remember that spaces and punctuation should not be changed by the cipher.

Paste your implementation of the `Message` class in the box below.
<br><br>

### Problem 2 - PlaintextMessage
[Solution for Problem Set 5, Problem 2](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps5/problem_2.py)
15.0/15.0 points (graded)

For this problem, the graders will use our implementation of the `Message` class, so don't worry if you did not get the previous parts correct.

`PlaintextMessage` is a subclass of `Message` and has methods to encode a string using a specified shift value. Our class will always create an encoded version of the message, and will have methods for changing the encoding.

Implement the methods in the class `PlaintextMessage` according to the specifications in `ps5.py`. The methods you should fill in are:

* `__init__(self, text, shift)`: Use the parent class constructor to make your code more concise.
* The getter method `get_shift(self)`
* The getter method `get_encrypting_dict(self)`: This should return a COPY of `self.encrypting_dict` to prevent someone from mutating the original dictionary.
* The getter method `get_message_text_encrypted(self)`
* `change_shift(self, shift)`: Think about what other methods you can use to make this easier. It shouldn???t take more than a couple lines of code.

Paste your implementation of the entire `PlaintextMessage` class in the box below.
<br><br>

### Problem 3 - CiphertextMessage
[Solution for Problem Set 5, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps5/problem_3.py)
15.0/15.0 points (graded)

For this problem, the graders will use our implementation of the `Message` and `PlaintextMessage` classes, so don't worry if you did not get the previous parts correct.

Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial. If `message` is the encrypted message, and `s` is the shift used to encrypt the message, then `apply_shift(message, 26-s)` gives you the original plaintext message. Do you see why?

The problem, of course, is that you don???t know the shift. But our encryption method only has 26 distinct possible values for the shift! We know English is the main language of these emails, so if we can write a program that tries each shift and maximizes the number of English words in the decoded message, we can decrypt their cipher! A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words. Note that this only means that most of the words obtained are actual words. It is possible to have a message that can be decoded by two separate shifts into different sets of words. While there are various strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.

Fill in the methods in the class `CiphertextMessage` acording to the specifications in `ps5.py`. The methods you should fill in are:

* `__init__(self, text)`: Use the parent class constructor to make your code more concise.
* `decrypt_message(self)`: You may find the helper function `is_word(wordlist, word)` and the string method `split()` useful. Note that `is_word` will ignore punctuation and other special characters when considering whether a word is valid.

#### Hints
<details>
<summary>Using string.split</summary>
<br>

You may find the function `string.split` useful for dividing the text up into words.
```shell:
>>> 'Hello world!'.split('o')
['Hell', ' w', 'rld!']
>>> '6.00.1x is pretty fun'.split(' ')
['6.00.1x', 'is', 'pretty', 'fun']
```
</details>

Paste your implementation of the entire CiphertextMessage class in the box below.
<br><br>

### Problem 4 - Decrypt a Story
[Solution for Problem Set 5, Problem 4](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps5/problem_4.py)
5.0/5.0 points (graded)

For this problem, the graders will use our implementation of the `Message`, `PlaintextMessage`, and `CiphertextMessage` classes, so don't worry if you did not get the previous parts correct.

Now that you have all the pieces to the puzzle, please use them to decode the file `story.txt`. The file `ps5.py` contains a helper function `get_story_string()` that returns the encrypted version of the story as a string. Create a `CiphertextMessage` object using the story string and use `decrypt_message` to return the appropriate shift value and unencrypted story string.

Paste your function `decrypt_story()` in the box below.
<br><br>

# Unit 6: Algorithmic Complexity
## Problem Set 6
### Problem 1
#### Problem 1-1
The ONLY thing we are interested in when designing programs is that it returns the correct answer.
- [ ] True
- [x] False

#### Problem 1-2
When determining asymptotic complexity, we discard all terms except for the one with the largest growth rate.
- [x] True
- [ ] False

#### Problem 1-3
Bisection search is an example of linear time complexity
- [ ] True
- [x] False

#### Problem 1-4
For large values of `n`, an algorithm that takes `20000 * n**2` steps has better time complexity (takes less time) than one that takes `0.001 * n**5` steps
- [x] True
- [ ] False

### Problem 2
#### Problem 2-1
Indirection, as talked about in lecture, means you have to traverse the list more than once.
- [ ] True
- [x] False

#### Problem 2-2
The complexity of binary search on a sorted list of `n` items is `O(log n)`.
- [x] True
- [ ] False

#### Problem 2-3
The worst case time complexity for selection sort is `O(n**2)`.
- [x] True
- [ ] False

#### Problem 2-4
The base case for the recursive version of merge sort from lecture is checking ONLY for the list being empty.
- [ ] True
- [x] False

### Problem 3
For each of the following expressions, select the order of growth class that best describes it from the following list: 
* `O(1)`, `O(log(n))`, `O(n)`, `O(n * log(n))`, `O(n**c)`, or `O(c**n)`. Assume `c` is some constant.

1. `0.000_000_1n + 1_000_000`: `O(n)`
2. `0.000_1 * n**2 + 20_000 * n - 90_000`: `O(n**c)`
3. `20n + 900 * log(n) + 100_000`: `O(n)`
4. `(log(n))**2 + 5 * n**7`: `O(n**c)`
5. `n**200 - 2 * n**30`: `O(n**c)`
6. `30 * n**2 + n * log(n)`: `O(n**c)`
7. `n * log(n) - 3000 * n`: `O(n * log(n))`
8. `3`: `O(1)`
9. `5**n + n**5 + n + 5`: `O(c**n)`
10. `n * log(n) + n**2 + n + log(n) + 1 + 2**n`: `O(c**n)`

### Problem 4
#### Problem 4-1
Consider the following Python procedure. Specify its order of growth.: `O(1)`
```
def modten(n):
    return n%10
```

#### Problem 4-2
Consider the following Python procedure. Specify its order of growth.: `O(len(n))`
```
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result   
```

#### Problem 4-3
Consider the following Python procedure. Specify its order of growth.: `O(log(n))`
```
def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1
```

#### Problem 4-4
Consider the following Python procedure. Specify its order of growth.: `O(n)`
```
def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)
```

#### Problem 4-5
Consider the following Python procedure. Specify its order of growth.: `O(n**2)`
```
def baz(n):
    for i in range(n):
        for j in range(n):
            print( i,j )
```

### Problem 5
Here is code for linear search that uses the fact that a set of elements is sorted in increasing order:
```
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```
    
Consider the following code, which is an alternative version of search.
```
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
```
    
Which of the following statements is correct? You may assume that each function is tested with a list `L` whose elements are sorted in increasing order; for simplicity, assume `L` is a list of positive integers.
- [ ] `search` and `newsearch` return the same answers for all `L` and `e`.
- [ ] `search` and `newsearch` return the same answers provided `L` is non-empty.
- [ ] `search` and `newsearch` return the same answers provided `L` is non-empty and `e` is in `L`.
- [ ] `search` and `newsearch` never return the same answers.
- [x] `search` and `newsearch` return the same answers for lists `L` of length 0, 1, or 2.
- [ ] `search` and `newsearch` return the same answers for lists `L` of length 0 or 1.

### Problem 6
#### Problem 6-1
Answer the questions below based on the following sorting function. If it helps, you may paste the code in your programming environment. Study the output to make sure you understand the way it sorts.
```
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
```   
Does this function sort the list in increasing or decreasing order? (items at lower indices being smaller means it sorts in increasing order, and vice versa)
- [x] Increasing
- [ ] Decreasing

#### Problem 6-2
What is the worst case time complexity of swapSort? Consider different kinds of lists when the length of the list is large.
- [x] `O(n**2)`
- [ ] `O(n)`
- [ ] `O(log(n))`
- [ ] `O(1)`

#### Problem 6-3
If we make a small change to the line for j in range(i+1, len(L)): such that the code becomes:
```
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
```
What happens to the behavior of swapSort with this new code?
- [ ] No change
- [x] `modSwapSort` now orders the list in descending order for all lists.
- [ ] `modSwapSort` now orders the list in descending order for SOME lists but not all
- [ ] `modSwapSort` enters an infinite loop.

#### Problem 6-4
What happens to the time complexity of this modSwapSort?
- [x] Best and worst cases stay the same.
- [ ] Worst case stays the same but best case changes.
- [ ] Best and worst cases change.
