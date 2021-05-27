def num_layers(n):
    thickess = 0.5
    total_thickness = thickess * 2**(n)
    return str(total_thickness/1000) + 'm'

# def num_layers(n):
# 	return str(0.0005 * 2**n) + "m"

    # Create a function that returns the thickness (in meters) 
    # of a piece of paper after folding it n number of times. 
    # The paper starts off with a thickness of 0.5mm