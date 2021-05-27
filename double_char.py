# def double_char(txt):
#     # takes a string and 
#     # returns a string in which each character is repeated once
#     character_list = [char for char in txt]
#     output = []
#     for character in character_list:
#         output.append(character)
#         output.append(character)
#     return ''.join(output)

def double_char(txt):
    return ''.join(character*2 for character in txt)    

double_char('abcd')