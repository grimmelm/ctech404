# Exercise Title: H5P Strings are Immutable
---
## Key Technical Outcome

## Exercise Context
Lists are mutable - list methods change the list<br>
Strings are immutable - string methods do NOT change the string.<br>
For this reasons, methods we have used on lists, such as .append(), cannot be used on a string. If you attempt to use such a method, you will receive an error. 
What we can do is create a new string continaing the desired changes.<br>

(note: replace() doesnt change the original string.)

## Exercise Instructions

my_string = 'Yellow Submarine.'<br>
s = my_string.replace('Y', 'F')


What is the value of my_string?<br>
'Yellow Submarine.' # <b> correct </b> <br>
'Fellow Submarine.' <br>
None of the above <br>

What is the value of s?
'Yellow Submarine.' <br>
'Fellow Submarine.' # <b> correct </b> <br>
None of the above <br>


my_string = 'Flood'<br>
s = my_string.replace('F', 'G').replace('l', '') + ' ' + 'Bye!'<br>
What is the value of s? # <b> Free text Quiz: 'Goodbye!' </b>
  

which will this work on? <br>

variable_name.append('s') 

list #<b> correct </b> <br>
string
  
We want to add on to string <code>s = 'Hello</code> to form the phrase 'Hello there!'<br>
Which one of these will work ? (select all that apply)

s = s + ' there!'  # <b> correct </b><br> 

s.append(' there!') <br>

s= s + ' ' + 'there!' # <b> correct </b> <br>

r = ' there!' <br>
s.extend(r) <br>

r = ' there!' <br>
s.append(r)
