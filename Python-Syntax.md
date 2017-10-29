# Basic Python Syntax
## Python 2

1. Printing output in python 2 :
     ```
     print "argument that you want to print"
     ```
      is same as
     ```
     print 'argument that you want to print'
     ```
2. Mathematical operators :
   ```
   x = 8
   y = 4
   print x+y                  # it wil give output of sum of x and y
   print x-y                  # it will give difference of x and y
   print x*y                  # it will give product of x and y
   print x/y                  # it will give quotient when x is divided by y
   print x%y                  # it is modulo function and gives remainder when x is divied by y
   print x ** y               # it means x^y. it is way to represnt power operator
   ```
   
 3. Comments in python (Python interpreter ignores them) :
     1) Single line comments can be given by putting # before a line.
     ```
       #This is a single line comment
     ```
     		
     2) Multi line comments can be given by putting 3 double quotes befire and after the lines.
   ```
       """This
     	    is a
     	    multiline comment
	    :)"""
   ```
 
 4. To find out the type of a value or a variable that refers to that value, you can use the type() function. 
  ```  
       a = 5
       type(a)
       >>>int
  ```
 5. To validate a variable to be an integer or a string, use ```isinstance(<var>, <type>)```
 it accepts two parameter:
    1) Variable name
    2) Type to be validated
  
 ```
  isinstance(a, dict) , isinstance(num, integer)
  # It return True if true else False.
 ```

 6. The strings are concatenated (pasted together) using the + operator:
       ```
       a = "Hello" + "World"
       ```
        is same as
       ```
       a = "HelloWorld"
       ```
 
 7. Python provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced.
 The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount.
 
 8. Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation character (\) to denote that the line should continue.
 ```
 a = \
 b + \
 c
 is same as a = b + c
 ```
 
 9. Python has six built-in types of sequences, but the most common ones are lists and tuples. There are certain operations you can perform on all sequence types: indexing, slicing, adding, multiplying, and checking for membership. Python has built-in functions for finding the length ( len() ) of a sequence and for finding its largest ( max() ) and smallest elements ( min() ).
 
 10. List is a compound data type; you can group values together. Lists can be written as a list of comma-separated values (items) between square brackets:
 ```
       a = "is"
       b = "nice"
       my_list = ["my", "list", a, b]
 ```
 A list can contain any or a mix of Python types including strings, floats, booleans, even list itself (list in a list) etc.

 11. 
 ```
     len([1, 2, 3])
     >>>3   	                         # Length
     [1, 2, 3] + [4, 5, 6]
     >>>[1, 2, 3, 4, 5, 6]	         # Concatenation
     ['Hi!'] * 4
     >>>['Hi!', 'Hi!', 'Hi!', 'Hi!']	 # Repetition
     3 in [1, 2, 3]
     >>>True	                         # Membership
     for x in [1, 2, 3]: print x,
     >>>1 2 3	                         # Iteration 
 ```
    
 12. Some more functions on list:
 ```
 list.append(obj)          # Appends object obj to list
 list.count(obj)           # Returns count of how many times obj occurs in list	
 list.extend(seq)          # Appends the contents of seq to list
 list.index(obj)           # Returns the lowest index in list that obj appears	
 list.insert(index, obj)   # Inserts object obj into list at offset index
 list.pop(obj=list[-1])    # Removes and returns last object or obj from list
 list.remove(obj)          # Removes object obj from list
 list.reverse()            # Reverses objects of list in place
 list.sort([func])         # Sorts objects of list, use compare func if given
 ```
 
 13. Subsetting Python lists
 ```
       x = ["a", "b", "c", "d"]
       x[1]
       >>>'b'
       x[-3]
       >>>'b'
    # same result!
 ```
 Note: Offsets start at zero
       Negative index: start counting from the right
       Slicing fetches sections
          
 14. Slicing means selecting multiple elements from your list.
 Syntax: my_list[start:end]
 The start index will be included, while the end index is not.
  ```
       x = ["a", "b", "c", "d"]
       x[1:3]
       >>>['b', 'c']
  ``` 
  If start index is not specified:
  ```
       x[:2]
       >>>["a", "b"]
  ``` 
  If end index is not specified:
  ```
       x[2:]
       >>>["c", "d"]
  ```
  If start and end index are not specified:
  ```
       x[:]
       >>>["a", "b", "c", "d"]
  ```
   
 15. Operations on a list:
     
     1. Extending a list:
  ```
       x = ["a", "b", "c", "d"]
       y = x + ["e", "f"]
  ```
  
     2. Replacing elements in a list:
  ```
       x = ["a", "b", "c", "d"]
       x[0] = ["e"]                  # "e" in place of "a"
       x[2:] = ["f", "g"]            # "f", "g" in place of "c", "d"
       >>>["e", "b", "f", "g"]
  ```

     3. Remove elements from your list with del statement:
  ```
       x = ["a", "b", "c", "d"]
       del(x[1])
       >>>["a", "c", "d"]
  ```
  
  Note: As soon as an element is removed from a list, the indexes of the elements that come after the deleted element all change.
  
  Note: Most list methods will change the list they're called on. Examples are:
       1. append(), that adds an element to the list it is called on,
       2. remove(), that removes the first element of a list that matches the input, and
       3. reverse(), that reverses the order of the elements in the list it is called on.
     
 16. In a list call index() method on it, to get the index of the first element of the list that matches its input and call count() method on the list, to get the number of times an element appears in that list.
 
 17. The ; sign is used to place commands on the same line. The following two code chunks are equivalent:
``` 
       # Same line
       command1; command2

       # Separate lines
       command1
       command2
```
 
 18. The functions str(), int(), bool() and float() are used for typecasting (switch between data types). These are built-in functions.
 
 19. You can ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.
    To get help on the max() function, for example, you can use one of these calls:
       help(max)
       ?max
 
