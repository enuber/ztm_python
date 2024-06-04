def do_stuff(num=0):
    try:
        # Explicitly checking if num is a string representation of an integer
        if str(num).isdigit():
            return int(num) + 5
        return 'please enter a valid number'
    except ValueError as err:
        return err
