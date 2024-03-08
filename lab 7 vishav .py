"""
Lab 7 - Set and Dict 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  <your name>
Due Date: This Friday (Mar. 8) 11am.
Note: Try best to finish the lab exercises using what we've learnt about algorithms.
      Please do not rely on AI assistant too heavily for labs.

Objective:
1. Review how to write a good python docstring (started from lab6).
2. Review how to code simple Python functions and write unit tests using assert.
3. Practice how to operate on set and dict.
4. Review iterations using loop.
5. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, a set, a dict, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Here is one solution of Lab 6 exercise 3: Remove the duplicate characters in a string.
E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"
"""
def remove_duplicates(s):
    """
    This function removes the duplicates from the string s.

    E.g.,
    >>> remove_duplicates("Apple")
    "Aple"

    Parameters:
    - s (string): The string in which duplicated chars are removed.

    Returns:
    - (string): The string without any duplicated chars.
    """
    res = ''
    for c in s:
        if c not in res:
            res += c
    return res
    
# Your unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"

"""
Exercise 1 (20 marks: doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Can you try to implement the above duplicates removal using data type set?

Hint: 1. We put the seen chars in the set while adding them to the res string;
      We also check if the new char is already in the set (more efficient than checking a string). If not seen, add it to the res string.
      2. To initialize an empty set: seen_set = set()
"""
def remove_duplicates_set(s):
    """
    Removes duplicate characters from a string using a set.

    Parameters:
    - s (str): The input string.

    Returns:
    - str: The string with duplicate characters removed.
    """
    seen_set = set()
    res = ""
    
    for char in s:
        if char not in seen_set:
            seen_set.add(char)
            res += char
    
    return res


# Unit tests
def test_remove_duplicates_set():
    assert remove_duplicates_set("hello") == "helo"
    assert remove_duplicates_set("programming") == "progamin"
    assert remove_duplicates_set("python") == "python"
    assert remove_duplicates_set("aaaaa") == "a"
    assert remove_duplicates_set("") == ""

# Run the unit tests
test_remove_duplicates_set()

"""
Exercise 2 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Assume you've collected many stones, 
and each character in the string stones represents a type of a stone. 
And each character in the string gems represents a type of a gem.

Write a function to calculate how many stones you've collected are actually jems. 

E.g.,
gem_counting("abDFMdm", "admMQq") will return 4
gem_counting("abDFMdm", "af") will return 1
gem_counting("awCcM", "cQqW") will return 1
gem_counting("bFfL", "cQqW") will return 0
"""
def gem_counting(stones, gems):
    """
    Calculates the number of stones that are actually gems.

    Parameters:
    - stones (str): A string representing the types of collected stones.
    - gems (str): A string representing the types of gems.

    Returns:
    - int: The count of stones that are gems.
    """
    gem_set = set(gems)
    gem_count = sum(1 for stone in stones if stone in gem_set)
    
    return gem_count


# Unit tests
def test_gem_counting():
    assert gem_counting("abDFMdm", "admMQq") == 4
    assert gem_counting("abDFMdm", "af") == 1
    assert gem_counting("awCcM", "cQqW") == 1
    assert gem_counting("bFfL", "cQqW") == 0
    assert gem_counting("", "cQqW") == 0

# Run the unit tests
test_gem_counting()

"""
Exercise 3 (20 marks: doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

CapU is planning to launch a shuttle bus between main campus 
and the students accomendation. (Fake news but best wishes 😄)

To determine how many buses are needed each day, 
CapU keeps track of the students who use the shuttle bus service.

Write a function students_id() that takes a list of student ids as its parameter, 
and returns the number of different students who use the shuttle service.

E.g.,
students_id(['002', '003', '001', '004', '012']) returns 5
students_id(['002', '003', '001', '012', '003', '001']) returns 4

Hint: 
Think about which data type we should use to ease the work of finding distinctive values from a list.

"""
def students_id(ids):
    """
    Counts the number of different students who use the shuttle service.

    Parameters:
    - ids (list): A list of student ids.

    Returns:
    - int: The number of different students.
    """
    unique_students = set(ids)
    return len(unique_students)


# Unit tests
def test_students_id():
    assert students_id(['002', '003', '001', '004', '012']) == 5
    assert students_id(['002', '003', '001', '012', '003', '001']) == 4
    assert students_id([]) == 0
    assert students_id(['001', '001', '001']) == 1
    assert students_id(['A', 'B', 'C', 'A', 'B']) == 3

# Run the unit tests
test_students_id()

"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Similar as exercise 3, write a function called students_id_occurences() 
that takes a list of student ids as its parameter, 
and returns the occurences of each different student 
who uses the shuttle service in the form of dictionary data type.

E.g.,
students_id_occurences(['002', '003', '001', '004', '012']) 
returns {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}}

students_id_occurences(['002', '003', '001', '012', '003', '001']) 
returns {'002': 1, '003': 2, '001': 2, '012': 1}

Hint: To initialize an empty dict: id_dict = {}
"""
def students_id_occurrences(ids):
    """
    Returns the occurrences of each different student who uses the shuttle service.

    Parameters:
    - ids (list): A list of student ids.

    Returns:
    - dict: A dictionary with student ids as keys and their occurrences as values.
    """
    id_dict = {}
    
    for student_id in ids:
        if student_id in id_dict:
            id_dict[student_id] += 1
        else:
            id_dict[student_id] = 1
    
    return id_dict


# Unit tests
def test_students_id_occurrences():
    assert students_id_occurrences(['002', '003', '001', '004', '012']) == {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}
    assert students_id_occurrences(['002', '003', '001', '012', '003', '001']) == {'002': 1, '003': 2, '001': 2, '012': 1}
    assert students_id_occurrences([]) == {}
    assert students_id_occurrences(['001', '001', '001']) == {'001': 3}
    assert students_id_occurrences(['A', 'B', 'C', 'A', 'B']) == {'A': 2, 'B': 2, 'C': 1}

# Run the unit tests
test_students_id_occurrences()

"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to count 
the frequency of words in a given paragraph.

E.g.,
word_frequency("I am alive. I am happy.") 
returns {'I': 2, 'am': 2, 'alive.': 1, 'happy.': 1}

word_frequency("I do not like water. I like fruits.") 
returns {'I': 2, 'do': 1, 'not': 1, 'like': 2, 'water.': 1, 'fruits.': 1}

Hint: Use paragraph.split() to split the sentences to a list of words.
"""

def word_frequency(paragraph):
    """
    Counts the frequency of words in a given paragraph.

    Parameters:
    - paragraph (str): The input paragraph.

    Returns:
    - dict: A dictionary with words as keys and their frequencies as values.
    """
    word_list = paragraph.split()
    frequency_dict = {}

    for word in word_list:
        # Remove punctuation from the word
        word = word.strip('.,!?:;"()[]{}')
        # Convert the word to lowercase to ensure case-insensitivity
        word = word.lower()

        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict


# Unit tests
def test_word_frequency():
    assert word_frequency("I am alive. I am happy.") == {'i': 2, 'am': 2, 'alive': 1, 'happy': 1}
    assert word_frequency("I do not like water. I like fruits.") == {'i': 2, 'do': 1, 'not': 1, 'like': 2, 'water': 1, 'fruits': 1}
    assert word_frequency("") == {}
    assert word_frequency("This is a test. This is only a test!") == {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
    assert word_frequency("One fish. Two fish. Red fish. Blue fish.") == {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

# Run the unit tests
test_word_frequency()

"""
Congratulations on finishing your lab7. Hope you feel more comfortable now on the data type set and dict.

You just need to upload this lab to your GitHub repository. That's all.
"""