def check_for_todo(task):
    # if "#TODO" in str:
    #     return str
    # else:
    #     return False
    if type(task) != str or task == "":
        raise Exception("This is not a valid string")
    return task if "#TODO" in task else False