#!/usr/bin/env python3
from flask import make_response, abort, jsonify

from functions import load_data

# Data to serve with our API
df = load_data()

def read_all():
    """
    This function responds to a request for /api/cereals
    with the complete lists of cereals
    :return:        json string of list of cereals
    """
    return [{'time': row['time'], 'name': row['cereal'], 'yield_map': [[float(row_map) for row_map in col_map] for col_map in row['yield_map'].data]} for index, row in df.iterrows()]


def read_mean():
    tmp = df.groupby(["time"]).agg({"time": "first", "yield_mean": "mean"})

    return [[k, v] for k, v in tmp["yield_mean"].items()]


def read_mean_cereal(name):
   tmp = df.groupby(['cereal']).get_group(name)[['time', 'yield_mean']]

   return [[row[0], row[1]] for index, row in tmp.iterrows()]
