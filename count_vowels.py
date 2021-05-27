# def count_vowels(txt):
#     vowels = 0
#     vowels += txt.count('a')
#     vowels += txt.count('e')
#     vowels += txt.count('i')
#     vowels += txt.count('o')
#     vowels += txt.count('u')
#     return vowels

def count_vowels(txt):
    return sum([1 for x in txt.lower() if x in 'aeiou'])