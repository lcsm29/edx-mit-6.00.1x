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

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call <img src="https://render.githubusercontent.com/render/math?math=\color{white}b_0">  (***b*** for ***balance***; subscript ***0*** to indicate this is the balance at month 0).

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

When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of `____` with `_ _ _ _` ). This is called ***usability*** - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

For this function, you may assume that all the letters in `secretWord` and `lettersGuessed` are lowercase.
<br><br>

### Problem 3 - Printing Out all Available Letters
[Solution for Problem Set 3, Problem 3](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/ps3/problem_3_printing_out_all_available_letters.py)
10.0/10.0 points (graded)

Next, implement the function `getAvailableLetters` that takes in one parameter - a list of letters, `lettersGuessed`. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are ***not*** in `lettersGuessed`.

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
