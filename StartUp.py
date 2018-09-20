# Yr8CS1_Samit

# MyFirstProgram
# v_3
# lr_20180815

# File to run the code
# BTW the reason for this is because you can run the projects from here
# and i might add some more functionality later


def run():
    try:
        runner = __import__('MyFirstPythonFile')

        while True:
            runner.startup()
            if not input('\nRestart? (y/n) ').lower() == 'y':
                break
    except KeyboardInterrupt:
        print('\nForce Shutting Down...')
        return


run()
