#!/usr/bin/python3
"""A method to check if all boxes can be unlocked"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened given a list of lists,
    where each inner list represents a box containing keys to other boxes.

    Args:
    boxes: A list of lists

    Returns:
    True if all boxes can be opened, False otherwise.
    """
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
