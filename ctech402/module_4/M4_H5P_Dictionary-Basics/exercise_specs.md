# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome

## Exercise Context
Syntax, making, looking up elements, assignment

## Exercise Instructions

1. Below is a dictionary that contains a simple itinerary with one main task or appointment to do per day.

weekly_planner = { 'Monday': 'hair appointment'  , 'Tuesday': 'pick up groceries', 'Wednesday': 'baseball practice'}

a. How do you access Monday's itinerary?

weekly_planner[1] <br>
weekly_planner['hair appointment'] <br>
weekly_planner[0] <br>
weekly_planner['Monday'] <b># correct </b>

b. What will the following statement result in?

weekly_planner[2] 

'Tuesday' <br>
error <b># correct </b> # perhaps give explanation again as to why this is a problem<br>  
'Wednesday' <br>
'baseball practice' <br>

c. You would like to have dinner with friends on Friday. Your entry will be 'dinner with friends.' How would you create a new key/value pair in the itinerary dictionary? (free text, answer is itinerary['Friday'] = 'dinner with friends')

2. Examine the dictionary and list below. Which of the following operations result in an error (select all that apply):

d = {45:2, 'x': 12, 'Frank': 'f345P', 'cat': 'not dog'}
l = ['cat', 'Frank', 67]

d[45] <br>
d[0] <b> # error </b><br>
d['Frank'] = 15 <br>
l['Frank'] <b> # error </b><br>
d['not dog']<b> # error </b><br>
d['pizza'] = 'mushrooms' <br>
l[2] = 3 <br>



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
