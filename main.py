# Pandas for data handling (if needed)
import pandas as pd
from sympy import *
import numpy

# Declare variables for tires
# not being used at the moment as just the bottom list to simplify and make work
conti_tires = {
    "steer": {
        "name": "HS3",
        "price": 325,
        "miles": 150000,
        "tread": 19,
    },
    "drive": {
        "name": "HDL2",
        "price": 290,
        "miles": 260000,
        "tread": 26,
    },
    "trailer": {
        "name": "HT3",
        "price": 225,
        "miles": 140000,
        "tread": 13,
    },
}
competitor_tires = {
    "steer": {
        "name": "XLEZ",
        "price": 400,
        "miles": 170000,
        "tread": 19,
    },
    "drive": {
        "name": "XLED",
        "price": 340,
        "miles": 295000,
        "tread": 26,
    },
    "trailer": {
        "name": "XLET",
        "price": 250,
        "miles": 150000,
        "tread": 13,
    },
}
truck_types = {
    "6x4": [2, 8, 0],
    "4x2": [2, 4, 0],
    "0x4": [0, 0, 8],
}
# Declare variables for use in functions
c_steer_p = 350
c_steer_m = 150000
com_steer_p = 400
com_steer_m = None  # 170000 --Is none so the solving works


var_dict = {
    "conti steer mileage": c_steer_m,
    "conti steer price": c_steer_p,
    "competitor steer mileage": com_steer_m,
    "competitor steer price": com_steer_p,
}


# Define symbols for calculation equation
x, y, a, b = symbols("x y a b")


def break_even_calc():

    comparison_expr = (x / y) - (a / b)
    known_vars = [(x, c_steer_p), (y, c_steer_m), (a, com_steer_p), (b, com_steer_m)]
    comparison_expr_solve = solve(comparison_expr.subs(known_vars))

    break_even = float(comparison_expr_solve[0])
    for key in var_dict:
        if var_dict[key] == None:
            break_variable = key
    return break_even, break_variable  # make this the unknown_val


break_even, break_variable = break_even_calc()


print(break_variable, break_even)
