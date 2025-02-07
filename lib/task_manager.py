def find_to_do_tasks(text):
    if type(text) != str:
        raise Exception('Error: input must be a string')

    if text == '':
        raise Exception('Error: function find_to_do_tasks takes an input of string')
    if text.upper().find('#TODO') != -1:
        return True
    else:
        return False