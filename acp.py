# Holiday Activity Planner
# Lesson: Nested Conditional Statements
 
print("=============================")
print("    Welcome to Holiday Planner!     ")
print("===============")
print()
 
print("Step 1: Pick your holiday type")
print("  1 - christmas")
print("  2 - Diwali")
print()
wish= int(input("Enter 1 or 2: "))
print()
 
if wish == 1:
    print("Step 2: Pick your christmas routine")
    print("  1 - do chores")
    print("  2 - decoratiung")
    print()
 
    christmas = int(input("Enter 1 or 2: "))
    print()
 
    if christmas == 1:
        print("You picked  : chores")
        print("Best time   : all time ")
    else:
        print("You picked  : new year")
        print("Best time   : visiting cousins")
 
elif wish == 2:
    print("Step 2: ")
    print("  1 - fireworks lighting")
    print("  2 - diya making")
    print()
 
    diwali = int(input("Enter 1 or 2: "))
    print()
 
    if diwali == 1:
        print("You picked  : diya")
        print("Best for    : fun time")
    else:
        print("You picked  : firework lighting")
        print("Best for    : night time beauty")
 
else:
    print("That was not a valid choice.")
    print("Please enter 1 for christmas or 2 for diwali.")
 
print()
print("============================")
print("   Your holiday plan is ready!      ")
print("   Enjoy your trip!                 ")
print("============================")
