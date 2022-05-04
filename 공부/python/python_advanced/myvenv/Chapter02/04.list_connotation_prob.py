word_list = ['apple', 'watch', 'apolo', 'start', 'abocado']
begins_with_a = [word for word in word_list if word[0] == 'a']
print(begins_with_a)

mylist = ['omega3', '', 'vitamin C500', '', 'ginger']
mylist = [word for word in mylist if word != '']
print(mylist)