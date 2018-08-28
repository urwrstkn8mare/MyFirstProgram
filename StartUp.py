# Yr8CS1_Samit

# MyFirstProgram
# v_3
# lr_20180815

# File to run the code
# BTW the reason for this is because you can read about my project from here,
# run the projects from here
# and i might add some more functionality later


runner = __import__('MyFirstPythonFile')

while True:
    runner.StartUp()
    restart = input('\nRestart? (y/n) ')
    if restart.lower() == 'y':
        print('')
    else:
        break

# INFO
"""
Each of the files in the projects folder is run from here.
The numbers on each file correspond to the number assigned to them in the importing function.
To understand more just look at the code.
:)
The tester file is for testing and has no use. There is just some random stuff on there i use that
probably doesnt work.
Each version (verson number in this file) is the the next time I look at this project with all it's new stuff
and clean it up (or give it the cherry on top). Then I give it the new version number.
lr (last revision) is the date this file was last worked on.
If you are not Samit then the date is when you were given this project to see.
"""
