def pigword(textword):
    new_word = textword[1:] + textword[0] + 'ay'
    return new_word

def depig(textword):
    temp_word = textword.replace('ay','')
    new_word = temp_word[-1] + temp_word[0:-1]
    return new_word

mystring = 'the quick brown fox jumped over the lazy dog'
word_list =mystring.split()
pig_string =''

for word in word_list:
    pig_string += ' ' + (pigword(word))
print(pig_string)

back_string =''
pig_word_list = pig_string.split()

for pig_word in pig_word_list :
    back_string += ' ' + (depig(pig_word))

print(back_string)