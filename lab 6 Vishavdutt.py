"""
Lab 6 - Strings and Tuples 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  <vishav dutt sharma>
Due Date: This Friday (Mar. 1) 11am.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
    # Using string slicing to reverse the string
    return s[::-1] 


# Your unit tests
def test_reverse_str():
    assert reverse_str('app') == 'ppa'
    assert reverse_str('Abd') == 'dbA'
    assert reverse_str('COMP115') == '511PMOC'
    assert reverse_str('hello') == 'olleh'
    assert reverse_str('12345') == '54321'


"""
Exercise 2 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.


For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    # Convert the input string to lowercase for case-insensitive counting
    s = s.lower()

    # Count the vowels using list comprehension
    vowel_count = sum(1 for char in s if char in 'aeiou')

    return vowel_count


# Your unit tests
def test_count_vowels():
    assert count_vowels("Apple") == 2
    assert count_vowels("Hmmm") == 0
    assert count_vowels("Python is fun") == 4

    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOUaeiou") == 10



"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: We have implemented a function removing duplicates for a list in week 6. Similar.
"""
def remove_duplicates(s):
    """
    This function removes duplicate characters in a string.

    E.g., 
    >>> remove_duplicates("apple")
    'aple'

    Parameters:
    - s (string): The input string from which duplicates will be removed.

    Returns:
    - (string): The string with duplicate characters removed.

    """
    # Use a set to keep track of unique characters
    unique_chars = set()

    # Use a list to store the characters in order
    result = []

    # Iterate through the string
    for char in s:
        # Check if the character is not in the set (i.e., not encountered before)
        if char not in unique_chars:
            # Add the character to the set and the result list
            unique_chars.add(char)
            result.append(char)

    # Convert the result list to a string
    result_string = ''.join(result)

    return result_string


# Your unit tests
def test_remove_duplicates():
    assert remove_duplicates("apple") == "aple"
    assert remove_duplicates("Popsipple") == "Popsile"
    assert remove_duplicates("pear") == "pear"
    assert remove_duplicates("Hello") == "Helo"
    assert remove_duplicates("Mississippi") == "Misp"



"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    This function returns the lowest index of the character t in the string s.
    If the character is not in the string, it returns -1.

    E.g., 
    >>> find_index("Abd", 'b')
    1

    Parameters:
    - s (string): The input string in which to search for the character.
    - t (char): The character to find in the string.

    Returns:
    - (int): The lowest index of the character t in the string s or -1 if not found.

    """
    # Iterate through the string
    for i, char in enumerate(s):
        # Check if the current character is equal to the target character
        if char == t:
            return i

    # If the target character is not found, return -1
    return -1


# Your unit tests
def test_find_index():
    assert find_index("Abd", 'b') == 1
    assert find_index("Abdccc", 'c') == 3
    assert find_index("Abd", 'w') == -1
    assert find_index("Hello", 'l') == 2
    assert find_index("Python", 'z') == -1


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def project_completion_day(day, days_to_completion):
    """
    This function returns the project completion day given the current day in a week and estimated time of days to completion.

    E.g., 
    >>> project_completion_day('Monday', 4)
    'Friday'

    Parameters:
    - day (string): The current day in a week (case-sensitive).
    - days_to_completion (int): The estimated time in days to project completion.

    Returns:
    - (string): The project completion day.

    """
    # Find the index of the current day in the tuple
    current_day_index = days_week.index(day)

    # Calculate the completion day index
    completion_day_index = (current_day_index + days_to_completion) % 7

    # Return the completion day using the index
    return days_week[completion_day_index]


# Your unit tests
def test_project_completion_day():
    assert project_completion_day('Monday', 4) == 'Friday'
    assert project_completion_day('Monday', 7) == 'Monday'
    assert project_completion_day('Saturday', 2) == 'Monday'
    assert project_completion_day('Saturday', 1) == 'Sunday'
    assert project_completion_day('Wednesday', 5) == 'Monday'


"""
Congratulations on finishing your lab6. Hope you feel more confident on function implementation.

Now you just need to upload it to your GitHub repository. That's all.

"""