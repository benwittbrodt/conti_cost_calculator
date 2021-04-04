# Pandas for data handling (if needed)
import pandas as pd


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


def break_even_calc(var_dict):

    # Getting all values in a list
    tire_list = [var_dict[ii] for ii in var_dict]
    tire_list_names = [ii for ii in var_dict]

    # Finding the None index - returning the first item
    empty = [ii for ii in range(len(tire_list)) if tire_list[ii] == None][0]

    # Using the index to compute the value
    if empty == 0:
        break_variable = tire_list[1] / (tire_list[3] / tire_list[2])
    elif empty == 1:
        break_variable = tire_list[0] * (tire_list[3] / tire_list[2])
    elif empty == 2:
        break_variable = tire_list[3] / (tire_list[1] / tire_list[0])
    else:
        break_variable = tire_list[2] * (tire_list[1] / tire_list[0])

    return tire_list_names[empty], break_variable


# Running it
print(break_even_calc(var_dict))
