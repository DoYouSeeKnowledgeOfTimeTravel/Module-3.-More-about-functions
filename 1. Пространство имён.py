calls = 0

def count_calls():
    global calls
    if calls >= 0:
        calls += 1
    return calls

def string_info(string):
    return len(string), string.upper(), string.lower()
count_calls()

def is_contains(string, list_to_search):
        count_calls()
        lower_string = string.lower()
        for spisok in range(len(list_to_search)):
            list_to_search[spisok] = list_to_search[spisok].lower()
            if lower_string in list_to_search:
                return True
        return False
count_calls()

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)