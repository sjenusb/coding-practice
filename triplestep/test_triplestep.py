from triplestep import *

def test_triplestep():
   assert triplestep(0) == 0
   assert triplestep(1) == 1
   assert triplestep(2) == 2
   assert triplestep(3) == 4

def test_triplestep_tribonacci():  
   assert triplestep_tribonacci(0) == 0
   assert triplestep_tribonacci(1) == 1
   assert triplestep_tribonacci(2) == 2
   assert triplestep_tribonacci(3) == 4
   assert triplestep_tribonacci(4) == 8
   assert triplestep_tribonacci(9) == 177
   assert triplestep_tribonacci(11) == 600
   assert triplestep_tribonacci(17) == 23249
