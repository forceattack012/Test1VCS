"! Insert the current directory path tp Python Path"

import sys
import os
cwd = os.getcwd() 
sys.path.append(cwd)
# print(sys.path)

# Test the module :generate_list
from generate_list import printIt()
printIt()