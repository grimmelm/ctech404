# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome

## Exercise Context
We have seen the differencde between methods and functions and the effects they can have on the values of variables.

[Comment on how a method returns None]
[Comment on how this applies to all methods() including reverse() sort() etc

## Exercise Instructions

1. We have a list a_list = [12,20,18,14,20]. We want to sort a_list but do not want to change the value of a_list. Rather, we want the sorted result to be saved to variable sorted_a_list. How do we accomplish this?

a_list.sort()
b_list.sort()
b_list = a_list.sort()
b_list = sorted(a_list)

2. Examine the following operations:
a_list = [1,2,3,4,5]
b_list = a_list
a_list.reverse()

What is the value of b_list?

None <br>
[1,2,3,4,5] <br>
[5,4,3,2,1] # <b>correct</b><br>

What is the value of a_list?

None <br>
[1,2,3,4,5]<br>
[5,4,3,2,1] # <b>correct</b><br>


3. Examine the following operations:
a_list = [1,2,3,4,5]
b_list = a_list
list(reversed(a_list))

What is the value of b_list?

None <br>
[1,2,3,4,5] # <b>correct</b> <br>
[5,4,3,2,1] <br>

What is the value of a_list?

None <br>
[1,2,3,4,5] # <b>correct</b><br>
[5,4,3,2,1] <br>

4. Examine the following operations:
a_list = [1,2,3,4,5]
b_list = list(reversed(a_list))

What is the value of b_list?

None <br>
[1,2,3,4,5]  <br>
[5,4,3,2,1] # <b>correct</b> <br>

What is the value of a_list?

None <br>
[1,2,3,4,5] # <b>correct</b><br>
[5,4,3,2,1] <br>

5. Examine the following operations:
a_list = [1,2,3,4,5]
b_list = a_list.reverse()

What is the value of b_list?

None # <b>correct</b><br>
[1,2,3,4,5]  <br>
[5,4,3,2,1]  <br>

What is the value of a_list?

None <br>
[1,2,3,4,5] <br>
[5,4,3,2,1] # <b>correct</b><br>


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
