import numpy as np
import os


def Check_energy_conservation(prod_p=None, load_p=None, p_or=None, p_ex=None, tolerance=1e-3):
    """
    this function verifies the law of conservation of energy (LCE) that says : productions = load + loss

    params
    ------
        prod_p: `array`
            the active power of production points in power network

        load_p: `array`
            the active power of load poins in power network

        p_or: `array`
            the active power of the origin side of power lines

        p_ex: `array`
            the active power of the extremity side of power lines

        tolerance: `float`
            a threshold value used to compare the value of the law, and below which the verification is failed

    Returns
    -------
        LCE: `array`
            an array including the law of conservation of energy values stored for each step (observation)

        violation_percentage: `scalar`
            a value expressed in percentage to indicate the percentage of 

        failed_indices: `array`
            an array giving the indices of observations that not verify the law given the indicated tolerance

    """
    print("************* Check Energy Conservation *************")

    productions = np.sum(prod_p, axis=1)
    loads = np.sum(load_p, axis=1)
    loss = np.sum(p_or + p_ex, axis=1)

    LCE = productions - loads - loss
    failed_indices = np.array(np.where(abs(LCE) > tolerance)).reshape(-1, 1)
    violation_percentage = (len(failed_indices) / len(LCE))*100
    print("Number of failed cases is {} and the proportion is {:.3f}% : ".format(
        len(failed_indices), violation_percentage))

    return LCE, violation_percentage, failed_indices
