# Exercise Title: H5P Control Flow in Functions
---
# Instructional Requirements
## Key Technical Outcome

## Exercise Context

## Exercise Instructions

What is the output of each program?

Q1:
<pre>
def a_function():
    print('I am in the function.')
    
a_function()
a_function()
</pre>


a. 'I am in the function'<br>
b.  Error <br>
c. 'I am in the function' # <b>correct</b> <br>
   'I am in the function'
   
Q2: 
<pre>
def a_function():
    print('I am in the function.')

the_function()
</pre>

a. No output  <br>
b. 'I am in the function' <br>
c.  Error # <b> correct </b> <br>

Q3: 
<pre>
def c_function():
    print('I am in c_function.')

def b_function():
    c_function()
    print('I am in b_function.')    

def a_function():
    print('I am in a_function.')
    b_function()

a_function()
</pre>
 
a. 'I am in a_function' <br>

b. I am in a_function'<br>
   I am in b_function'<br>
   I am in c_function'<br>

c. I am in a_function. # <b>correct</b> <br>
I am in c_function.<br>
I am in b_function.<br>

d. I am in a_function.<br> 
I am in c_function.<br>


Q4: 
<pre>
def c_function():
    print('I am in c_function.')

def b_function():
    c_function()
    print('I am in b_function.')    

def a_function():
    print('I am in a_function.')
    b_function()

b_function()
</pre>


a. I am in a_function. <br>
I am in c_function.<br>
I am in b_function.<br>

b. I am in b_function.<br> 
I am in c_function.<br>

c. I am in c_function.<b> #correct </b><br>
I am in b_function.<br> 

d. No output

Q5: 
<pre>
def c_function():
    print('I am in c_function.')

def b_function():
    print('I am in b_function.') 
    c_function()

def a_function():
    print('I am in a_function.')
    b_function()
</pre>

a. 'I am in a_function' <br>

b. I am in a_function'<br>
   I am in b_function'<br>
   I am in c_function'<br>

c. No output # <b> correct</b><br>
d. Error
