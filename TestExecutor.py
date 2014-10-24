__author__ = 'polanco'
from proboscis import TestProgram
from proboscis import register

def run_tests():
    from src.testcases.user import RegistrationUserTests


    # Run Proboscis and exit.
    TestProgram().run_and_exit()

if __name__ == '__main__':
    run_tests()