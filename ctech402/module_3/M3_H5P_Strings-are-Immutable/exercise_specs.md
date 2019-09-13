# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome

## Exercise Context
Lists are mutable - list methods change the list<br>
Strings are immutable - string methods do NOT change the string.<br>
For this reasons, methods we have used on lists, such as .append(), cannot be used on a string. If you attempt to use such a method, you will receive an error. 
What we can do is create a new string continaing the desired changes.<br>

(note: replace() doesnt change the original string. this is not stated in the video and can be confusing to students)


Instructions in doc:

MC for lists <br>
"What is the value of this?" <br>
You can’t change a string- students should learn to call multiple methods in a row by doing  <br>
value.method.method etc.  
1 MC mutable/immutable “which of these will work?” <br>
Give students a desired output after an operation is performed and say which will this work on ( a list or a string). A list will be the correct answer since it is mutable <br>

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


## Any Unique Requirements or Notes?

---
# Technical Requirements
<em><strong></strong></em>

## Environment/s Used
Terminal. Python interpreter

## Language/s Used
<em></em>

## Package/s Required
<em>Python 3</em>

---
# Test Requirements
<em>This is the space to indicate what specifically about the student actions in the exercise needs to be tested. These specifications are the basis of how feedback or grading is given to the student. <strong>Don't worry about the specific method for verifying this initially, just focus on what needs to be checked from the student's actions to validate that they reached the key technical outcome for the exercise. Please also note that not all of these test types need to be specified, only what is necessary to test against the key outcome.</strong></em>

## Outcome Tests
<em>Indicate here criteria that should be tested relating to the outcomes or outputs of a student's actions in the exercise.</em>

## Student Code Tests
<em>This relates to specific aspects of the student's code which need to be assessed. The best way to indicate these requirements is with comments in your solution code file, indicating the parts of the code which need to be verified. This helps make the requirements less abstract. However, if you have any requirements that are better explained long form, please do so below.</em>

## Process Tests
<em>Indicate here criteria that should be tested relating to the process by which the student reached their outcomes in the exercise.</em>

---
#  Implementation Decisions

## Graded or Ungraded:
<em>This is easily adjusted in future iterations, but this is a place to indicate whether this exercise will pass a grade to the Canvas gradebook, just provide smart feedback to the student without a grade, or simply serve as a sandbox environment with no evaluation.</em>

## Exercise Type:
<em>This will always be determined in collaboration with the developers, designers, and authors based on the requirements above, what is most feasible and meets the key objectives.</em>

## Success Message
<em>This is the message the student will see when they complete the exercise, in the case that this is an exercise which provides automatic feedback. This should be written after the implementation decisions are made.</em>

## Test Case Failure Messages
<em>These should be written later in development, and only apply to automatically tested programming exercises. These will be written in accordance with the test cases developed for the exercise, which will also need to be specified here.</em>

## Environment Layout:
<em>This is how the environment components will be presented to students. This will usuall relate to Codio panes and what they contain.</em>

## Custom Codio Menu Items:
<em>This is a space to indicate any buttons that will need to be present in the Codio menu beyond the default items in the template.</em>

## New Integrations Required:
<em>We will indicate here if this exercise requires any new and unestablished integrations with Codio or Canvas.</em>
