import unittest
import subprocess

from gradescope_utils.autograder_utils.decorators import weight, number

class TestBase(unittest.TestCase): 
    def assertValidAssembly(self, name):
        res = subprocess.call(['n2tAssembler', f'/autograder/source/{name}.asm'])
        if res != 0:
            raise AssertionError(f'Unable to assemble student\'s ASM output!')

    def assertCPUMatches(self, name):
        res = subprocess.call(['n2tCPUEmulator', f'/autograder/source/{name}.tst'])
        if res != 0:
            raise AssertionError(f'Unable to run CPU Emulator!')

    def assertCorrectJack(self, name):
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
