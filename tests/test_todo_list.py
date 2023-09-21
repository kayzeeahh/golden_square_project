from lib.todo_list import *

def test_check_for_todo():
    result = todo_list("#TODO learn some python programming")
    assert result == "This task is not completed"
    
def test_for_no_todo():
    result = todo_list("eat breakfast")
    assert result == "This task is completed"
    