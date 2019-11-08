weekly_planner = { 'Monday': 'hair appointment' , 'Tuesday': 'pick up groceries', 'Wednesday': 'baseball practice', 'Thursday': 'wash car', 'Friday': 'dinner with friends'}

if 'Monday' in weekly_planner:
  weekly_planner.pop('Monday')
  
if 'Wednesday' in weekly_planner:
  weekly_planner.pop('Wednesday')
  
print(weekly_planner)
