#!/usr/bin/env python3
from flask import make_response, abort, jsonify

from functions import load_data

# Data to serve with our API
df = load_data()

def read():
    """
    This function responds to a request for /api/cereals
    with the complete lists of cereals
    :return:        json string of list of cereals
    """
    # Create the list of people from our data
    return [{'name': name} for name in df['cereal'].unique()]
    # return [{'name': 'pouet'}, {'name': 'caca'}]


# def read_one(name):
#     """
#     This function responds to a request for /api/cereal/{name}
#     with one matching person from people
#     :param lname:   last name of person to find
#     :return:        person matching last name
#     """
#     if name in df['cereal'].unique():
#         cereal = name
#     # otherwise, nope, not found
#     else:
#         abort(
#             404, "Person with last name {cereal} not found".format(cereal=name)
#         )

#     return cereal



# def cereal():
#     cereal_trend = df.groupby(["time"]).agg({"time": "first", "yield_mean": "mean"})
#     data = [[k, v] for k, v in cereal_trend["yield_mean"].items()]

#     return jsonify({"status": "ok", "data": data})
