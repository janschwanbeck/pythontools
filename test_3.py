# Path: main.py (in a different directory than test.py)
import sys
sys.path.append("/path/to/directory/containing/test.py")
import test

print(test.test())  # This will print the numpy array
