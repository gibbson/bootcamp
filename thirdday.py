import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', )
xa_low = np.loadtxt('data/xa_low_food.csv', )

def xa_high_diaameter(xa):
    """
    Convert an array of cross_sectional areas to diameters with commuensurate units
    """

    # Compute diameter from area
    # A = pi * d^2 / 4
    diameter = np.sqrt(xa * 4 / np.pi)
    
    return diameter
