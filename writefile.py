# f = open('newfile.txt', 'a')
# f.write("\nHello World")
# f.close()

# This will add the word "Hello" (or whatever is in the write function) into the file. 

words = ['The', 'Quick', 'Brown', 'Fox']
words_as_str = "\n".join(words)
f = open('words.txt', 'w')
f.write(words_as_str)
f.close()

# readlines inserts a new line, and writelines doesn't seperate the words. To make write work, you have to add the '\n' for new lines with .join(name of list)

# R is for read, W is for write, A is for append in the open file command. There is also R+, W+ and A+. These will allow for reading/writing/and appending. 

# When you call open, you have a variable called f. print(f.mode) will tell you what type of file you have (read, write, etc) 