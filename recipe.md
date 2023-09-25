SINGLE METHOD RECIPE:


EXERCISE ONE

1. Describe the Problem
# Put or write the user story here. Add any clarifying notes you might have.

> As a user
> So that I can manage my time
>I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute

2. Design the Function Signature
# Include the name of the function, its parameters, return value, and side effects.
def manage_reading_time(words_in_books):
        takes the number of words in a book.
    Parameters: (list all parameters and their type)
        words_in_books: a list of num showung the number of words in multiple book eg. [650, 800, 1500]

    Returns: (state the return value and its type)
        a list of floats divided by 200 to show how many mins it takes to read the text

    Side effects: (state any side effects)
        this function must round up to the nearest whole number


    """
3. Create Examples as Tests
# Make a list of examples of what the function will take and return.
'''given a number that is exactly 200
it returns 1 min'''
manage_reading_time(200) >> [1.0]

'''given a number that is less than 200
it returns a decimal number''
manage_reading_time(50) >> [0.25]

'''given a number more than 200
it returns the number divided by 200 rounded up'''
manage_reading_time(450) >> [2.0]

'''given a 0 or None value
it returns an error'''
manage_reading_time(None) >> error


4. Implement the Behaviour
# After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
 from lib.manage_reading_time import *

'''given a number that is exactly 200
it returns 1 min'''

def test_manage_reading_time(int):
    result = manage_reading_time(200)
    assert result == [1]

























EXERCISE TWO

1. Describe the Problem
# Put or write the user story here. Add any clarifying notes you might have.
> As a user
>To that I can improve my grammar
>I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.


2. Design the Function Signature
# Include the name of the function, its parameters, return value, and side effects.
def check_grammar(string):
    """checks that a text starts with capitl letters and ends with punctuation"""

    Parameters: (list all parameters and their types)
        string: a string thats makes a full sentence.

    Returns: (state the return value and its type)
        a True if the sentence is starts with a capital letter and ends in punctuation

        a False if it is missing both a capital letter and a full stop.

        a "Close, try again" if it is missing a capital letter or a full stop.

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass 



3. Create Examples as Tests
# Make a list of examples of what the function will take and return.

"""
Given no capital letter and no punctuation
It returns False
"""
check_grammar("this is not correct") => False

"""Given a capital letter and punctuation
It returns True"""
check_grammar("This is correct.") => True

"""Given a capital letter but not punctuation
It returns close, try again"
check_grammar("This is almost correct) => "Close, try again!"

"""Given punctuation but not capital letter
It returns close, try again"
check_grammar("this is also almost correct.") => "Close, try again"

4. Implement the Behaviour
# After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

from lib.check_grammar import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_check_no_capital_no_punctuation():
    result = check_grammar("this is not correct")
    assert result == False






















CHALLENGE

1. Describe the Problem
# Put or write the user story here. Add any clarifying notes you might have.
> As a user
>So that I can keep track of my tasks
>I want to check if a text inclues the string #TODO


2. Design the Function Signature
# Include the name of the function, its parameters, return value, and side effects.
def todo_list(string):
    """checks if a string contains #TODO"""

    Parameters: (list all parameters and their types)
        string: a string that may or may not contain #TODO.

    Returns: (state the return value and its type)
        a "This tasks needs to be completed" if the string contains #TODO

        a "This task is completed" is the strinf doesn't contain #TODO

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass 



3. Create Examples as Tests
# Make a list of examples of what the function will take and return.

"""
Given a string with #TODO
It returns message that task needs to be completed
"""
todo_list("#TODO learn some python programming") => "This task is not completed"

"""Given a string without #TODO
todo_list("eat breakfast") => "This tasks is completed"

4. Implement the Behaviour
# After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

from lib.check_grammar import *

"""
Given a string with #TODO
It returns message that task needs to be completed
"""
def test_check_for_todo():
    result = todo_list("#TODO learn some python programming")
    assert result == "This task is not completed"






























////////////////////////////////////////////////

SINGLE CLASS DESIGN RECIPE:

Exercise 1(Pair Programmed)
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
"""
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks
to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and
have them disappear from the list.
"""
2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE
class TaskTracker:
    def __init__(self):
    self._completed = completed
    self._incomplete = incomplete
    def add(self, text):
    a string representing a todo task
    returns a list with added tasks
    def remove(self, completed)
    given a completed task will then remove from the list
    returns a list with only incompleted tasks
3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
given a string without a #TODO
return an error
"""
def test_given_string_without_todo_raises_error():
    todo_list = ToDo_List()
    with pytest.raises(Exception) with e:
        todo_list("")
        error_message = str(e.value)
        assert error_message == "No TODO given!"
"""
given a string with a #TODO
it will return list with the TODO added
"""
def test_given_a_todo_returns_list_with_todo():
    todo_list = ToDo_List()
    result = todo_list.add("#TODO clean room")
    assert result == ["#TODO clean room"]
"""
given a completed task
it will return list without the completed task
"""
def test_without_completed_task():
    todo_list = ToDo_List()
    result = todo_list.remove("#TODO clean room")
    assert result == [""]
4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.





















Design a class(CHALLENGE):
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
"""
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
"""
2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE
class MusicTracker:
    def add(string):
    a string representing music you have listened to
    returns a strings of music listened to in a list.
    

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
given an empty string
return an error
"""
def test_given_an_empty_string():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) with err:
        add("")
        error_message = str(err.value)
        assert error_message == "No music added"
"""
given a string with a song
it will return list with the song added to it
"""
def test_given_song_returns_list_with_song_added():
    music_tracker = MusicTracker()
    music_tracker.add("Rebecca Black - Friday")
    result = music_tracker.song_list
    assert result == ["Rebecca Black - Friday"]
"""
given more than one song
it will return list with all the songs added
"""
def test_without_completed_task():
    music_tracker = MusicTracker()
    music_tracker.add("Rebecca Black - Friday")
    music_tracker.add("Justin Bieber - Baby")
    music_tracker.add("Beyonce - Single Ladies")
    music_tracker.add("Kanye West - All of the lights")
    assert result == ["Rebecca Black - Friday", "Justin Bieber - Baby", "Beyonce - Single Ladies", "Kanye West - All of the lights"]

""" given wrong data type
def 

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

class MusicTracker:
    def add(self, text):
    a string representing music you have listened to
    returns a strings of music listened to in a list.

    return [text]
    

