
# https://stackoverflow.com/questions/63701553/loop-through-multiple-questions-each-with-a-condition-in-python

def loop_user_input(input_name, meets_condition):
    while True:
        value = int(input(f"Enter {input_name}: "))
        if not meets_condition(value):
            print(f"Invalid {input_name}")
        else:
            return value