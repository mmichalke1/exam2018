def score_name(name):
    list = []
    score = 0
    name = name.lower()
    for letter in name:
        list.append(letter)
    for item in list:
        score += (ord(item)-96)
    return score

def find_mv():
    text_file = open("roster.txt")
    roster = text_file.readlines()
    high_score = 0
    MVP = ''
    for full_name in roster:
        first_name = (full_name.split()[0])
        if score_name(first_name) > high_score:
            high_score = score_name(first_name)
            MVP = first_name
    return 'The Most Valuable Person in our class is {} with a score of {}'.format(MVP, high_score)

def find_words(name):
    text_file = open("positive-words.txt")
    words = text_file.readlines()
    word_list = []
    for word in words:
        word = word.replace('\n', '')
        if (score_name(word)) == score_name(name):
            word_list.append(word)
    if len(word_list) == 0:
        return None
    else:
        return word_list

def main():

    print(find_mv())
    name = 'Matthew'
    print(find_words(name))
    name = 'a'
    print(find_words(name))
    pass


if __name__ == '__main__':
    main()
