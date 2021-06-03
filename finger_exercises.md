# Table of Contents
- [Unit 1: Python Basics, Incomplete section](#unit-1--python-basics--incomplete-section)
  * [1. Introduction to Python](#1-introduction-to-python)
    + [Exercises 1](#exercises-1)
    + [Exercises 2](#exercises-2)
    + [Exercises 3](#exercises-3)
    + [Exercises 4](#exercises-4)
    + [Exercise 5](#exercise-5)
    + [Exercise 6](#exercise-6)
    + [Exercise 7](#exercise-7)
    + [Exercise 8](#exercise-8)
    + [Exercise 9](#exercise-9)
    + [Exercise 10](#exercise-10)
  * [2. Core Elements of Programs](#2-core-elements-of-programs)
- [Unit 2: dummy](#unit-2--dummy)

# Unit 1: Python Basics, Incomplete section

## 1. Introduction to Python

### Exercises 1
4/4 points (graded)

**1. What is the difference between an Algorithm and a Program?**
- [x] ***An algorithm is a conceptual idea, a program is a concrete instantiation of an algorithm.***
- [ ] An algorithm is limited to mathematical operation, a program can specify all kinds of operations.
- [ ] An algorithm makes a slow program run fast.
- [ ] An algorithm deals with computer hardware, a program deals with computer software.

**2. True or False? A computational mode of thinking means that everything can be viewed as a math problem involving numbers and formulas.**
- [x] ***True***
- [ ] False


**3. True or False? Computer Science is the study of how to build efficient machines that run programs.**
- [ ] True
- [x] ***False***

**4. The two things every computer can do are:**
- [x] Perform calculations
- [ ] Convert electricity to numbers
- [ ] Display results to a screen
- [x] Remember the results


### Exercises 2
3/3 points (graded)

**1. True or False? Declarative knowledge refers to statements of fact.**
- [x] ***True***
- [ ] False

**2. True or False? Imperative knowledge refers to 'how to' methods.**
- [x] ***True***
- [ ] False

**3. True or False? A recipe for deducing the square root involves guessing a starting value for y. Without another recipe to be told how to pick a starting number, the computer cannot generate one on its own.**
- [x] ***True***
- [ ] False


### Exercises 3
5/5 points (graded)

**1. True or False? A stored program computer is designed to compute precisely one computation, such as a square root, or the trajectory of a missile.**
- [ ] True
- [x] False

**2. True or False? A fixed program computer is designed to run any computation, by interpreting a sequence of program instructions that are read into it.**
- [ ] True
- [x] False

**3. A program counter**
- [ ] counts the number of primitive operations executed by the program.
- [ ] counts the number of primitive operations comprising a complex operation.
- [x] points the computer to the next instruction to execute in the program.
- [ ] remembers how many times a program has been executed.

**4. What does it mean when we say that "the computer walks through the sequence executing some computation"?**
- [ ] The computer tests each instruction to ensure it will not harm the circuitry.
- [ ] The computer executes the instructions in strict, linear sequence, just like walking in a straight line.
- [x] The computer executes the instructions mostly in a linear sequence, except sometimes it jumps to a different place in the sequence.
- [ ] The computer slowly executes instructions so that we can follow its progress, rather than running a program at full speed.

**5. True or False? In order to compute everything that is computable, every computer must be able to handle the sixteen most primitive operations.**
- [ ] True
- [x] False


### Exercises 4
3/3 points (graded)

Choose the term described by each of the following definitions.

Definitions:
**1. Determines whether a string is legal**
- [ ] Semantics
- [ ] Static semantics
- [x] Syntax

**2. Determines whether a string has meaning**
- [ ] Semantics
- [x] Static semantics
- [ ] Syntax

**3. Assigns a meaning to a legal sentence**
- [x] Semantics
- [ ] Static semantics
- [ ] Syntax


### Exercise 5
5/5 points (graded)

For each of the following expressions, indicate the type of the expression. While you could simply type these expressions into your shell, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

`Note: The Python 'None' keyword`

* 3.14
- [ ] NoneType
- [ ] int
- [x] float
- [ ] bool

* 34
- [ ] NoneType
- [x] int
- [ ] float
- [ ] bool


* True
- [ ] NoneType
- [ ] int
- [ ] float
- [x] bool

* None
- [x] NoneType
- [ ] int
- [ ] float
- [ ] bool

* 3.0
- [ ] NoneType
- [ ] int
- [x] float
- [ ] bool


### Exercise 6
10/10 points (graded)

For each of the following expressions, indicate the value returned, or if the evaluation would lead to an error, write the word 'error' (note this is a word, not a string, no quotes). While you could simply type these expressions into an IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

For decimal answers, give the full result, or four decimal places of accuracy (whichever is shortest).

`Floating point errors`
* `6 + 12 -3`: `15`
* `2 * 3.0`: `6.0`
* `- - 4`: `4`
* `10/3`: `3.3333`
* `10.0/3.0`: `3.3333`
* `(2 + 3) * 4`: `20`
* `2 + 3 * 4`: `14`
* `2**3 + 1`: `9`
* `2.1 ** 2.0`: `4.41`
* `2.2 * 3.0`: `6.6000`


### Exercise 7
6/6 points (graded)

Below is a transcript of a session with the Python shell. For each expression being evaluated, provide the type and the value the expression returns. If evaluating an expression would cause an error, select 'NoneType' and write the word 'error' (note this is a word, not a string, no quotes) in the box. While you could simply type these expressions into your IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

Assume that the expressions are evaluated in the order shown - that is, each problem part is evaluated directly after the previous problem part(s).

1. 
```
>>> a = 3
>>> a + 2.0 
```
- [ ] NoneType
- [ ] int
- [x] float
- [ ] bool

`5.0`

2. 
```
>>> a = a + 1.0
>>> a
```
- [ ] NoneType
- [ ] int
- [x] float
- [ ] bool

`4.0`

3. 
```
>>> a = 3
>>> b
```
- [ ] NoneType
- [ ] int
- [x] float
- [ ] bool

`error` (as this gives you `NameError: name 'b' is not defined`)


### Exercise 8
12/12 points (graded)

For each of the following expressions, indicate the value returned, or if the evaluation would lead to an error, write the word 'error' (note this is a word, not a string, no quotes). While you could simply type these expressions into your IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

<details>
<summary>Hint: Python boolean types</summary>
<br>
Remember that in Python words are case-sensitive. The word `True` is a Python keyword (it is the value of the Boolean type) and is not the same as the word `true`. Refer to the Python documentation on Boolean values https://docs.python.org/3/library/stdtypes.html#boolean-values
</details>


<details>
<summary>Hint: Priority order of Boolean operations</summary>
<br>
For these problems, it's important to understand the priority of Boolean operations. The order of operations is as follows:

1. Parentheses. Before operating on anything else, Python must evaluate all parentheticals starting at the innermost level.

2. `not` statements.

3. `and` statements.

4. `or` statements.

What this means is that an expression like

`not True and False`
  
evaluates to `False`, because the `not` is evaluated first (`not True` is `False`), then the `and` is evaluated, yielding `False and False` which is `False`.

However the expression

`not (True and False)`
  
evaluates to `True`, because the expression inside the parentheses must be evaluated first - `True and False` is `False`. Next the `not` can be evaluated, yielding `not False` which is `True`.

Overall, you should always use parenthesis when writing expressions to make it clear what order you wish to have Python evaluate your expression. As we've seen here, `not (True and False)` is different from `(not True) and False` - but it's easy to see how Python will evaluate it when you use parentheses. A statement like `not True and False` can bring confusion!
</details>


* `3 > 4`: `False`
* `4.0 > 3.999`: `True`
* `4 > 4`: `False`
* `4 > + 4`: `False`
* `2 + 2 == 4`: `True`
* `True or False`: `True`
* `False or False`: `False`
* `not False`: `True`
* `3.0 - 1.0 != 5.0 - 3.0`: `False`
* `3 > 4 or (2 < 3 and 9 > 10)`: `False`
* `4 > 5 or 3 < 4 and 9 > 8`: `True`
* `not(4 > 3 and 100 > 6)`: `False`


### Exercise 9
4/4 points (graded)

Below is a transcript of a session with the Python shell. For each expression being evaluated, provide the type and the value that the last expression in the transcript returns. If evaluating an expression would cause an error, select 'NoneType' and write the word 'error' (note this is a word, not a string, no quotes) in the box. While you could simply type these expressions into your IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

Assume that the expressions are evaluated in the order shown - that is, each problem part is evaluated directly after the previous problem part(s).

1. 
```
>>> a = 3
>>> a == 5.0
>>> a 
```
- [ ] NoneType
- [x] int `3`
- [ ] float
- [ ] bool

2.
```
>>> b = 10
>>> c = b > 9
>>> c 
```
- [ ] NoneType
- [ ] int
- [ ] float
- [x] bool `True`


### Exercise 10
16/16 points (graded)

For each of the following expressions, indicate the type of the expression and the value returned, or, if the evaluation would lead to an error, choose the type 'NoneType' and write the word 'error' (note this is a word, not a string, no quotes) as the value returned.

While you could simply type these expressions into your IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

* `3 + 5.0`
- [ ] NoneType
- [ ] int
- [x] float `8.0`
- [ ] bool

* `5/2`
- [ ] NoneType
- [ ] int
- [x] float `2.5`
- [ ] bool

* `5/2 == 5/2.0`
- [ ] NoneType
- [ ] int
- [ ] float
- [x] bool `True`

* `5/2.0`
- [ ] NoneType
- [ ] int
- [x] float `2.5`
- [ ] bool

* `round(2.6)`
- [ ] NoneType
- [x] int `3`
- [ ] float
- [ ] bool

* `int(2.6)`
- [ ] NoneType
- [x] int `2`
- [ ] float
- [ ] bool

* `2.0 + 5.0`
- [ ] NoneType
- [ ] int
- [x] float `7.0`
- [ ] bool

* `5*2 == 5.0 * 2.0`
- [ ] NoneType
- [ ] int
- [ ] float
- [x] bool `True`


## 2. Core Elements of Programs


# Unit 2: dummy
