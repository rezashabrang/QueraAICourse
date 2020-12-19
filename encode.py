def encode(text):
    text = text.replace('\n', ' ').split()
    counter = 1
    word_to_number_map = {}
    numbers = []
    for word in text:
        if word.isalnum():
            if word not in word_to_number_map:
                word_to_number_map[word] = counter
                counter += 1
            numbers.append(word_to_number_map[word])
        else:
            edited_word = ''.join(i for i in word if i.isalnum())
            if edited_word is '':
                continue
            if edited_word not in word_to_number_map:
                word_to_number_map[edited_word] = counter
                counter += 1
            numbers.append(word_to_number_map[edited_word])

    return word_to_number_map, numbers


text = """
:: #ali# $quera$
quera a'l'i ali
quera  
"""
d , numbers = encode(text)
print(d, numbers)
