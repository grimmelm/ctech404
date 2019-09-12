# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome
## Exercise Context
sorted(), 
reversed(), 
max(), min(), 
sum()

## Exercise Instructions

<pre>a_list = [3, 29, 45, 2, 101, 14]</pre>

Which functions produce the following results?

<pre>a_list = [2, 3, 14, 29, 45, 101]</pre>
list(reverse()) <br>
sorted() # <b> correct </b> <br>
min() <br>
max() <br>
sum()

<pre>2<pre>
list(reverse()) <br>
sorted()  <br>
min() # <b> correct </b><br>
max() <br>
sum()

What is the result of the following:

1. <pre>list(reversed(['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear']))</pre>

<pre>['bear', 'zebra', 'lion', 'mouse', 'cat', 'dog']</pre> # <b>correct</b><br>
<pre>['bear', 'cat', 'dog', 'lion', 'mouse', 'zebra']</pre><br>
'bear'<br>
ERROR<br>

2. <pre>sorted(['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear'])

<pre>['bear', 'zebra', 'lion', 'mouse', 'cat', 'dog']</pre> <br>
'dog'
<pre>['bear', 'cat', 'dog', 'lion', 'mouse', 'zebra']</pre> # <b>correct</b>br>
ERROR<br>

3. <pre>min(['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear'])</pre>

'dog' <br>
'bear' # <b>correct</b> <br>
<pre>['bear', 'cat', 'dog', 'lion', 'mouse', 'zebra']</pre> <br>
ERROR<br>

4. <pre>sum(['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear'])</pre>

<pre>['dog', 'cat', 'mouse', 'lion', 'zebra', 'bear']</pre><br>
<pre>['bear', 'cat', 'dog', 'lion', 'mouse', 'zebra']</pre> <br>
'dog'<br>
ERROR<br>

5. <pre>a_list = [3, 29, 45, 2, 101, 14]</pre>

sum(a_list)/len(a_list)
6 <br>
194 <br>
32 # <b>correct</b> <br>
ERROR

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
