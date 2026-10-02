#!/usr/bin/python3
"""
Module to determine if all locked boxes can be opened.
"""
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    :param boxes: list of lists, where boxes[i] contains keys found in box i
    :return: True if all boxes can be opened, False otherwise
    """

    n = len(boxes)
    if n == 0:
        return True

    # tracks of unlocked boxes 
    unlocked  = {0}

    # keys to process 
    key_process = [0]

    while key_process:
        current_box = keys_to_process.pop()
        
        for key in boxes[current_box]:

            if 0 <= key < n and key not in unlocked:
                unlocked.add(key)
                key_process.append(key)
    
    return len(unlocked) == len(boxes)
    



