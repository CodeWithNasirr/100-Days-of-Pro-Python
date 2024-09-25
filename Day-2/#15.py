def do_overlap(L1, R1, L2, R2):
    # Extract coordinates
    x1, y1 = L1  # Top-left corner of rectangle 1
    x2, y2 = R1  # Bottom-right corner of rectangle 1
    x3, y3 = L2  # Top-left corner of rectangle 2
    x4, y4 = R2  # Bottom-right corner of rectangle 2
    
    # Check if one rectangle is to the left of the other
    if x2 < x3 or x4 < x1:
        return False
    
    # Check if one rectangle is above the other
    if y1 < y4 or y3 < y2:
        return False
    
    return True

# Example usage
L1 = (0, 10)  # Top-left corner of rectangle 1
R1 = (10, 0)  # Bottom-right corner of rectangle 1
L2 = (5, 5)   # Top-left corner of rectangle 2
R2 = (15, 0)  # Bottom-right corner of rectangle 2

if do_overlap(L1, R1, L2, R2):
    print("Rectangles overlap")
else:
    print("Rectangles do not overlap")
