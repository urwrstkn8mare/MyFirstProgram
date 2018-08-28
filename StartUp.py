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
