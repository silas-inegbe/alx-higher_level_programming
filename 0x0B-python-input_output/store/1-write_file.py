#!/usr/bin/python3
"""Defines a text file writting function"""


def write_file(filename="", text=""):
    """Write a stru=ing to a UTF* text file'

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to thr file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
