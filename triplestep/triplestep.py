#Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

#tip: use recursion
times_called  = 0

def triplestep(steps: int):
   global times_called
   times_called += 1
   print(f'times_called {times_called}')
   if steps <= 0:
         return 0
   if steps == 1:
         return 1
   return (1 + triplestep(steps - 1) + triplestep(steps - 2) + triplestep(steps - 3))

# non-recursive solution   
def triplestep_tribonacci(steps: int):
   # Tribonacci sequence: F(N) = F(N-1)+F(N-2)+F(N-3) creates a list [0,0,1,2,4,7,13,24,44,81,149,274,504 etc.]
   # using this list, we can build a stair_paths list where stair_paths[i] is the # of possible paths up [i] number of stairs
   Tribonacci_seq = [0,0,1,2,4]
   for i in range (5, (steps + 3)):
       # next entry in the sequence is the sum of the 3 previous entries
       next_entry = Tribonacci_seq[i-1]+Tribonacci_seq[i-2]+Tribonacci_seq[i-3]
       Tribonacci_seq.append(next_entry)

   stair_paths = [0,1,2]
   for m in range (3, (steps + 1)):
       trib_index = m+1
       trib_next = trib_index - 3
       # start at trib_index, continue to add the value 3 numbers back until you reach the start of the sequence (0)
       # i.e. 11 stairs, start at trib_index 12 (504): 504 + 81 + 13 + 2 + 0 = 600 possible stair/step combinations
       new_entry = Tribonacci_seq[trib_next]+Tribonacci_seq[trib_index]
       trib_next -= 3
       while (trib_next > 0):
           new_entry += Tribonacci_seq[trib_next]
           trib_next -= 3
       stair_paths.append(new_entry)

   return stair_paths[steps]
