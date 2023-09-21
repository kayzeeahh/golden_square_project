def todo_list(str):
    todo = "#TODO"
    for word in str.split():
        if word == todo:
            return "This task is not completed"
        else:
            return "This task is completed"
    