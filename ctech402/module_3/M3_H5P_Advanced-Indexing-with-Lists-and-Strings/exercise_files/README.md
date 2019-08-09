# Description

Most importantly, this folder needs to contain a solution_code.ext file which is the solution to the exercise the student is faced with. A few things that should be clarified about that file:

* In many cases there are multiple routes by which a student could reach the needed outcome of the exercise. The solution_code.ext file should be an example of your estimation of the best way to reach the intended outcome, and does not need to be exhaustive of all possible solutions. Your test criteria in the exercise specs file is what will indicate which aspects of the solution_code file are essential and need to be tested.
* You should use commenting in your solution_code.ext file to indicate which aspects of the code need to be explicitly tested and which are flexible to different methods. For test criteria which is based on output or process, that can be described in the exercise_specs file. This file will not be student-facing or accessible to students.
* In some cases there will not be a single file that can contain a solution to the exercise. The required approach here will vary based on circumstance, but try to make the structure of the solution files clearly titled and well commented. When logical, put all these files into a solution_code subfolder. If you are stuck on how to structure this reach out to your instructional designer.

Second most importantly, this folder should contain a starter_code.ext file or files which is the file that a student starts with at the beginning of the exercise. Sometimes this will be blank, in which case you should note this in your exercise_specs.md file. In other cases it will be numerous files, in which case you should put them in a starter_code subfolder and name them appropriately. Many of these files will be student facing, so ensure they model good code writing etiquette with appropriate indentation, spacing, and commenting as needed.

There may be other files that are specific to this exercise that are needed for it to function, these should also be included in this folder. This could be things like datasets, images, stylesheets, etc...
Please name them logically in a way that indicates their function.

Lastly, please be sure to test your files locally to ensure everything is functioning before commiting to the repo.
