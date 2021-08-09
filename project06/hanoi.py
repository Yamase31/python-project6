"""
Author: James Lawson, Laurie Jones, Harry Pinkerton
Project: 6
File: hanoi.py
The Towers of Hanoi game/logic puzzle
"""

from linkedStack import LinkedStack

class Disk(object):
   
   SHAPE = "="
   
   def __init__(self, rank):
      self.rank = rank
      self.str = Disk.SHAPE * rank * 2 + Disk.SHAPE
      

   def __lt__(self, other):
      return self.rank < other.rank
   
   def __gt__(self, other):
      return self.rank > other.rank
   
   def __le__(self, other):
      return self.rank <= other.rank
   
   def __ge__(self, other):
      return self.rank >= other.rank
   
   def __eq__(self, other):
      return self.rank == other.rank
   
   
   def __str__(self):
      return self.str
   

class HanoiTowers(object):
   """A class to simulate the Towers of Hanoi logic puzzle."""
   
   # The maximum rank of the disks is 9
   MAX_SIZE = 9
   
   # Minimum tower printing width in characters for pretty-ness.
   MIN_WIDTH = 9
   
   def __init__(self, size):
      """Sets up the sizes and initial state for the class."""
      
      #Size indicates the maximum rank of the disks
      self.size = min(size, HanoiTowers.MAX_SIZE)
      
      # The tower width has to be at least twice the size of the largest disk rank
      #  plus 3 for some extra padding. Don't make the tower width smaller than the min
      #  width
      self.towerWidth = max(self.size * 2 + 3, HanoiTowers.MIN_WIDTH)
      
      # How many moves until the towers were solved
      self.numMoves = 0
      
      # A list of three stacks to represent the towers
      self.towers = [LinkedStack(), LinkedStack(), LinkedStack()]
      
      # Set up all disks in order on the leftmost stack/tower
      
      while size > 0:
         self.towers[0].push(Disk(size))
         size -= 1
      
         
      
   def centerString(self, string):
      """Helper function to center a string in a space equal to the tower's width."""
      return "{s:^{w}}".format(s=string, w=self.towerWidth)
   
   def makeMove(self, source, destination):
      """Attempts to move from the source tower to the destination tower. Does nothing if the move isn't allowed.
          Disks can be moved on top of disks that are larger than itself, or an empty tower."""
      
      if self.towers[source].isEmpty() == False:
         if self.towers[destination].isEmpty() or self.towers[source].peek() < self.towers[destination].peek() :

            value = self.towers[source].pop()
            self.towers[destination].push(value)
            self.numMoves += 1
         #print("value" + value)
            
   
   def detectWin(self):
      """Returns True if all the disks are on the rightmost tower."""
      if self.towers[0].isEmpty() and self.towers[1].isEmpty():
         return True
      else:
         return False
   
   def __str__(self):
      
      # Add one extra pole at the top for prettiness
      result = self.centerString("|") * len(self.towers) + "\n"
      
      # Create an iterator for each tower
      towerIters = [iter(x) for x in self.towers]
      
      
      # The iterators for stacks go from bottom up, but printing is from top
      #  down, so we need to first iterate through the iterators, then reverse
      #  the results to get the correct printing order.
      # We will create an array of strings that represents each row bottom up,
      #  then reverse it.
      printRows = []
      
      # The number of rows is equal to the size of the Hanoi Tower
      for row in range(self.size):
         
         # Add a new row to our print rows
         printRows.append("")
         
         # Iterate through the iterators
         for tIter in towerIters:
            
            # Try to get the next disk from the tower and add it to the
            #  printRow string.
            try:
               printRows[-1] += self.centerString(str(next(tIter)))
            
            # If we failed to get next() on an iterator, it means the stack is empty
            #  and we need to add a pole character instead.
            except:
               printRows[-1] += self.centerString("|")
               
      # Reverse our printable strings
      printRows.reverse()
      
      # Join by new lines and append to our result
      result += "\n".join(printRows) + "\n"
               
        
      # Add a line of tildes for visual separation from the towers
      result += "~" * self.towerWidth * len(self.towers) + "\n\n"
      
      # Add some tower number labels
      for towerNum in range(len(self.towers)):
         result += self.centerString("Tower " + str(towerNum))
         
      # Extra white space
      result += "\n\n"
      
      return result


#extra credit
'''def solve(HanoiTowers, showProcess = False):
   if showProcess = True
      print(towerGame)
      input("Press Enter each time the tower is changed")

   def recurse(self)''' 
   


def main(gameSize):
   """Runs a game of HanoiTowers"""
   
   # Make a game of HanoiTowers
   towerGame = HanoiTowers(gameSize)
   
   # Run forever
   while True:
      # Display the towers
      print(towerGame)
      
      # Did we win?
      if towerGame.detectWin():
         print("You won in", towerGame.numMoves, "moves!")
         break
      
      # Try to move otherwise
      try:
         move = [int(x) for x in input("Enter the source and destination towers separated by a space: ").split() if x != ""]
         
         # Allow pressing of enter with no input to exit the game
         if len(move) == 0:
            break
         
         towerGame.makeMove(*move)
         
      # If we can't tell what the move is let the user know
      except:
         print("Unknown command.\n")
   

if __name__ == '__main__':
   main(4)

      
