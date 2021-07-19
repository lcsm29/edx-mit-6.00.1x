# Table of Contents
- [Unit 1: Python Basics, Incomplete section](#unit-1-python-basics-incomplete-section)
  * [Lecture 1. Introduction to Python](#lecture-1-introduction-to-python)
  * [Lecture 2. Core Elements of Programs](#lecture-2-core-elements-of-programs)
- [Unit 2: Simple Programs](#unit-2-simple-programs)
  * [Lecture 3. Simple Algorithms](#lecture-3-simple-algorithms)
  * [Lecture 4. Functions](#lecture-4-functions)
- [Unit 3: Structured Programs](#unit-3-structured-programs)
  * [Lecture 5. Tuples and Lists](#lecture-5-tuples-and-lists)
  * [Lecture 6. Dictionaries](#lecture-6-dictionaries)
- [Unit 4: Good Programming Practices](#unit-4-good-programming-practices)
  * [Lecture 7. Testing and Debugging](#lecture-7-testing-and-debugging)
  * [Lecture 8. Exceptions and Assertions](#lecture-8-exceptions-and-assertions)
- [Unit 5: Object Oriented Programming](#unit-5-object-oriented-programming)
  * [Lecture 9. Classes and Inheritance](#lecture-9-classes-and-inheritance)
  * [Lecture 10. An Extended Example](#lecture-10-an-extended-example)
- [Unit 6: Algorithmic Complexity](#unit-6-algorithmic-complexity)
  * [Lecture 11. Computational Complexity](#lecture-11-computational-complexity)
  * [Lecture 12. Searching and Sorting Algorithms](#lecture-12-searching-and-sorting-algorithms)
- [Unit 7: Plotting and Final Thoughts](#unit-7-plotting-and-final-thoughts)
  * [Lecture 13. Visualization of Data](#lecture-13-visualization-of-data)
  * [Lecture 14. Summary](#lecture-14-summary)


# Unit 1: Python Basics, Incomplete section

## Lecture 1. Introduction to Python
* [Lecture 1. Introduction to Python](#lecture-1-introduction-to-python)    
  + [Exercise 1](#exercise-1)
  + [Exercise 2](#exercise-2)
  + [Exercise 3](#exercise-3)
  + [Exercise 4](#exercise-4)
  + [Exercise 5](#exercise-5)
  + [Exercise 6](#exercise-6)
  + [Exercise 7](#exercise-7)
  + [Exercise 8](#exercise-8)
  + [Exercise 9](#exercise-9)
  + [Exercise 10](#exercise-10)
### Exercise 1
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

### Exercise 2
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

### Exercise 3
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

### Exercise 4
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

<details>
<summary>Note: The Python 'None' keyword</summary>
<br>

In Python, the keyword None is frequently used to represent the absence of a value. None is the only value in Python of type NoneType.
</details>

* `3.14`: float
* `34`: int
* `True`: bool
* `None`: NoneType
* `3.0`: float

### Exercise 6
10/10 points (graded)

For each of the following expressions, indicate the value returned, or if the evaluation would lead to an error, write the word 'error' (note this is a word, not a string, no quotes). While you could simply type these expressions into an IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

For decimal answers, give the full result, or four decimal places of accuracy (whichever is shortest).

<details>
<summary>Floating point errors</summary>
<br>
Decimal numbers cannot be stored exactly in the computer because the computer does not have an infinite amount of memory. So decimal numbers are rounded when stored. When you do calculations with these numbers, your final result will be different than the actual result. For example, you may get something like 5.0000000044 instead of 5.0. This is called floating-point rounding error.
</details>

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

1. float `5.0`
```
>>> a = 3
>>> a + 2.0 
```
2. float `4.0`
```
>>> a = a + 1.0
>>> a
```
3. NoneType `error` (as this gives you `NameError: name 'b' is not defined`)
```
>>> a = 3
>>> b
```

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

1. int `3`
```
>>> a = 3
>>> a == 5.0
>>> a 
```
2. bool `True`
```
>>> b = 10
>>> c = b > 9
>>> c 
```

### Exercise 10
16/16 points (graded)

For each of the following expressions, indicate the type of the expression and the value returned, or, if the evaluation would lead to an error, choose the type 'NoneType' and write the word 'error' (note this is a word, not a string, no quotes) as the value returned.

While you could simply type these expressions into your IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

* `3 + 5.0`: float `8.0`
* `5/2`: float `2.5`
* `5/2 == 5/2.0`: bool `True`
* `5/2.0`: float `2.5`
* `round(2.6)`: int `3`
* `int(2.6)`: int `2`
* `2.0 + 5.0`: float `7.0`
* `5*2 == 5.0 * 2.0`: bool `True`


## Lecture 2. Core Elements of Programs
* [Lecture 2. Core Elements of Programs](#lecture-2-core-elements-of-programs)
  + [Exercise 1](#exercise-1-1)
  + [Exercise 2](#exercise-2-1)
    - [Exercise 2 part 1](#exercise-2-part-1)
    - [Exercise 2 part 2](#exercise-2-part-2)
    - [Exercise 2 part 3](#exercise-2-part-3)
    - [Exercise 2 part 4](#exercise-2-part-4)
  + [Exercise 3](#exercise-3-1)
  + [Exercise: hello world](#exercise-hello-world)
  + [Exercise: happy](#exercise-happy)
  + [Exercise 4](#exercise-4-1)
  + [Exercise: while](#exercise-while)
    - [Exercise: while exercise 1](#exercise-while-exercise-1)
    - [Exercise: while exercise 2](#exercise-while-exercise-2)
    - [Exercise: while exercise 3](#exercise-while-exercise-3)
  + [Exercise: for](#exercise-for)
    - [Exercise: for exercise 1](#exercise-for-exercise-1)
    - [Exercise: for exercise 2](#exercise-for-exercise-2)
    - [Exercise: for exercise 3](#exercise-for-exercise-3)
  + [Exercise 5](#exercise-5-1)
  + [Exercise 6](#exercise-6-1)
  + [Exercise 7](#exercise-7-1)

### Exercise 1
7/7 points (graded)

For each of the following expressions, indicate the value returned, or if the evaluation would lead to an error, write the word 'error' (note this is a word, not a string, no quotes). While you could simply type these expressions into your IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

<details>
<summary>Note: Advanced String Slicing</summary>
<br>

You've seen in lecture that you can slice a string with a call such as `s[i:j]`, which gives you a portion of string `s` from index `i` to index `j-1`. However this is not the only way to slice a string! If you omit the starting index, Python will assume that you wish to start your slice at index 0. If you omit the ending index, Python will assume you wish to end your slice at the end of the string. Check out this session with the Python shell:
```
>>> s = 'Python is Fun!'
>>> s[1:5]
'ytho'
>>> s[:5]
'Pytho'
>>> s[1:]
'ython is Fun!'
>>> s[:]
'Python is Fun!'
```
That last example is interesting! If you omit both the start and ending index, you see your original string!

There's one other cool thing you can do with string slicing. You can add a third parameter, `k`, like this: `s[i:j:k]`. This gives a slice of the string `s` from index `i` to index `j-1`, with step size `k`. Check out the following examples:
```
>>> s = 'Python is Fun!'
>>> s[1:12:2]
'yhni u'
>>> s[1:12:3]
'yoiF'
>>> s[::2]
'Pto sFn'
```
The last example is similar to the example `s[:]`. With `s[::2]`, we're asking for the full string `s` (from index 0 through 13), with a step size of 2 - so we end up with every other character in `s`. Pretty cool!
</details>

* `"a" + "bc"`: `'abc'`
* `3 * "bc"`: `bcbcbc`
* `"3" * "bc"`: `error` (TypeError: can't multiply sequence by non-int of type 'str')
* `"abcd"[2]`: `'c'`
* `"abcd"[0:2]`: `'ab'`
* `"abcd"[:2]`: `'ab'`
* `"abcd"[2:]`: `'cd'`


### Exercise 2
NOTE: These exercises are ungraded.

#### Exercise 2 part 1

For each of the expressions below, specify its type and value. If it generates an error, select type 'NoneType' and write the word 'error' (note this is a word, not a string, no quotes) in the box for the value. While you could simply type these expressions into your IDE, we encourage you to answer them directly since this will help reinforce your understand of basic Python expressions.

Assume we've made the following assignments:

```
> str1 = 'hello'
> str2 = ','
> str3 = 'world'
```
<details>
<summary>Note: The Python 'in' operator</summary>
<br>

The operators `in` and `not in` test for collection membership (a 'collection' refers to a string, list, tuple or dictionary - don't worry, we will cover lists, tuples and dictionaries soon!). The expression
```
element in coll
```
evaluates to `True` if `element` is a member of the collection `coll`, and `False` otherwise.

The expression
```
element not in coll
```
evaluates to `True` if element is `not` a member of the collection `coll`, and `False` otherwise.

Note this returns the negation of `element in coll` - that is, the expression `element not in coll` is equivalent to the expression `not (element in coll)`.
</details>

1. `str1`: string `'hello'`
2. `str1[0]`: string `'h'`
3. `str1[1]`: string `'e'`
4. `str1[-1]`: string `'o'`
5. `len(str1)`: int `5`

#### Exercise 2 part 2
```
> str1 = 'hello'
> str2 = ','
> str3 = 'world'
```
1. `str1[len(str1)]`: NoneType `error` (IndexError: string index out of range)
2. `str1 + str2 + str3`: string `'hello,world'`
3. `str1 + str2 + ' ' + str3`: string `'hello, world'`
4. `str3 * 3`: string `'worldworldworld'`
5. `'hello' == str1`: boolean `True`

#### Exercise 2 part 3
```
> str1 = 'hello'
> str2 = ','
> str3 = 'world'
```
1. `'HELLO' == str1`: boolean `False`
2. `'a' in str3`: boolean `False`
3. boolean `True`
```
str4 = str1 + str3
'low' in str4
```
4. `str3[1:3]`: string `'or'`
5. `str3[:3]`: string `'wor'`

#### Exercise 2 part 4
```
> str1 = 'hello'
> str2 = ','
> str3 = 'world'
> str4 = str1 + str3
```
1. `str3[:-1]`: string `'worl'`
2. `str1[1:]`: string `'ello'`
3. `str4[1:9]`: string `'elloworl'`
4. `str4[1:9:2]`: - string `'elwr'`
5. `str4[::-1]`: string `'dlrowolleh'`

### Exercise 3

For each of the following expressions, indicate the value that prints out when the expression is evaluated. If the evaluation would lead to an error, write the word 'error'; if nothing would print out, write the word 'blank'.

While you could simply type these expressions into your IDE, we encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

If the temperatures seem weird to you, like most of the world, you probably use the Celsius system. We Americans still use the crazy [Fahrenheit system...](https://www.fahrenheittocelsius.com/)

1. `blank`
```python:
if 6 > 7:
   print("Yep")
```

2. `Nope`
```python:
if 6 > 7:
   print("Yep")
else:
   print("Nope")
```

3. `Regal!`
```python:
var = 'Panda'
if var == "panda":
   print("Cute!")
elif var == "Panda":
   print("Regal!")
else:
   print("Ugly...")
```

4. `Hot`
```python:
temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable") 
else:
   print("Cold")
```

5. `Cold`
```python:
temp = 50
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable")
else:
   print("Cold")
```

### Exercise: hello world
5.0/5.0 points (graded)

Write a piece of Python code that prints out the string hello world
```python:
print('hello world')
```


### Exercise: happy
5.0/5.0 points (graded)

Write a piece of Python code that prints out the string 'hello world' if the value of an integer variable, happy, is strictly greater than 2.
```python:
if happy > 2:
    print('hello world')
```
* Note: `print('hello world' if happy > 2 else '')` would be considered as incorrect on auto grader, because it prints a blank line when `happy <= 2`


### Exercise 4
5/5 points (graded)

Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

This question is going to ask you what some simple loops print out. If you're asked what code like this prints:
```python:
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)
```
write what it prints out, separating what appears on a new line by a comma and a space. So the answer for the above code would be:
```
5, 4
```
If a given loop will not terminate, write the phrase 'infinite loop' (no quotes) in the box. Recall that you can stop an infinite loop in your program by typing CTRL+c in the console.

<details>
<summary>Note: What does +=, -=, *=, /= stand for?</summary>
<br>

`a += b` is equivalent to `a = a + b`

`a -= b` is equivalent to `a = a - b`

`a *= b` is equivalent to `a = a * b`

`a /= b` is equivalent to `a = a / b`
</details>

1. `0, 1, 2, 3, 4, 5, Outside of loop, 6`
```python:
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 
```

2. `infinite loop`
```python:
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
```

3. `9, 8, 7, 6, 5, 4, 3`
```python:
num = 10
while num > 3:
    num -= 1
    print(num) 
```

4. `10, 9, 8, 7, Breaking out of loop, Outside of loop`
```python:
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')
```

5. `num is: 100`
```python:
num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))
```

### Exercise: while

#### Exercise: while exercise 1
5.0/5.0 points (graded)

In this problem you'll be given a chance to practice writing some while loops.

Convert the following into code that uses a while loop.
```
prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
```
```python:
n = 2
while n <= 10:
    print(n)
    n += 2
print('Goodbye!')
```

#### Exercise: while exercise 2
5.0/5.0 points (graded)

Convert the following into code that uses a while loop.
```
prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
```
```python:
n = 10
print('Hello!')
while n:
    print(n)
    n -= 2
```

#### Exercise: while exercise 3
5.0/5.0 points (graded)

Write a while loop that sums the values 1 through `end`, inclusive. `end` is a variable that we define for you. So, for example, if we define `end` to be 6, your code should print out the result: 
```
21
```
which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include ```input``` statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

<details>
<summary>Hint: Don't Use A Variable Called 'sum'</summary>
<br>

For reasons related to our grader, you cannot call your variable `sum`. Call it anything else, but not `sum`. If you do, you will be marked incorrectly.

This is because `sum` is a Python built-in function for summing a list of numbers – we prevent you from using it because if you did it'd defeat the point of the exercise.

Take it as a lesson – overwriting built-in functions is generally bad practice anyway (you'd not call a variable `print`, or `while` or `elif` - because if you did, how would you use those built-in functions/keywords?). A general rule of thumb is: when writing code in Idle, if a word turns orange or purple, then it is special in Python - it is either a keyword or a built in function. In Canopy, the color is green. Don't give your variables the same name as any of the Python keywords or built in functions.

Here is a [list of Python keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

Here is a [list of Python built-in functions](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

You will learn more about functions in the next lecture sequence!
</details>

```python:
s = 0
while end:
    s += end
    end -= 1
print(s)
```

### Exercise: for
5.0/5.0 points (graded)

#### Exercise: for exercise 1
Convert the following code into code that uses a for loop.
```
prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
```
```python:
for i in range(2, 11, 2):
    print(i)
print('Goodbye!')
```

#### Exercise: for exercise 2
5.0/5.0 points (graded)

Convert the following into code that uses a while loop.
```
prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
```
```python:
print('Hello!')
for i in range(10, 1, -2):
    print(i)
```

#### Exercise: for exercise 3
5.0/5.0 points (graded)

Write a while loop that sums the values 1 through `end`, inclusive. `end` is a variable that we define for you. So, for example, if we define `end` to be 6, your code should print out the result: 
```
21
```
which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include ```input``` statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

```python:
a = 0
for i in range(1, end + 1):
    a += i
print(a)
```

### Exercise 5
5/5 points (graded)

Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

This question is going to ask you what some simple loops print out. If you're asked what code like this prints:
```
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)
```
write what it prints out, separating what appears on a new line by a comma and a space. So the answer for the above code would be:
```
5, 4
```
If a given loop will not terminate, write the phrase 'infinite loop' in the box.

1. `0, 1, 2, 3, 4, 4`
```
num = 10
for num in range(5):
    print(num)
print(num)
```

2. `0.0, 1.0, 2.0, 3.0, 4.0`
```
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
```

3. `0, Foo!, 4, 8, 12, 16, Foo!`
```
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
```

4. `h, o, l, a`
```
for letter in 'hola':
    print(letter)  
```

5. `Letter # 0 is S, 1`
```
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)
```

### Exercise 6

15/15 points (graded)

Below are some short Python programs. For each program, answer the associated questions.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong. You'll learn the most this way, by figuring things out, instead of just running the code and reading off the answers.

* 1.
```python:
myStr = '6.00x'

for char in myStr:
    print(char)

print('done')
```
1. How many times does `6` print out? `1`
2. How many times does `.` print out? `1`
3. How many times does `0` print out? `2`
4. How many times does `x` print out? `1`
5. How many times does `done` print out? `1`

* 2.
```python:
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')
```
1. How many times does `H` print out? `1`
2. How many times does `e` print out? `2`
3. How many times does `l` print out? `3`
4. How many times does `o` print out? `1`
5. How many times does `!` print out? `2`
6. How many times does `done` print out? `1`

* 3. 
```python:
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
```
1. How many times does `o` print out? Disregard the `o`'s in last two print statements. `0`
2. How many times does `M` print out? `1`
3. What will the value of the variable `numVowels` be? `11`
4. What will the value of the variable `numCons` be? `-25`

### Exercise 7
5/5 points (graded)

Here is some code:

**Code Sample**
```
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
```
We wish to re-write the above code, but instead of nesting a for loop inside a while loop, we want to nest a while loop inside a for loop. Which of the following loops gives the same output as the **Code Sample**?

Try to answer the following questions by just reading the code. Reading code is a very good skill to have (and will help you both in your programming career and on your exams!). It is okay to check your answers that you obtain from just reading the code, then in your interpreter run the code for the ones you got wrong on your first attempt.

Test 1
```
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
```
- [x] No, Test 1 does not give the same output as the Code Sample

Test 2
```
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break
```
- [x] No, Test 2 does not give the same output as the Code Sample

Test 3
```
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
```
- [x] Yes, Test 3 gives the same output as the Code Sample

Test 4
```
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
```
- [x] Yes, Test 4 gives the same output as the Code Sample

Test 5
```
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
```
- [x] Yes, Test 5 gives the same output as the Code Sample


# Unit 2: Simple Programs

## Lecture 3. Simple Algorithms
* [Lecture 3. Simple Algorithms](#lecture-3-simple-algorithms)
  + [Exercise 1](#exercise-1-2)
  + [Exercise 2](#exercise-2-2)
  + [Exercise: guess my number](#exercise-guess-my-number)
  + [Exercise 3](#exercise-3-2)
### Exercise 1
14/14 points (graded)

Below are some short Python programs. For each program, answer the associated questions.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

* 1.
```
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
```
1. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 0? `12`
2. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 1? `24`
3. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 2? `36`
4. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 3? `48`
5. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 4? `60`

* 2.
```
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
```
1. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 0? `12`
2. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 1? `12`
3. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 2? `12`
4. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 3? `12`
5. What is the value of the variable `count` that is printed out (at the `print` statement) on iteration 4? `12`

* 3.
```
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
```
1. How many times will the `print` statement be executed? `5`
2. What is the largest value of the variable `iteration` that will be printed out (at the `print` statement)? `4`
3. What is the largest value of the variable `count` that will be printed out (at the `print` statement)? `12`
4. What is the smallest value of the variable `count` that will be printed out (at the `print` statement)? `1`

### Exercise 2
3/3 points (graded)

Consider the following code:
```
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
```
If this code is executed, it will print `succeeded: 4.9999999999998` (or `succeeded: 5.0`). Remember floating point errors?

Now suppose we try the following:
```
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
```
Select the answer that best describes what occurs when the above code is executed:
- [ ] Script successfully completes, and prints out `succeeded: 4.9999999999998` (or `succeeded: 5.0`)
- [ ] Script successfully completes, but prints out `failed`
- [ ] Script successfully completes, but prints out `succeeded:` followed by some number not really close to 5.0
- [x] Script enters an infinite loop and never terminates

Now suppose we try the following:
```
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
```
Select the answer that best describes what occurs when the above code is executed:
- [x] Script successfully completes, and prints out `succeeded: 4.9999999999998` (or `succeeded: 5.0`)
- [ ] Script successfully completes, but prints out `failed`
- [ ] Script successfully completes, but prints out `succeeded:` followed by some number not really close to 5.0
- [ ] Script enters an infinite loop and never terminates

Finally, let's use the same code as immediately above, but change the first line to x = 23. Note that the square root of 23 is roughly 4.7958.

Select the answer that best describes what occurs when the modified code is executed:
- [ ] Script successfully completes, and prints out `succeeded: 4.9999999999998` (or `succeeded: 5.0`)
- [x] Script successfully completes, but prints out `failed`
- [ ] Script successfully completes, but prints out `succeeded:` followed by some number not really close to 5.0
- [ ] Script enters an infinite loop and never terminates

### Exercise: guess my number
10.0/10.0 points (graded)

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:
```
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83
```
<details>
<summary>Hint: Endpoints</summary>
<br>

** Your program should use bisection search. So think carefully what that means. What will the first guess always be? How should you calculate subsequent guesses?

** Your initial endpoints should be 0 and 100. Do not optimize your subsequent endpoints by making them be the halfway point plus or minus 1. Rather, just make them be the halfway point.
</details>
<details>
<summary>Python Trick: Printing on the same line</summary>
<br>
Try the following in your console:

```
# Notice how if we have two print statements
print("Hi")
print("there")

# The output will have each string on a separate line:
Hi
there

# Now try adding the following:
print("Hi",end='')
print("there")
print("Hi",end='*')
print("there")

# The output will place the subsequent string on the same line
# and will connect the two prints with the character given by end
Hithere
Hi*there
```
</details>
<details>
<summary>Click to See Test Cases</summary>
<br>

Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Test case 1. Secret guess = 42
```
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 25?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 37?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 43?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 40?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 41?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 42?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 42
```
Test case 2. Secret guess = 91
```
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 93?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 90?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 91
```
</details>

Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input. For example:
```
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
```

```python:
print('Please think of a number between 0 and 100!')
l, h, user_input = 0, 100, ''
txt = ('''Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ''')
while user_input != 'c':
    m = (l + h) // 2
    user_input = ''
    while 1:
        print('Is your secret number {}?'.format(m))
        user_input = input(txt)
        if user_input in ('l', 'h', 'c'): break
        else: print('Sorry, I did not understand your input.')
    if user_input == 'h': h, m = m, (l + m) // 2
    elif user_input == 'l': l, m = m, (h + m) // 2
    else: print('Game over. Your secret number was:', m)
```
### Exercise 3
4/4 points (graded)

1. True or False? The internal computer representation of any number is always an approximation. `False`
2. The decimal 11 is what binary?: `1011`
3. True or False? The internal representation of the decimal number 1/10 = 0.1 requires an infinite number of digits. `True`
4. After many computations, you get two floating numbers stored in variables `a` and `b`. Your code compares the numbers with `a == b`. `Doing the comparison will sometimes lead to a correct program.`


## Lecture 4. Functions
* [Lecture 4. Functions](#lecture-4-functions)
  + [Exercise 1](#exercise-1-3)
  + [Exercise: square](#exercise-square)
  + [Exercise: eval quadratic](#exercise-eval-quadratic)
  + [Exercise 2](#exercise-2-3)
  + [Exercise 3](#exercise-3-3)
  + [Exercise 4](#exercise-4-2)
  + [Exercise 5](#exercise-5-2)
  + [Exercise 6](#exercise-6-2)
  + [Exercise: fourth power](#exercise-fourth-power)
  + [Exercise: odd](#exercise-odd)
  + [Exercise: power iter](#exercise-power-iter)
  + [Exercise: power recur](#exercise-power-recur)
  + [Exercise: gcd iter](#exercise-gcd-iter)
  + [Exercise: gcd recur](#exercise-gcd-recur)
  + [Exercise: as in](#exercise-as-in)
  + [Exercise 7](#exercise-7-2)
### Exercise 1
6/6 points (graded)

#### Part1: Function Types
For each of the following functions, specify the type of its return. You can assume each function is called with an appropriate argument, as specified by its docstring.

If the output can be either an int or a float, select num, which isn't a real Python type, but which we'll use to indicate that either basic numeric type is legal.

In fact, in Python, booleans True and False can be operated on as if they were the integers 1 and 0; but it is ugly and confusing to take advantage of this fact, and we will resolutely pretend that it isn't true.
<details>
<summary>What are those lines under the function definitions?</summary>
<br>
In this and future problems, you'll see function definitions that look like this:

```
def a(x):
   '''
   x: int or float.
   '''
   return x + 1
```
What are those three lines between `def a(x):` and `return x + 1`? These lines are called the docstring of the function. A docstring is a special type of comment that is used to document what your function is doing. Typically, docstrings will explain what the function expects the type(s) of the argument(s) to be, and what the function is returning.

In Python, docstrings appear immediately after the `def` line of a function, before the body. Docstrings start and end with triple quotes - this can be triple single quotes or triple double quotes, it doesn't matter as long as they match. To sum up this general form:
```
def my_function(argument):
   """
   Docstring goes here. Explain what type argument(s) should have, and what your function
   is going to return.
   """
   < Code for your function (the body of the function) goes here >
```
As you begin coding your own functions, we strongly encourage you to document all your functions by using properly-formatted docstrings!
</details>

1. Indicate the type of the output that the function `a` will yield. `num`
```
def a(x):
   '''
   x: int or float.
   '''
   return x + 1
```
2. Indicate the type of the output that the function `b` will yield. `float`
```
def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
```
3. Indicate the type of the output that the function `c` will yield. `num`
```
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y
```
4. Indicate the type of the output that the function `d` will yield. `boolean`
```
def d(x, y):
   '''
   x: Can be int or float.
   y: Can be int or float.
   '''
   return x > y
```
5. Indicate the type of the output that the function `e` will yield. `boolean`
```
def e(x, y, z):
   '''
   x: Can be int or float.
   y: Can be int or float.
   z: Can be int or float.
   '''
   return x >= y and x <= z
```
6. Indicate the type of the output that the function `f` will yield. `NoneType`
```
def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
```

### Exercise: square
5/5 points (graded)

Write a Python function, `square`, that takes in one number and returns the square of that number.

This function takes in one number and returns one number.

```python:
def square(x):
    '''
    x: int or float.
    '''
    return x ** 2
```
### Exercise: eval quadratic
5/5 points (graded)

Write a Python function, `evalQuadratic(a, b, c, x)`, that returns the value of the quadratic <img src="https://render.githubusercontent.com/render/math?math=\color{white}ax^2 %2B bx %2B c">

This function takes in four numbers and returns a single number.
```python:
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b * x + c
```

### Exercise 2
14/14 points (graded)

You have the following function definitions:
```
def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2    
```
Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the value of an expression is a function, select function as the type and write 'function' in the box.

1. `a(6)`: `int`, `7`
2. `a(-5.3)`: `float`, `-4.3`
3. `a(a(a(6)))`: `int`, `9`
4. `c(a(1), b(1))`: `float`, `4.0`
5. `d('apple', 11.1)`: `NoneType`, `error`
6. `e(a(3), b(4), c(3, 4))`: `boolean`, `False`
7. `f`: `function`, `function`

### Exercise 3
8/8 points (graded)

Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the result is a function, select function and write 'function' in the box. As always, try to do this problem by hand before turning to your interpreter.

Assume the following definitions have been made:
```
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
```
1. `a(False, 2, 3)`: `int`, `3`
2. `b(3, 2)`: `int`, `3`
3. `a(3>2, a, b)`: `function`, `function`
4. `b(a, b)`: `NoneType`, `error`

### Exercise 4
4/4 points (graded)

Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the result is a function, select function and write 'function' in the box.

To get the most out of this problem, try to figure out the answers by reading the code, not running it. Run the code in your interpreter only after you've checked your answers a few times.

**Hint**: If you are confused, you may find it helpful to draw out an environment diagram similar to what was presented in lecture.
1. `int` `4`
```
>>> a = 10
>>> def f(x):
      return x + a
>>> a = 3
>>> f(1)
```

2. `int` `19`
```
>>> x = 12
>>> def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
>>> g(x)
```

### Exercise 5
4/4 points (graded)

Enter the value of the expressions below.

To get the most out of this problem, try to figure out the answers by reading the code, not running it. Run the code only after you've used up a few of your checks.

**Hint**: If you are confused, you may find it helpful to draw out an environment diagram similar to what was presented in lecture.

1. `11`
```
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3)
```

2. `1`
```
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)

foo(3, 0)
```

3. `5`
```
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)
```

4. `3`
```
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)
```

### Exercise 6
30/30 points (graded)

As we'll see in subsequent lectures, everything in Python is an object. Objects are special because we can associate special functions, referred to as object methods, with the object. In this problem you'll be working with string objects, and their built-in methods.

A complete description of the methods available to string objects can be found in the [Python library reference on string methods](http://docs.python.org/library/stdtypes.html#string-methods).

In this exercise, we want you to get some experience in using methods as functions. The convention for object methods is to use the "dot" notation, so that if s is a string, evaluating s.upper will return the actual function, and evaluating s.upper() will cause the function itself to be evaluated (in this case it returns a new string, since strings are immutable) with every character now in upper case. An example of this follows:
```
>>> s = 'abc'
>>> s.capitalize
<built-in method capitalize of str object at 0x104c35878>
>>> s.capitalize()
'Abc'
```
For each of the expressions in this problem, specify its type and value. If it generates an error, select type 'NoneType' and put the word 'error' in the box for the value. If it would be a function, select type 'function' and put the word 'function' in the box for the value.

Assume we've made the following assignments:
```
> str1 = 'exterminate!' 
> str2 = 'number one - the larch'
```
Assume that the expressions are evaluated in the order shown - that is, each problem part is evaluated directly after the previous problem part(s).
1. `str1.upper`: `function`, `function`
2. `str1.upper()`: `string`, `EXTERMINATE!`
3. `str1`: `string`, `exterminate!`
4. `str1.isupper()`: `boolean`, `False`
5. `str1.islower()`: `boolean`, `True`
6. `string`, `Number one - the larch`
```
str2 = str2.capitalize()
str2
```
7. `str2.swapcase()`: `string`, `nUMBER ONE - THE LARCH`
8. `str1.index('e')`: `int`, `0`
9. `str2.index('n')`: `int`, `8`
10. `str2.find('n')`: `int`, `8`
11. `str2.index('!')`: `NoneType`, `error`
12. `str2.find('!')`: `int`, `-1` (***Note***: Be sure to make note of the difference between the `find` and `index` string methods...)
13. `str1.count('e')`: `int`, `3`
14. `string`, `*xt*rminat*!`
```
str1 = str1.replace('e', '*')
str1
```
15. `str2.replace('one', 'seven')`: `string`, `Number seven - the larch`

### Exercise: fourth power
5.0/5.0 points (graded)

Write a Python function, `fourthPower`, that takes in one number and returns that value raised to the fourth power.

You should use the `square` procedure that you defined in an earlier exercise (you don't need to redefine `square` in this box; when you call `square`, the grader will use our definition).

This function takes in one number and returns one number.
```python:
def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))
```

### Exercise: odd
5.0/5.0 points (graded)

Write a Python function, `odd`, that takes in one number and returns `True` when the number is odd and `False` otherwise.

You should use the `%` (mod) operator, not `if`.

This function takes in one number and returns a boolean.
```python:
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x % 2 == 1
```

### Exercise: power iter
5.0/5.0 points (graded)

Write an iterative function iterPower(base, exp) that calculates the exponential <img src="https://render.githubusercontent.com/render/math?math=\color{white}base^{exp}"> by simply using successive multiplication. For example, `iterPower(base, exp)` should compute <img src="https://render.githubusercontent.com/render/math?math=\color{white}base^{exp}"> by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical value. Your code must be iterative - use of the `**` operator is not allowed.
```python:
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    answer = 1
    for _ in range(exp):
        answer *= base
    return answer
```
```python:
# The following one liner is not only extremely dirty but also extremely inefficient.
# But it works for any non-negative integer exponent.
# Requirements: Python 3.8+ (which means it won't pass the grader, since it's still on Python 3.5)
def iterPower(b, e, a=1, l=[1]): return [a:=a*n for n in l + [b for _ in range(e)]][e]
```
```python:
# The following one liner is written by one of the community TAs of the course, kiwitrader.
# This one passes the grader, but it's even slower than my already extremely inefficient one liner.
def iterPower(b, e): return eval('*'.join(str(b) for _ in range(e))) if e else 1
```

### Exercise: power recur
5.0/5.0 points (graded)

In Problem 1, we computed an exponential by iteratively executing successive multiplications. We can use the same idea, but in a recursive function.

Write a function `recurPower(base, exp)` which computes <img src="https://render.githubusercontent.com/render/math?math=\color{white}base^{exp}"> by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

This function should take in two values - `base` can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical value. Your code must be recursive - use of the `**` operator or looping constructs is not allowed.
```python:
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    return 1 if not exp else base * recurPower(base, exp - 1)
```
Note: In programming there are many ways to solve a problem. For your code to check correctly here, though, you must write your recursive function such that you make a recursive call directly to the function `recurPower`. Thank you for understanding.

Hints
<details>
<summary>What should your base case be?</summary>
<br>

To figure out what base case to use, think about what the smallest value of exp can be.
<details>
<summary>Smallest value of exp?</summary>
<br>

Recall that `exp` will be an integer greater than or equal to zero - so, the smallest value of `exp` is zero. What is the value of <img src="https://render.githubusercontent.com/render/math?math=\color{white}base^{exp}"> when `exp` equals zero, for any value of `base`?
</details>
</details>

<details>
<summary>Thinking about recursion</summary>
<br>

A good way to think about recursion is that recursion is the process of solving a given problem with a smaller instance of the same problem.

So, how could we express <img src="https://render.githubusercontent.com/render/math?math=\color{white}base^{exp}"> as a smaller instance of an exponential equation?
<details>
<summary>How to break down the equation</summary>
<br>

<img src="https://render.githubusercontent.com/render/math?math=\color{white}base^{exp}%20=%20base{\cdot}base^{exp-1}">

To convince yourself this is true, put in real numbers for `base` and `exp`; then, work through the recursion over and over until you reach your base case.
</details>
</details>


**If you are getting the error stating that "Your code should be recursive" when you already make a call to** `recurPower`: check your indention -- specifically, a common mistake is that your function and docstring do not start at the same indentation level.


### Exercise: gcd iter
5.0/5.0 points (graded)

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

* gcd(2, 12) = 2

* gcd(6, 12) = 6

* gcd(9, 12) = 3

* gcd(17, 12) = 1

Write an iterative function, `gcdIter(a, b)`, that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both `a` and `b` without remainder, or you reach 1.
```python:
from math import sqrt


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    def get_pfactors(num):
        def get_smallest_prime(num):
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0: return i
            return num
        factors = []
        prime, divided = 2, num
        while prime <= divided:
            prime = get_smallest_prime(divided)
            if prime <= divided:
                divided //= prime
                factors.append(prime)
        return factors
    
    def get_combs(factors_lst):
        def combs(factors_lst):
            if len(factors_lst) == 0:
                return [[]]
            combinations = []
            for c in combs(factors_lst[1:]):
                combinations += [c, c + [factors_lst[0]]]
            return combinations
        dirty_lst = combs(factors_lst)[1:]
        clean_lst = []
        for lst in dirty_lst:
            if lst not in clean_lst:
                clean_lst.append(lst)
        return clean_lst

    def get_divs(num, combs_lst):
        divisors = [1]
        for l in combs_lst:
            prd = 1
            for elem in l:
                prd *= elem
            divisors.append(prd)
        return divisors

    for a_div in reversed(get_divs(a, get_combs(get_pfactors(a)))):
        if b % a_div == 0:
            return a_div
 
```
### Exercise: gcd recur
5.0/5.0 points (graded)

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

* gcd(2, 12) = 2

* gcd(6, 12) = 6

* gcd(9, 12) = 3

* gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that `a` and `b` are two positive integers:

* If b = 0, then the answer is a

* Otherwise, gcd(a, b) is the same as gcd(b, a % b)

[See this website for an example of Euclid's algorithm being used to find the gcd.](https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example)

Write a function `gcdRecur(a, b)` that implements this idea recursively. This function takes in two positive integers and returns one integer.
```python:
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    return b if a == 0 else gcdRecur(b % a, a)
```

### Exercise: as in
5.0/5.0 points (graded)

We can use the idea of **bisection search** to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's `<` function.)

Implement the function `isIn(char, aStr)` which implements the above idea recursively to test if `char` is in `aStr`. `char` will be a single character and `aStr` will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.

```python:
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        return char == aStr
    else:
        m = len(aStr) // 2
        if aStr[m] == char:
            return True
        else:
            return isIn(char, aStr[:m]) if aStr[m] > char else isIn(char, aStr[m:])
```

Note: In programming there are many ways to solve a problem. For your code to check correctly here, though, you must write your recursive function such that you make a recursive call directly to the function `isIn`. Thank you for understanding.

Hints
<details>
<summary>Basic function structuring</summary>
<br>

Be very careful about how you slice the string in the recursive cases! Before you execute the recursive cases, you test the middle character - so if you reach the recursive cases, you know the middle character cannot be a match, right? So be careful to not include this character when you make your recursive call!
</details>
<details>
<summary>What should your base case be?</summary>
<br>

You should be thinking about 3 situations:
* What happens when the string is empty?
* What happens when the string is of length 1?
* What happens when the test character equals the middle character?
</details>
<details>
<summary>What should your recursive case be?</summary>
<br>

You should be thinking about 2 situations:
* What happens when the test character is smaller than the middle character?
* What happens when it is larger?
</details>

**If you are getting the error stating that "Your code should be recursive" when you already make a call to `isIn`**: check your indention -- specifically, a common mistake is that your function and docstring do not start at the same indentation level.
### Exercise 7
4/4 points (graded)

1. Assume the two files below are in the same folder. You run inventory.py. What happens?
- [x] prints `aa`
- [ ] prints `AA`
- [ ] There is an error.
<details>
<summary>batteries.py</summary>
<br>

```
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
```
</details>
<details>
<summary>inventory.py</summary>
<br>

```
aa = "aa"
tripleA = "aaa"
print(aa)
```
</details>

2. Assume the two files below are in the same folder. You run inventory.py. What happens?
- [ ] prints `aa`
- [ ] prints `AA`
- [x] There is an error.
<details>
<summary>batteries.py</summary>
<br>

```
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
```
</details>
<details>
<summary>inventory.py</summary>
<br>

```
aa = "aa"
tripleA = "aaa"
print(batteries.aa)
```
</details>

3. Assume the two files below are in the same folder. You run inventory.py. What happens?
- [ ] prints `aa`
- [x] prints `AA`
- [ ] There is an error.
<details>
<summary>batteries.py</summary>
<br>

```
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
```
</details>
<details>
<summary>inventory.py</summary>
<br>

```
import batteries
aa = "aa"
tripleA = "aaa"
print(batteries.aa)
```
</details>

4. Assume the two files below are in the same folder. You run inventory.py. What happens?
- [ ] prints `AA AAA C D`
- [ ] prints `aa aaa c d`
- [x] prints `aa AAA C D`
- [ ] There is an error.
<details>
<summary>batteries.py</summary>
<br>

```
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"
```
</details>
<details>
<summary>inventory.py</summary>
<br>

```
from batteries import *
aa = "aa"
print(aa, aaa, c, d)
```
</details>

# Unit 3: Structured Programs
## Lecture 5. Tuples and Lists

* [Lecture 5. Tuples and Lists](#lecture-5-tuples-and-lists)
  + [Exercise 1](#exercise-1-4)
  + [Exercise: odd tuples](#exercise-odd-tuples)
  + [Exercise 2](#exercise-2-4)
  + [Exercise 3](#exercise-3-4)
  + [Exercise 4](#exercise-4-3)
  + [Exercise: apply to each](#exercise-apply-to-each)
    - [Exercise: apply to each 1](#exercise-apply-to-each-1)
    - [Exercise: apply to each 2](#exercise-apply-to-each-2)
    - [Exercise: apply to each 3](#exercise-apply-to-each-3)
  + [Exercise 5](#exercise-5-3)

### Exercise 1
26/26 points (graded)

For each of the expressions below, specify its type and value. If it generates an error, select type 'NoneType' and put the word 'error' in the box for the value.

Assume we've made the following assignment:
```
x = (1, 2, (3, 'John', 4), 'Hi')
```
<details>
<summary>Hints: Single Element Tuples</summary>
<br>

When a tuple has only one element, you must specify it as follows: (elt,). Here is an example shell session that illustrates the difference:
```
>>> tup1 = (5)
>>> print(tup1)
5
>>> type(tup1)
<type 'int'>
>>> tup2 = (5,)
>>> print(tup2)
(5,)
>>> type(tup2)
<type 'tuple'>
```
</details>

* `x[0]`: `int`, `1`
* `x[2]`: `tuple`, `(3, 'John', 4)`
* `x[-1]`: `string`, `'Hi'`
* `x[2][2]`: `int`, `4`
* `x[2][-1]`: `int`, `4`
* `x[-1][-1]`: `string`, `'i'`
* `x[-1][2]`: `NoneType`, `error`
* `x[0:1]`: `tuple`, `(1,)`
* `x[0:-1]`: `tuple`, `(1, 2, (3, 'John', 4))`
* `len(x)`: `int`, `4`
* `2 in x`: `boolean`, `True`
* `3 in x`: `boolean`, `False`
* `x[0] = 8`: `NoneType`, `error`

### Exercise: odd tuples
5/5 points (graded)

Write a procedure called `oddTuples`, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple `('I', 'am', 'a', 'test', 'tuple')`, then evaluating `oddTuples` on this input would return the tuple `('I', 'a', 'tuple')`.
```python:
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return tuple([elem for i, elem in enumerate(aTup) if i % 2 == 0])

```

### Exercise 2
16/16 points (graded)

For each of the expressions below, specify its type and value. If it generates an error, select type 'NoneType' and put the word 'error' in the box for the value.

Assume we've made the following assignment:
```
x = [1, 2, [3, 'John', 4], 'Hi'] 
```
Additionally, assume that the expressions are evaluated in the order shown - that is, each problem part is evaluated directly after the previous problem part(s).

* `x[0]`: `int`, `1`
* `x[1]`: `list`, `[3, 'John', 4]`
* `x[-1]`: `string`, `'Hi'`
* `x[2][2]`: `int`, `4`
* `x[0:1]`: `list`, `[1]`
* `2 in x`: `boolean`, `True`
* `3 in x`: `boolean`, `False`
* `list`, `[8, 2, [3, 'John', 4], 'Hi']`
```
x[0] = 8
x
```

### Exercise 3
34/34 points (graded)

For each of the expressions below, specify its type and value. If it generates an error, select type 'NoneType' and put the word 'error' in the box for the value. If it would be a function, select type 'function' and put the word 'function' in the box for the value.

If the method returns None, select type 'NoneType' and put the word 'None' in the box for the value.

Assume we've made the following assignments:
```
> listA = [1, 4, 3, 0]
> listB = ['x', 'z', 't', 'q']
```

* `listA.sort`: `function`, `function`
* `listA.sort()`: `NoneType`, `None`
* `listA`: `list`, `[0, 1, 3, 4]`
* `listA.insert(0, 100)`: `NoneType`, `None`
* `listA.remove(3)`: `NoneType`, `None`
* `listA.append(7)`: `NoneType`, `None`
* `listA`: `list`, `[100, 0, 1, 4, 7]`
* `listA + listB`: `list`, `[100, 0, 1, 4, 7, 'x', 'z', 't', 'q']`
* `string`, `'z'`
```
listB.sort()
listB.pop()
```
* `listB.count('a')`: `int`, `0`
* `listB.remove('a')`: `NoneType`, `error`
* `listA.extend([4, 1, 6, 3, 4])`: `NoneType`, `None`
* `listA.count(4)`: `int`, `3`
* `listA.index(1)`: `int`, `2`
* `listA.pop(4)`: `int`, `7`
* `listA.reverse()`: `NoneType`, `NOne`
* `listA`: `list`, `[4, 3, 6, 1, 4, 4, 1, 0, 100]`

### Exercise 4
16/16 points (graded)

For the last expression in each question below, specify its type and value. If it generates an error, select type 'NoneType' and put the word 'error' in the box for the value.

1. `boolean`, `True`
```
>>> aList = [0, 1, 2, 3, 4, 5]
>>> bList = aList
>>> aList[2] = 'hello'
>>> aList == bList
```
2. `boolean`, `True`
```
>>> aList is bList
```
3. `list`, `[0, 1, 'hello', 3, 4, 5]`
```
>>> aList
```
4. `list`, `[0, 1, 'hello', 3, 4, 5]`
```
>>> bList
```
5. `boolean`, `True`
```
>>> cList = [6, 5, 4, 3, 2]
>>> dList = []
>>> for num in cList:
        dList.append(num)
>>> cList == dList
```
6. `boolean`, `False`
```
>>> cList is dList
```
7. `list`, `[6, 5, 20, 3, 2]`
```
>>> cList[2] = 20
>>> cList
```
8. `list`, `[6, 5, 4, 3, 2]`
```
>>> dList
```

### Exercise: apply to each
#### Exercise: apply to each 1
5/5 points (graded)

Here is the code for a function `applyToEach`:
```
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
```
Assume that
```
testList = [1, -4, 8, -9]
```
For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using `applyToEach`, so that after evaluation `testList` has the indicated value. You may need to write a simple procedure in each question to help with this process.

Example Question:
```
>>> print(testList)
[5, -20, 40, -45]
```
<details>
<summary>Solution to Example Question</summary>
<br>

```
def timesFive(a):
    return a * 5

applyToEach(testList, timesFive)
```
</details>

```
>>> print(testList)
[1, 4, 8, 9]
```
```python:
applyToEach(testList, abs)
```

#### Exercise: apply to each 2
5/5 points (graded)

```
>>> print(testList)
[2, -3, 9, -8]
```
```python:
def plusone(n):
    return n + 1
applyToEach(testList, plusone)
```

#### Exercise: apply to each 3
5/5 points (graded)

```
>>> print(testList)
[1, 16, 64, 81]
```
```python:
def sqrd(n):
    return n**2
applyToEach(testList, sqrd)
```

### Exercise 5
3/3 points (graded)

Here is a different piece of code for working with lists:
```
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
```
Suppose that you are given the following functions:
```
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
```

1. `applyEachTo([inc, square, halve, abs], -3)`: `[-2, 9, -1.5, 3]`
2. `applyEachTo([inc, square, halve, abs], 3.0)`: `[4.0, 9.0, 1.5, 3.0]`
2. `applyEachTo([inc, max, int], -3)`: `error`

## Lecture 6. Dictionaries
* [Lecture 6. Dictionaries](#lecture-6-dictionaries)
  + [Exercise 1](#exercise-1-5)
  + [Exercise: how many](#exercise-how-many)
  + [Exercise: biggest](#exercise-biggest)

### Exercise 1
12/12 points (graded)

Suppose we evaluate the following expressions:
```
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
```

1. `{'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}`
```
>>> animals
```
2. `'coati'`
```
>>> animals['c']
```
3. `error`
```
>>> animals['donkey']
```
4. `4`
```
>>> len(animals)
```
5. `'anteater'`
```
>>> animals['a'] = 'anteater'
>>> animals['a']
```
6. `8`
```
>>> len(animals['a'])
```
7. `False`
```
>>> 'baboon' in animals
```
8. `True`
```
>>> 'donkey' in animals.values()
```
9. `True`
```
>>> 'b' in animals
```
10. `dict_keys(['a', 'b', 'c', 'd'])`
```
>>> animals.keys()
```
11. `3`
```
>>> del animals['b']
>>> len(animals)
```
12. `dict_values(['anteater', 'coati', 'donkey'])`
```
>>> animals.values()
```

### Exercise: how many
5/5 points (graded)

Consider the following sequence of expressions:
```
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
```
We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:
```
>>> print(how_many(animals))
6
```

```python:
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    return sum([len(e) if type(e) == list else 1 for e in aDict.values()])
```

### Exercise: biggest
5/5 points (graded)

Consider the following sequence of expressions:
```
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
```
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called `biggest`, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

Example usage:
```
>>> biggest(animals)
'd'
```
If there are no values in the dictionary, `biggest` should return `None`.
```python:
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = {k: len(v) for k, v in aDict.items()}
    return max(count, key=count.get) if max(count.values()) > 0 else None
```

# Unit 4: Good Programming Practices
## Lecture 7. Testing and Debugging
* [Lecture 7. Testing and Debugging](#lecture-7-testing-and-debugging)
  + [Exercise 1](#exercise-1-6)
  + [Exercise 2](#exercise-2-5)
  + [Exercise 3](#exercise-3-5)
  + [Exercise 4](#exercise-4-4)
  + [Exercise 5](#exercise-5-4)
  + [Exercise: integer division](#exercise-integer-division)
  + [Exercise 6](#exercise-6-3)
  + [Exercise 7](#exercise-7-3)

### Exercise 1
1/1 point (graded)

Consider the following code specification:
```
def size(aSet):
   """
   aSet is a collection of objects, which might be empty.
   Objects are assumed to be of the same type.
   """
```
Here is a set of possible test cases to include in a black box test suite. Indicate which of the following conditions would make a good black box test suite for the function `size` by clicking on the appropriate choice(s).
<details>
<summary>Review: Black Box Test Suites</summary>
<br>

Black-box testing is a method of software testing that tests the *functionality* of an application. Recall from the lecture that a way to think about black-box testing is to look at both:

* The possible paths through the specification.
* The possible boundary cases.

Undoubtably many - if not all - of the listed tests look like they would be pretty good for testing the function `size`. However, we want you to think critically about the way `size` is specified - including possible boundary cases - and pick a set of tests that adequately and fully tests all paths and boundary conditions. Be sure the set of tests you pick does not have extraneous, useless, or repetitive tests.
</details>

- [x] Empty set
- [x] Set of size 1
- [ ] Set of odd size
- [ ] Set of even size
- [x] Set of size greater than 1
- [ ] Set whose size is a prime number
### Exercise 2
1/1 point (graded)

Consider the following code specification:
```
def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
```
Indicate which of the conditions below would combine to make a good black box test suite for the function `union` by selecting the appropriate choice(s).

- [x] `set1` is an empty set; `set2` is an empty set
- [x] `set1` is an empty set; `set2` is of size greater than or equal to 1
- [x] `set1` is of size greater than or equal to 1; `set2` is an empty set
- [x] `set1` and `set2` are both nonempty sets which do not contain any objects in common
- [x] `set1` and `set2` are both nonempty sets which contain objects in common

### Exercise 3
1/1 point (graded)

Consider the following function definition:
```
def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger
```
Assume that `maxOfThree` is called with numbers as arguments.

Which of the following test suites would make a path-complete glass box test suite for `maxOfThree`?

<details>
<summary>Review: Glass Box Test Suites</summary>
<br>

Recall from the lecture that a path-complete glass box test suite would find test cases that go through every possible path in the code. This is different from black-box testing, because in black-box testing you only have the function specification. For glass-box testing, you actually know how the function you are testing is defined. Thus you can use this definition to figure out how many different paths through the code exist, and then pick a test suite based on that knowledge.

Undoubtably many - if not all - of the listed tests look like they would be pretty good for testing the function `maxOfThree`. However, we want you to think critically about the way `maxOfThree` is defined - including possible boundary cases - and pick a set of tests that adequately and fully tests all paths and boundary conditions. A good first step will be to look at the function definition and figure out what paths through the code exist. Then, look through the suggested test suites one test at a time and see if the suite tests every single path.
</details>

- [x] Test Suite A: `maxOfThree(2, -10, 100)`, `maxOfThree(7, 9, 10)`, `maxOfThree(6, 1, 5)`, `maxOfThree(0, 40, 20)`
- [ ] Test Suite B: `maxOfThree(10, 100, -20)`, `maxOfThree(99, 0, 20)`, `maxOfThree(1, 60, 300)`
- [ ] Test Suite C: `maxOfThree(0, 0, 0)`, `maxOfThree(-3, -10, -1)`, `maxOfThree(10, 30, 100)`, `maxOfThree(0, -9, 11)`, `maxOfThree(-10, 0, 30)`

### Exercise 4
1/1 point (graded)

Consider the following function definition:
```
def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      return set1[0] + union(set1[1:], set2)
```
Assume that `union` is called with strings as arguments.

Please select the best glass box test suite for the function `union` from the following options:

- [ ] Test Suite A: union('',''), union('','a'), union('','ab'), union('a',''), union('a','b'), union('c','ab'), union('de',''), union('ab','c'), union('cd','ab')
- [ ] Test Suite B: union('abc',''), union('abc','a'), union('abc','ab'), union('abc','d'), union('abc', 'abcd')
- [ ] Test Suite C: union('','abc'), union('a','abc'), union('ab','abc'), union('abc','abc')
- [x] Test Suite D: union('','abc'), union('a','abc'), union('ab','abc'), union('d','abc')

### Exercise 5
1/1 point (graded)

Consider the following function definition:
```
def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count
```
Please select the best glass box test suite for the function `foo` from the following options.

- [ ] Test Suite A: `foo(2, 5)`, `foo(5, 6)`, `foo(9, 7)`
- [x] Test Suite B: `foo(10, 3)`, `foo(1, 4)`, `foo(10, 6)`
- [ ] Test Suite C: `foo(100, 5)`, `foo(96, 5)`, `foo(22, 5)`

### Exercise: integer division
5/5 points (graded)

Consider the following function definition:
```
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    while x >= a:
        count += 1
        x = x - a
    return count
```
When we call
```
print(integerDivision(5, 3))
```
we get the following error message:
```
File "temp.py", line 9, in integerDivision
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
```
Your task is to modify the code for integerDivision so that this error does not occur.
```python:
def integerDivision(x, a, count=0):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    while x >= a:
        count += 1
        x = x - a
    return count
```

### Exercise 6
2/2 points (graded)

Consider the following function definition:
```
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)
```
When we call
```
rem(2, 5)
```
the shell returns 2. When we call
```
rem(5, 5)
```
the shell returns 0. But when we call
```
rem(7, 5)
```
the shell does not return anything! Using this information, choose what line of code should be changed from the following choices:

- [ ] `if x == a:`
- [ ] `return 0`
- [ ] `elif x < a:`
- [ ] `return x`
- [ ] `else:`
- [x] `rem(x-a, a)`

How should this line be rewritten?
```python:
return rem(x-a, a)
```

### Exercise 7

Consider the following function definition:
```
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)
```
When we call `f(3)` we expect the result 6, but we get 0.

When we call `f(1)` we expect the result 1, but we get 0.

When we call `f(0)` we expect the result 1, but we get 0.

Using this information, choose what line of code should be changed from the following choices:

- [ ] `if n == 0:`
- [x] `return n`
- [ ] `else:`
- [ ] `return n * f(n-1)`

How should this line be rewritten?
```python:
return 1
```

## Lecture 8. Exceptions and Assertions
* [Lecture 8. Exceptions and Assertions](#lecture-7-exceptions-and-assertions)
  + [Exercise 1](#exercise-1-7)
  + [Exercise 2](#exercise-2-6)
  + [Exercise: simple divide](#exercise-simple-divide)
  + [Exercise 3](#exercise-3-6)

### Exercise 1
5/5 points (graded)

Try to answer the following questions by just reading the code. Reading code is a very good skill to have (and will help you both in your programming career and on your exams!). It is okay to check your answers that you obtain from just reading the code, then in your interpreter run the code for the ones you got wrong on your first attempt.

What error (if any) is raised when the following code snippets are attempted?

* `'1' / '2'`: `TypeError`
* `'1' / 2`: `TypeError`
* `int('1') / 2.0`: `No error is raised`
* `ValueError`
```
mylist = [10, 20, 30]
mylist.index(11)
```
* `NameError`
```
A=2
3*a
```

### Exercise 2
11/11 points (graded)

Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

These questions will ask you to write what the code prints out. If an exception is raised that is not handled by the code write "error" (no quotes), in addition to any other text that is output.

The function in the following questions takes a list of integers `numbers` and a position `index`, and divides each entry in the list of numbers by the value at entry `index`.

Write what it prints out, separating what appears on a new line by a comma and a space.

1. 
```
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
```
* What does `fancy_divide([0, 2, 4], 1)` print out? `1, 0`
* What does `fancy_divide([0, 2, 4], 4)` print out? `-1, 0`
* What does `fancy_divide([0, 2, 4], 0)` print out? `0, error` (`ZeroDivisionError`)

2. 
```
def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
```
* What does `fancy_divide([0, 2, 4], 1)` print out? `1, 0`
* What does `fancy_divide([0, 2, 4], 4)` print out? `1, 0, 0`
* What does `fancy_divide([0, 2, 4], 0)` print out? `-2, 0`

3. 
```
def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
```
* What does `fancy_divide([0, 2, 4], 1)` print out? `1, 0`
* What does `fancy_divide([0, 2, 4], 4)` print out? `1, 0, 0`
* What does `fancy_divide([0, 2, 4], 0)` print out? `0, -2`

4. Does this code print 0 when you call `fancy_divide([0, 2, 4], 0)`? `No.`
```
def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
```

5. Does this code print 0 when you call `fancy_divide([0, 2, 4], 0)`? `Yes.` 
```
def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
```

### Exercise: simple divide
5/5 points (graded)

Suppose we rewrite the FancyDivide function to use a helper function.
```
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   return item / denom
```
This code raises a `ZeroDivisionError` exception for the following call: `fancy_divide([0, 2, 4], 0)`

Your task is to change the definition of `simple_divide` so that the call does not raise an exception. When dividing by 0, `fancy_divide` should return a list with all 0 elements. Any other error cases should still raise exceptions. You should only handle the `ZeroDivisionError`.

```python:
def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
```

### Exercise 3
8/8 points (graded)

Consider the function normalize that takes as input a list of positive numbers numbers and returns a list of numbers that are a fraction of the maximum element in the list. Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong. You'll learn the most this way, by figuring things out, instead of just running the code and reading off the answers.
```
def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers
```
The code below tries to call normalize with one particular input. Answer the next 5 questions based on the following code.
```
try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')
```
1. Does the `try` block throw (also known as raise) an exception? `Yes`
2. What is the name of the exception the code is trying to catch? `ZeroDivisionError`
3. What is the output? `Invalid maximum element`
4. Since we are dividing by the maximum element in a list of positive numbers, we know that `normalize` will return a value between 0 and 1. What type of condition is this? `post condition`
5. We also know the result is not meaningful when the maximum element is 0, so we want to ensure that the numbers in the list do not violate this. What type of condition is this? `pre condition`

Now assume the definition of the function normalize is rewritten as follows
```
def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers
```    
Answer the next 3 questions based on this code.

1. Which condition does the line `assert(max_number != 0)` correspond to? `pre condition`
2. Which condition does the line `assert(0.0 <= numbers[i] <= 1.0)` correspond to? `post condition`
3. What does the function call `normalize([0, 0, 0])` print out? `AssertionError`

# Unit 5: Object Oriented Programming
## Lecture 9. Classes and Inheritance
* [Lecture 9. Classes and Inheritance](#lecture-9-classes-and-inheritance)
  + [Exercise 1](#exercise-1-8)
  + [Exercise 2](#exercise-2-7)
  + [Exercise 3](#exercise-3-7)
  + [Exercise: coordinate](#exercise-coordinate)
  + [Exercise: int set](#exercise-int-set)
  + [Exercise: spell](#exercise-spell)
  + [Exercise 4](#exercise-4-5)

### Exercise 1
5/5 points (graded)

1. What method is called when an object is created?

- [ ] `self`
- [ ] `obj.self`
- [ ] `init`
- [x] `__init__`
- [ ] `new`

2. If you have an object instance, obj, and you want to call its doSomething() method (assuming it has one), how would you do this? (write the line of code you would use)
```
obj.doSomething()
```

3. True or False? An object's attributes must be defined in the object's `__init__` method.

- [ ] True
- [x] False

4. The following code starts the definition of a class called Address. The class needs to have two attributes: number and streetName. Please add in the two lines of code that will create these attributes from the appropriate passed in parameters.
```
class Address(object):
    def __init__(self, number, streetName):
        # Line 1: Creating a number attribute
        # Line 2: Creating a streetName attribute  
```
* What is the correct expression for # Line 1? `self.number = number`
* What is the correct expression for # Line 2? `self.streetName = streetName`

### Exercise 2
4/4 points (graded)

1. Consider the following code:
```
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	time = '6:30'
	print(self.time)

clock = Clock('5:30')
clock.print_time()
```
What does the code print out? If you aren't sure, create a Python file and run it. `5:30`

2. Consider the following code:
```
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self, time):
	print(time)

clock = Clock('5:30')
clock.print_time('10:30')
```
What does the code print out? If you aren't sure, create a Python file and run it. `10:30`

3. Consider the following code:
```
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
```
What does the code print out? If you aren't sure, create a Python file and run it. `10:30`

Are boston_clock and paris_clock different objects?

- [ ] Yes
- [x] No

### Exercise 3
24/24 points (graded)

Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated inside the `print`. If evaluating an expression would cause an error, select NoneType and write `error` in the box. If the result is a function, select function and write `function` in the box. As always, try to do this problem by hand before turning to your interpreter for help.

Assume the following definitions have been made:
```
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
```

1. `NoneType`: `error`
```
w1 = Weird(X, Y)
print(w1.getX())
```

2. `NoneType`: `error`
```
print(w1.getY())
```

3. `int`: `7`
```
w2 = Wild(X, Y)
print(w2.getX())
```

4. `int`: `8`
```
print(w2.getY())
```

5. `int`: `17`
```
w3 = Wild(17, 18)
print(w3.getX())
```

6. `int`: `18`
```
print(w3.getY())
```

7. `int`: `7`
```
w4 = Wild(X, 18)
print(w4.getX())
```

8. `int`: `18`
```
print(w4.getY())
```

9.`int`: `31`
```
X = w4.getX() + w3.getX() + w2.getX()
print(X)
```

10. `int`: `7`
```
print(w4.getX())
```

11. `int`: `44`
```
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)
```

12. `int`: `8`
```
print(w2.getY())
```

### Exercise: coordinate
5/5 points (graded)

Consider the following code from the last lecture video:
```
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
```
Your task is to define the following two methods for the `Coordinate` class:

1. Add an `__eq__` method that returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).

2. Define `__repr__`, a special method that returns a string that looks like a valid Python expression that could be used to recreate an object with the same value. In other words, `eval(repr(c)) == c` given the definition of `__eq__` from part 1.

For more on `__repr__`, see this [SO post](https://stackoverflow.com/questions/452300/python-object-repr-self-should-be-an-expression).
```python:
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
```

### Exercise: int set
5/5 points (graded)

Consider the following code from the last lecture video:
```
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
```

Your task is to define the following two methods for the `intSet` class:

1. Define an `intersect` method that returns a new `intSet` containing elements that appear in both sets. In other words,
```
s1.intersect(s2)
```
would return a new `intSet` of integers that appear in both `s1` and `s2`. Think carefully - what should happen if `s1` and `s2` have no elements in common?

2. Add the appropriate method(s) so that `len(s)` returns the number of elements in `s`.

Hint: look through the [Python docs](https://docs.python.org/3.3/reference/datamodel.html) to figure out what you'll need to solve this problem.
```python:
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        newSet = intSet()
        for element in [e for e in self.vals if other.member(e)]:
            newSet.insert(element)
        return newSet
        
    def __len__(self):
        return len(self.vals)
```

### Exercise: spell
9/9 points (graded)

Consider the following code:
```
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
```

1. What are the parent class(es)? Note that the term "parent class" is interchangable with the term "superclass".

- [x] Spell
- [ ] Accio
- [ ] Confundo

2. What are the child class(es)? Note that the term "child class" is interchangable with the term "subclass".

- [ ] Spell
- [x] Accio
- [x] Confundo

3. What does the code print out? Try figuring it out in your head before you try running it in Python.

Hint: This code prints out 5 lines. Enter each line that is printed out in its own box, in sequential order.

  1. Accio
  2. Summoning Charm Accio
  3. No description
  4. Confundus Charm Confundo
  5. Causes the victim to become confused and befuddled.

4. Which `getDescription` method is called when `studySpell(Confundo())` is executed?

- [ ] The getDescription method defined within the Spell class
- [ ] The getDescription method defined within the Accio class
- [x] The getDescription method defined within the Confundo class

5. How do we need to modify `Accio` so that `print(Accio())` will print the following description?
```
Summoning Charm Accio
This charm summons an object to the caster, potentially over a significant distance.
```

```python:
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
```

### Exercise 4
7/7 points (graded)

Python supports a limited form of multiple inheritance, demonstrated in the following code:
```
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")
```
Which `__init__` methods are invoked and in which order is determined by the coding of the individual `__init__` methods.

When resolving a reference to an attribute of an object that's an instance of class `D`, Python first searches the object's instance variables then uses a simple left-to-right, depth first search through the class hierarchy. In this case that would mean searching the class `C`, followed the class `B` and its superclasses (ie, class `A`, and then any superclasses it may have, et cetera).

With the definitions above if we define
```
obj = D()
```
then what is printed by each of the following statements?

1. `print(obj.a)`: `2`
2. `print(obj.b)`: `3`
3. `print(obj.c)`: `5`
4. `print(obj.d)`: `6`
5. `obj.x()`: `A.x`
6. `obj.y()`: `C.y`
7. `obj.z()`: `D.z`

## Lecture 10. An Extended Example
* [Lecture 10. An Extended Example](#lecture-10-an-extended-example)
  + [Exercise: hand](#exercise-hand)
  + [Exercise 1](#exercise-1-9)
  + [Exercise: genPrimes](#exercise-genprimes)
  + [Exercise 2](#exercise-2-8)

### Exercise: hand
5/5 points (graded)

In this problem, you'll be asked to read through an object-oriented implementation of the hand from the word game problem of Problem Set 4. You'll then be asked to implement one of its methods. Note that the implementation of the object-oriented version of the hand is a bit different than how we did things with the functional implementation; pay close attention to doc strings and read through the implementation carefully.

To begin: Download [hand.py](https://raw.githubusercontent.com/lcsm29/edx-mit-6.00.1x/d4f275378820b82aaa3ed1b06dc0f1ff940b3d5d/others/hand.py) and read through the file. Be sure to understand what's going on in the file. Make a few instances of the `Hand` class, and play around with the existing methods.

When you have completed reading through the file, implement the `update` method.

Paste the entire `Hand` class in the box below.

The `__str__` method is this:
```
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''        
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output
```
Use this `__str__` method to ensure the grading of the hand's display is consistent.
```python:
class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        for char, count in {c: word.count(c) for c in set(word)}.items():
            if char not in self.hand.keys():
                return False
            if count > self.hand[char]:
                return False
        for c in word:
            self.hand[c] = self.hand.get(c, 0) - 1
        return True
```

### Exercise 1
2/2 points (graded)

This problem will ask some questions about the previous problem. You will want to refer to the `Hand` class from `hand.py`.

1. There are two ways to write the `Hand.update` method: you could write this method in a way that gets rid of the key letter in the attribute `hand` dictionary when the frequency of the letter falls to 0, or write it in a way that leaves the key letter in the attribute `hand` dictionary even when the frequency of the letter falls to 0.

Will the two different implementations of the `Hand.update` method lead to `Hand` objects having different hand internal attributes?

- [ ] Yes, always
- [x] Yes, depending on what happened during the update call
- [ ] No

2. There are two ways to write the `Hand.update` method: you could write this method in a way that gets rid of the key letter in the attribute `hand` dictionary when the frequency of the letter falls to 0, or write it in a way that leaves the key letter in the attribute `hand` dictionary even when the frequency of the letter falls to 0.

Does the `calculateLen` method, as defined, return different values for the two different implementations of the `update` method?

- [ ] Yes, always
- [ ] Yes, depending on what happened during the update call
- [x] No
### Exercise: genPrimes
5/5 points (graded)

Write a generator, `genPrimes`, that returns the sequence of prime numbers on successive calls to its `next()` method: 2, 3, 5, 7, 11, ...

#### Hints
<details>
<summary>Ideas about the problem</summary>
<br>

Have the generator keep a list of the primes it's generated. A candidate number `x` is prime if `(x % p) != 0` for all earlier primes `p`.
</details>

```python:
def genPrimes(cand=1):
    primes=[2]
    while True:
        cand += 2
        for p in primes:
            if cand % p == 0:
                break
        else:
            yield primes[-1]
            primes.append(cand)
```

### Exercise 2
10/10 points (graded)

This problem will ask a series of questions about generators.

1. Thinking about the `genPrimes` generator from the last problem, which of the following can be done only by using a generator, instead of defining a function (that uses any type of construct we've learned about, except generators)?

- [ ] Return 1000000 prime numbers
- [ ] Print every 10th prime number, until you've printed 20 of them
- [ ] Keep printing the prime number until the user stops the program
- [x] Everything that can be done with generator can be done with a function

2. Every procedure that has a yield statement is a generator.

- [x] True
- [ ] False

3. If a procedure has only one yield statement, but that statement will never be executed, then the procedure is not a generator.

- [ ] True
- [x] False

4. If we were to use a generator to iterate over a million numbers, how many numbers do we need to store in memory at once?

- [ ] 1
- [x] 2
- [ ] 1000
- [ ] 1000000
- [ ] Don't need to store anything in memory

For the following tasks, would it be best to use a generator, a standard function, or either?

1. Finding the nth Fibonacci number

- [ ] Generator
- [x] Standard function
- [ ] Either a generator or standard function is fine

2. Printing out an unbounded sequence of Fibonacci numbers

- [x] Generator
- [ ] Standard function
- [ ] Either a generator or standard function is fine

3. Printing out a bounded sequence of prime numbers, where the prime numbers are successively computed by division by smaller primes

- [ ] Generator
- [ ] Standard function
- [x] Either a generator or standard function is fine

4. Printing out an unbounded sequence of prime numbers, where the prime numbers are successively computed by division by smaller primes

- [x] Generator
- [ ] Standard function
- [ ] Either a generator or standard function is fine

5. Finding the score of a word from the 6.00x Word Game of Pset 4

- [ ] Generator
- [x] Standard function
- [ ] Either a generator or standard function is fine

6. Iterating over a sequence of numbers in a random order, where no number is repeated

- [ ] Generator
- [x] Standard function
- [ ] Either a generator or standard function is fine

# Unit 6: Algorithmic Complexity
## Lecture 11. Computational Complexity
* [Lecture 11. Computational Complexity](#lecture-11-computational-complexity)
  + [Exercise 1](#exercise-1-10)
  + [Exercise 2](#exercise-2-9)
  + [Exercise 3](#exercise-3-8)
  + [Exercise 4](#exercise-4-6)
  + [Exercise 5](#exercise-5-5)
  + [Exercise 6](#exercise-6-4)
  + [Exercise 7](#exercise-7-4)

### Exercise 1

### Exercise 2

### Exercise 3

### Exercise 4

### Exercise 5

### Exercise 6

### Exercise 7


## Lecture 12. Searching and Sorting Algorithms


# Unit 7: Plotting and Final Thoughts
## Lecture 13. Visualization of Data


## Lecture 14. Summary
