"""
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
 and another number. The function decides whether or not the given number is inside the list and returns (then prints)
  an appropriate boolean.
  """

def input_numbers():
    input_list=input('Please enter list of numbers:')
    return input_list
    
def con(*args):
    
    ui_number=input("Please a numbers:")
    if ui_number in args:
        print "True"
    else:
        print "False"
        
def main():
    
    args=input_numbers()
    con(*args)

main()