import unittest
import subprocess
import os

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def assertValidAssembly(self, name):
        res = subprocess.call(['n2tAssembler', f'/autograder/source/{name}.asm'])
        if res != 0:
            raise AssertionError(f'Unable to assemble student hack code!\nTest in the nand2tetris suite to debug.')

    def assertCPUMatches(self, name):
        res = subprocess.call(['n2tCPUEmulator', f'/autograder/source/{name}.tst'])
        if res != 0:
            raise AssertionError(f'Failed to pass test file!\nTest in the nand2tetris suite to debug the mismatch.')

    def assertCorrectJack(self, name):
        if not os.path.isfile(f'/autograder/source/{name}.asm'):
            raise AssertionError(f'{name}.asm not found! Make sure the name is capitalized and has the right extension.')
        self.assertValidAssembly(name)
        self.assertCPUMatches(name)
        subprocess.run(['mv', f'/autograder/source/{name}.out', '/autograder/outputs/'])

class TestModules(TestBase): 
    @weight(95/2)
    @number(1)
    def test_mult(self):
        self.assertCorrectJack('Mult')

    @weight(95/2)
    @number(2)
    def test_fill(self):
        self.assertCorrectJack('Fill')
