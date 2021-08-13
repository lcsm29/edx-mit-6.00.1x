## [edX MIT 6.00.1x](https://www.edx.org/course/introduction-to-computer-science-and-programming-7) - Intro to CS and Programming Using Python
A few weeks ago, I have already [finished](https://github.com/lcsm29/MIT6.0001) the same course available on OCW ([MIT 6.0001 Fall 2016](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)) (at least I've finished the problem sets), but that one was pretty old and some provided materials started to break down (e.g. [feedparser](https://github.com/lcsm29/MIT6.0001/commit/c53684d2d6d06465bd0d08087161be7b7d529ee4#diff-d3d78a8e23517614c0c0c8a862b804341cf46d02c80d4db7a515b0f0d299468e)). Also, I don't know whether my implementation or style is acceptable or not, as I don't have anyone to review my code. My code have passed the provided unit tests, but that's about it.

Then, I found [this newer course](https://www.edx.org/course/introduction-to-computer-science-and-programming-7) on edX. The graded assignments and exams did a good job of hooking me up, because that's exactly what I needed. However, after I enrolled in this course, I found out that those assignments are still graded automatically, which is better than nothing but falls short of my expectations. Anyway, they do have slightly different finger exercises and problem sets, so I redid the course once again.

[![Certificate](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/cert.png?raw=true)](https://courses.edx.org/certificates/a5e8444108fe4527871ae5b22a9ff203)
![Progress](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/progress.png?raw=true)

## Contents
* [finger_exercises.md](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/finger_exercises.md): containing all finger exercises and the answers
* [problem_sets.md](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/problem_sets.md): containing all problem sets and links to the solution
* [others](https://github.com/lcsm29/edx-mit-6.00.1x/tree/main/others)/[polysum.py](https://github.com/lcsm29/edx-mit-6.00.1x/blob/main/others/polysum.py): solution for Complete Programming Experience: Polysum

## Exam Info
* **Eligibility**: a) Pay $75 **and** b) go through the automated ID verification process.
  * Both midterm and final exams are behind the paywall, so unless you pay, you don't have an access to exams.
  * You also need to verify your identity. The ID verification is handled by third-party, and it takes a few days to process, so make sure you get your ID verified before the exam starts.
  * Once you verified your ID, it is valid for 2 years. I assume it's probably valid for other courses too for that period.
* **Timed exam**: 8 hours from start to finish
  * The course has a [timed exam](https://support.edx.org/hc/en-us/articles/360000037728) (8 hours), not a [proctored exam](https://support.edx.org/hc/en-us/articles/207249428). Thus, no webcam or software installation is required for monitoring.
  * The 8 hour limit is more than generous. The exam is certainly not meant for 8 hours worth of continuous effort (more like 2-3 hours tops).
  * I think they've implemented such generous limit to handle the extreme cases with some sort of disasters (e.g. edX down for everyone, local internet/power outrage, earthquake, tsunami, etc). It took about 60 minutes for me from start to finish.
* **Randomized question bank**: The problem you get is randomly selected from a question bank.
* **Difficulty**: Roughly on par with problem sets or finger exercises.
* **Types of Problems**: a) Multiple choice problems, b) Coding problems
  * Each multiple choice problem contains several multiple choice quizzes, while each coding problem contains only one problem.
  * I got 2 multiple choice problems (each contains 7-10 multiple choice quizzes), and 5 coding problems for midterm exam.
* **Number of Submissions Alloweds**: a) 1 submission for MC problems, b) 10 submission for coding problems.
  * Don't be too hasty when you submit the answer of the quiz.
* **Scoring**: Based on the result of the auto grader. No human involved in grading.
  * score distribution by type: In my case, the ratio of the score of MC problems to coding problems was roughly 2:8. 20 Points for 17 MC quizzes, and 85 points for 5 coding problems.
* **Things you're allowed and not allowed to do during the exams**:
  * **Allowed**
    1. Look up for resources a) which are posted on the platform (including the textbook), b) any other textbooks you possess, c) and any notes you've prepared youself
    2. Use your IDEs, Python shells, or online Python interpreters to test your solutions for coding problems.
  * **Not Allowed**:
    1. Use the Internet to search for solutions
    2. Communicate with any person about the exam
    3. Run code provided in non-coding questions in your IDEs
    4. Post anything related to the exam questions on the edX discussion forum or anywhere else. (Therefore, I won't post the problems and solutions here)

## Some Other Random Info
* 📅 **Started** on June 3, 2021
* ℹ️ **Python Versions I used**: [3.9.6](https://www.python.org/downloads/release/python-396/)
* 🔗 **Link to my repo for OCW courses:** [MIT6.0001](https://github.com/lcsm29/MIT6.0001), [MIT6.0002](https://github.com/lcsm29/MIT6.0002) (work in progress)

## Resources
The following resources are from the resource page of the course.

### Documentations
* [Official Python 3 Documentation](https://docs.python.org/3/library/index.html) - "official"/technical explanation of what a particular function/operator does, examples of correct syntax, what the various libraries are, etc.
* [PEP 8](https://www.python.org/dev/peps/pep-0008/) - Style Guide for Python Code - learn what is good and bad style in Python

### Textbooks
* [Dive Into Python](https://diveintopython3.problemsolving.io/) (free) - another survey of Python syntax, datatypes, etc.
* [Think Python](https://greenteapress.com/wp/think-python-2e/) by Allen Downey (free) - a good general overview of the Python language. Includes exercises.
* [Learn Python the Hard Way](https://learnpythonthehardway.org/python3/) (free) - another free online text
* [Get Programming: Learn to Code with Python](https://www.manning.com/books/get-programming) by Ana Bell (course staff) - a basic intro to programming if you are having trouble keeping up with the course
* [Fluent Python: Clear, Concise, and Effective Programming](https://www.oreilly.com/library/view/fluent-python/9781491946237/) by Luciano Ramalho - an advanced book

### Tutorials
* [The Official Python Tutorial](https://docs.python.org/3/tutorial/) - self-explanatory
* [Reserved Keywords in Python](https://docs.python.org/3.0/reference/lexical_analysis.html#id8) - don't use these as variable names
* [CheckIO](https://checkio.org/) - learn Python by exploring a game world
* [Invent with Python](https://inventwithpython.com/) - develop your Python skills by making games or hacking ciphers
* [Codecademy](https://www.codecademy.com/catalog) - (note: for Python 2) learn Python by building web apps and manipulating data; interactive tutorial sequence
* [Python Tutor](http://www.pythontutor.com/) - interactive tutorial sequence of exercises
* [Blog with tutorials](https://mitxcsjourney.blogspot.com/) - created by one of our community TAs
* [Study Guide](https://docs.google.com/document/d/1oMYRnogRrGgCtz-26E8hJYLp7Bm99JS1SP4lhdXvqpw/edit#heading=h.wkdtdlnax0u3) - created by another of our community TAs

### Debugging
* [Python Tutor](http://www.pythontutor.com/) - an excellent way to actually visualize how the interpreter actually reads and executes your code
* [DiffChecker](https://www.diffchecker.com/) - compares two sets of text and shows you which lines are different
* [Debugging in Python](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/) - steps you can take to try to debug your program

### Software
* [Python Tools for Visual Studio](https://microsoft.github.io/PTVS/) - Visual Studio plug-in enabling Python programming

### Other Q&A
* [Stack Overflow](https://stackoverflow.com/questions/tagged/python) - a large Q&A forum for programming concepts (not just Python). Try searching here before you post on the edX forum, and you may find that someone has already answered your question.

### More practice problems
* [Python Challenge](http://www.pythonchallenge.com/) - a series of puzzles you can try to test your Python abilities
* [Project Euler](https://projecteuler.net/) - additional programming challenges you can try once your Python knowledge becomes stronger; problems are sorted by increasing difficulty
* [Coding Bat](https://codingbat.com/python) - problems you can solve within an online interpreter
* [Codewars](https://www.codewars.com/?language=python) - improve your skills by training on real code challenges
