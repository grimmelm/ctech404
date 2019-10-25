# Exercise Title: H5P Strings are Immutable
---
## Key Technical Outcome

## Exercise Context
Lists are mutable - list methods change the orignal list<br>
Strings are immutable - string methods do NOT change the orignal string.<br>
Therefore, some of the methods we have used on lists, such as .append(), cannot be used on strings. 
If you attempt to use such a method, you will receive an error. 
One way to make a change to a string is to create a new string that contains the desired change.<br>


## Exercise Instructions

<pre>
my_string = 'Yellow Submarine.'<br>
s = my_string.replace('Y', 'F')
</pre>

What is the value of <code>my_string</code>?<br>
'Yellow Submarine.' # <b> correct </b> <br>
'Fellow Submarine.' <br>
None of the above <br>

What is the value of <code>s</code>?
'Yellow Submarine.' <br>
'Fellow Submarine.' # <b> correct </b> <br>
None of the above <br>

<pre>
my_string = 'Flood'<br>
s = my_string.replace('F', 'G').replace('l', '') + ' ' + 'Bye!'<br>
</pre>
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
