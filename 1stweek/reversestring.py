#Class 04-01-207
#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#  My name is Michele
#Then I would see the string:
#  Michele is name My
#shown back to me.

s=raw_input(' Enter the String to be reversed: ')
print ' '.join(reversed(s.split(" ")))