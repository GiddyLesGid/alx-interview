<div align="center">
  <h1>Lockboxes Challenge</h1>
  <p>
    <b>Determine if all the boxes can be opened</b>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.9-blue" alt="Python 3.9">
  </p>
</div>

Problem Description

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to the other boxes.

Your task is to write a Python function canUnlockAll(boxes) that determines if all the boxes can be opened.

Prototype

def canUnlockAll(boxes: List[List[int]]) -> bool

boxes is a list of lists where each list represents a box and contains integers representing keys.
A key with the same number as a box opens that box.
You can assume all keys will be positive integers.
There can be keys that do not have boxes.
The first box boxes[0] is unlocked.

Your function should return True if all boxes can be opened, and False otherwise.

Example

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False


Implementation Details

The function canUnlockAll(boxes) can be implemented using a depth-first search (DFS) algorithm to traverse through the boxes and keep track of the opened boxes using a dictionary.

1. Initialize a set keys to keep track of all the keys found while traversing the boxes.
2. Use a dictionary opened_boxes to keep track of opened boxes during the traversal.
3. Start the traversal from the first box boxes[0].
4. For each box, update the keys set with the keys found in the current box.
5. If a new box is found and it has not been opened yet, continue the traversal from the new box.
6. If no new box is found during the traversal, it means no more boxes can be opened, and the function should return False.
7. After the traversal, check if all boxes except the first one have been opened. If not, return False, otherwise, return True.

How to Run the Code

To run the code and test the implementation, follow these steps:

1. Save the provided Python code in a file named lockboxes.py.
2. Use the canUnlockAll(boxes) function in your code by importing it:

from lockboxes import canUnlockAll

1. Create a list of lists boxes representing the locked boxes and their keys.
2. Call the canUnlockAll(boxes) function with the boxes list as an argument to check if all boxes can be opened.

Testing

You can test the implementation by running the provided test cases or adding your own test cases in a separate file and calling the function with different inputs.

Feel free to explore the implementation and modify the code as needed for your specific use case.

Author
GiddyLesGid
