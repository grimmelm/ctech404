# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome
Understand string functions, namely int() and string()

## Exercise Context
Sometimes it is necessary to use string functions when writing output. <br>
For example, we may want to convert an integer into a string to output a number along with text. <br>
The following exercise will demonstrate how to properly use these functions.


## Exercise Instructions

MC Select the output? (maybe add an invalid option?)<br>
  
str(4) (4, '4', 4.0, error) #'4' <br>
int(4) (4, '4', 4.0, error) # 4 <br>
int('56') (56, '56', 56.0, error) # 56 <br>
str(int('27.0')) (27, '27', 27.0, error) #error - the string '27.0' represents a floating point number and cannot be converted directly to an integer. <br>
int(str(100)) (100, '100', 100.0, error) # 100 <br>
str('100.0') (100, '100', 100.0, error) # '100.0' <br>

Enter the output into the text box: <br>

print('I am outputting the number ' + str(int('123')))<br> 


## Any Unique Requirements or Notes?

---
# Technical Requirements
<em><strong>If these aren't distinct from what is specified in the course and module-level specs, you can leave these blank.</strong></em>

## Environment/s Used
<em>Here is where you indicate environments that the student will work in. Such as: code editor with browser preview, command line with virtual desktop for previewing plots, or unique environments such as RStudio, Jupyter Notebooks, etc...</em>

## Language/s Used
<em>Indicate any languages used that are unique to this exercise (this is quite rare).</em>

## Package/s Required
<em>Indicate here any unique packages that need to be installed for the exercise to function.</em>

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
