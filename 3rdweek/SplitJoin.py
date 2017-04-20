"""
You are given a string.  Split the string on a " " (space) delimiter and join using a - hyphen.
Sample Input
this is a string   
Sample Output
this-is-a-strin
"""

s=raw_input("Please enter a sentence:")

print "-".join(s.split())