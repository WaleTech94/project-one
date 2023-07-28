1. Describe the Problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

    def check_for_todo()
    Parameters: (list all parameters and their types)
        Some text given as an argument (string)

    Returns: (state the return value and its type)
        argument if contains #TODO (String)
        returns False if it does not contain #TODO (Boolean)

    Side effects: (state any side effects)
       Should fail if not given a string
    
    pass # Test-driving means _not_ writing any code here yet.
3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

"""
Given a string that contains #TODO, it should return the string
check_for_todo("#TODO Wash Dishes") == "#TODO Wash Dishes"
'''
Given a string without #TODO, it should return False
check_for_todo("Tidy Bathroom") == False
'''
Given a non string, it should raise an error
check_for_todo(123) == "This is not a valid string"
'''
Given an empty string, it should raise an error
check_for_todo("") == "This is not a valid string

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE
