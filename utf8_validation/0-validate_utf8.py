#!/usr/bin/python3
"""
Module to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list of int): List of integers representing bytes.
        
    Returns:
        bool: True if valid UTF-8, False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the bit patterns
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get only the 8 least significant bits of the integer
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine how many bytes the character consists of
            if (byte & mask1) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & mask1) and (byte & mask2) == 0:
                # But wait, let's check the number of leading 1s for 2, 3, or 4 bytes
                pass

            # Count leading 1s
            bit_mask = 1 << 7
            while (byte & bit_mask):
                n_bytes += 1
                bit_mask >>= 1

            # 1 is invalid for n_bytes (cannot have a single leading 1: 10xxxxxx)
            # UTF-8 characters can be at most 4 bytes long
            if n_bytes == 1 or n_bytes > 4:
                return False

            n_bytes -= 1
        else:
            # If we are looking for a continuation byte, it must start with "10"
            if not (byte & mask1) or (byte & mask2):
                return False
            n_bytes -= 1

    return n_bytes == 0