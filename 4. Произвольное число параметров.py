def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        root_word = root_word.lower()
        if root_word in word.lower():
            same_words.append(word)
    return same_words

result1 = single_root_words('thing', 'anything', 'everything', 'think', 'thank')
result2 = single_root_words('Effect', 'Effectivity', 'Affect', 'Effort', 'Worthy', 'Effected')
result3 = single_root_words('ThiNg', 'anYthinG', 'eVerYTHiNg', 'tHINk', 'ThAnK')
print(result1)
print(result2)
print(result3)