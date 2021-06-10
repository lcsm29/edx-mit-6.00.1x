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
  + [Exercise 1](#exercise-1)
  + [Exercise 2](#exercise-2)
    - [Exercise 2 part 1](#exercise-2-part-1)
    - [Exercise 2 part 2](#exercise-2-part-2)
    - [Exercise 2 part 3](#exercise-2-part-3)
    - [Exercise 2 part 4](#exercise-2-part-4)
  + [Exercise 3](#exercise-3)
  + [Exercise. hello world](#exercise-hello-world)
  + [Exercise. happy](#exercise-happy)
  + [Exercise 4](#exercise-4)
  + [Exercise. while](#exercise-while)
    - [Exercise: while exercise 1](#exercise-while-exercise-1)
    - [Exercise: while exercise 2](#exercise-while-exercise-2)
    - [Exercise: while exercise 3](#exercise-while-exercise-3)
  + [Exercise. for](#exercise-for)
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

### Exercise. hello world
5.0/5.0 points (graded)

Write a piece of Python code that prints out the string hello world
```python:
print('hello world')
```


### Exercise. happy
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

### Exercise. while

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

Here is a list of Python keywords. https://docs.python.org/3/reference/lexical_analysis.html#keywords

Here is a list of Python built-in functions. https://docs.python.org/3/reference/lexical_analysis.html#keywords

You will learn more about functions in the next lecture sequence!
</details>

```python:
s = 0
while end:
    s += end
    end -= 1
print(s)
```

### Exercise. for
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
  + [Exercise 1.](#exercise-1)
  + [Exercise 2](#exercise-2-1)
  + [Exercise. guess my number](#exercise-guess-my-number)
  + [Exercise 3](#exercise-3-1)
### Exercise 1.
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

### Exercise. guess my number
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

* Notice how if we have two print statements

print("Hi")

print("there")

* The output will have each string on a separate line:

Hi

there

* Now try adding the following:

print("Hi",end='')

print("there")

print("Hi",end='*')

print("there")

* The output will place the subsequent string on the same line

* and will connect the two prints with the character given by end

Hithere

Hi*there
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
  + [Exercise 1](#exercise-1-1)
  + [Exercise 2](#exercise-2-2)
  + [Exercise 3](#exercise-3-2)
  + [Exercise 4](#exercise-4-1)
  + [Exercise 5](#exercise-5-2)
  + [Exercise 6](#exercise-6-2)
  + [Exercise. fourth power](#exercise-fourth-power)
  + [Exercise. odd](#exercise-odd)
  + [Exercise. power iter](#exercise-power-iter)
  + [Exercise. power recur](#exercise-power-recur)
  + [Exercise. gcd iter](#exercise-gcd-iter)
  + [Exercise. gcd recur](#exercise-gcd-recur)
  + [Exercise. as in](#exercise-as-in)
  + [Exercise 7](#exercise-7-2)
### Exercise 1

### Exercise 2

### Exercise 3
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

### Exercise. fourth power

### Exercise. odd

### Exercise. power iter

### Exercise. power recur

### Exercise. gcd iter

### Exercise. gcd recur

### Exercise. as in

### Exercise 7

# Unit 3: Structured Programs
## Lecture 5. Tuples and Lists


## Lecture 6. Dictionaries


# Unit 4: Good Programming Practices
## Lecture 7. Testing and Debugging


## Lecture 8. Exceptions and Assertions


# Unit 5: Object Oriented Programming
## Lecture 9. Classes and Inheritance


## Lecture 10. An Extended Example


# Unit 6: Algorithmic Complexity
## Lecture 11. Computational Complexity


## Lecture 12. Searching and Sorting Algorithms


# Unit 7: Plotting and Final Thoughts
## Lecture 13. Visualization of Data


## Lecture 14. Summary

