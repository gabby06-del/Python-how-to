# Practice on Lecture three topics by making a savings goal tracker
# the program should ask the user:
# How much money do you want to save?
# How much money will you save each week? 
# The program should print weekly until the goal is reached

#--------------------- Example code----------------

goal = int(input("How much money do you want to save in total?: "))
weekly_saving= int(input("How much money do you want to save weekly?: "))
week = 0
total_saved = 0
while total_saved<goal:
    week +=1 
    total_saved = weekly_saving*week
    print(f"Week {week}: total saved {total_saved}")
print(f"goal reached! {total_saved} saved")