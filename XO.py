# def XO(txt):
#     if txt.lower().count('x') == txt.lower().count('o'):
#        return True
#     else:
#         return False

def XO(text):
  return text.lower().count('x') == text.lower().count('o')

print(XO("ooxx"))


