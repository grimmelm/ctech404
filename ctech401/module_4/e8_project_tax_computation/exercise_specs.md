# Exercise Title:
---
# Instructional Requirements
## Key Technical Outcome
Test the comprehension of most topics covered in this course:
1. I/O
2. Branching with if/else statements and nested if/else statements
3. comparison operators 
4. data types and type conversion
5. expressions


## Exercise Context
It's time to put into practice everything we have learned in this course!
(elaborate?)

## Exercise Instructions
You will write a program that computes a user's federal income tax for the year.

The table below contains the federal income tax rates:

| Tax rate	| Taxable income bracket	| Tax owed
| ----------|-------------------------| ------------------------------------------------ |
| 10%       | $0 to $9,525            | 10% of taxable income                            |
| 12%	      | $9,526 to $38,700	      | $952.50 plus 12% of the amount over $9,525       |
| 22%	      | $38,701 to $82,500	    | $4,453.50 plus 22% of the amount over $38,700    |
| 24%	      | $82,501 to $157,500	    | $14,089.50 plus 24% of the amount over $82,500   |
| 32%	      | $157,501 to $200,000	  | $32,089.50 plus 32% of the amount over $157,500  |
| 35%	      | $200,001 to $500,000	  | $45,689.50 plus 35% of the amount over $200,000  |
| 37%	      | $500,001 or more	      | $150,689.50 plus 37% of the amount over $500,000 |


Your program should use the information contained in this table to compute the tax owed for the different tax brackets (hint: use nested if/else). <b>should i give the formula?  x = 952.50 + 0.12*(income - 9525)?</b>
  
  
The IRS requests that that we round our amounts to the nearest dollar. <br>
For example, $101.49 rounds to $101, while $101.51 round to $102.

After you have computed the tax owed, round that amount to the nearest dollar.

Your program will ask the user to input his or her yearly income, will compute how much tax is owed, and then output that amount to the user.

<em>Sample output:</em>

Tax due: $1,250


## Any Unique Requirements or Notes?
I'm using the tax table from 2018-19. 
---
# Technical Requirements

## Environment/s Used
Code editor and terminal

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
