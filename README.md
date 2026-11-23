
# python-development

## Python Week 3 - Grade Reporter & Bug Hunt

### Assignment Files

- `grade_reporter.py`: Uses loops and conditional statements to assign grades, count passes and failures, and calculate the average score.
- `bug_hunt.py`: Demonstrates identifying and fixing three bugs in a while loop to calculate the sum of numbers from 1 to 5.

### Bug Hunt Reflection

The hardest bug to identify was the incorrect while-loop condition because it did not produce an error message. The program could run but return 10 instead of the expected 15. I knew something was wrong because the number 5 was not being included in the calculation. Changing `< 5` to `<= 5` corrected the problem.

---

## Python Week 4 - Functions

### Assignment Files

- `welcome.py`: Uses a welcome() function to generate greetings for different people without repeating code.
- `toolbox.py`: Contains three reusable functions for doubling numbers, checking pass scores, and generating greetings with optional greeting messages.

### Function Reflection

The hardest function to write was greet() because it had to accept an optional greeting while still using "Hello" by default. I understood that a default parameter allows the function to work with either one or two arguments.