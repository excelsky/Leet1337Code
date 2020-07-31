def average_words(words):
    words = words.strip()
    if len(words) == 0:
        return None
    word_list = words.split()
    count_list = [len(x) for x in word_list]
    return round(sum(count_list) / len(count_list), 1)




words0 = ''
ans0 = None
words1 = 'fb'
ans1 = 2
words2 = ' Hello World '
ans2 = 5
words3 = 'This is how we re-do that'
ans3 = 3.3 # <-- [4,2,3,2,5,4]
assert average_words(words0) == ans0
assert average_words(words1) == ans1
assert average_words(words2) == ans2
assert average_words(words3) == ans3