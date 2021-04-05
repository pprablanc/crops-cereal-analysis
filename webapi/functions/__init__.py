#!/usr/bin/env python3


import os
import pandas as pd
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt


def load_data():
    '''Description: load netcdf4 files, store it in a dataframe and preprocess the data.

    Return: df (DataFrame):
                columns:
                    'time'      (int):                  row year
                    'cereal'    (str):                  cereal type
                    'yield_map' (numpy masked array):   yield map
                    'mean_yield' (str):                 mean yield for a given map
    '''
    full_dataset = dict(time=[], cereal=[], nc=[])
    path = "../data/raw"
    with os.scandir(path) as dir_data:
        for sub_dir_data in dir_data:
            for f in os.scandir(os.path.join(path, sub_dir_data.name)):
                path_f = os.path.join(path, sub_dir_data.name, f.name)
                time = int(f.name.split("_")[1][:4])
                full_dataset["time"].append(time)
                full_dataset["cereal"].append(sub_dir_data.name)
                full_dataset["nc"].append(nc.Dataset(path_f, "r"))
    df = pd.DataFrame(full_dataset

    # Dataset preprocessing

    # Sort data as they are messy when load with scandir
    df = df.sort_values(["cereal", "time"], ignore_index=True)  # sorting by time

    # Add a 'yield' column for display purpose
    # Remask with -1/0 to avoid flatten amplitude
    mask_value = 0
    list_var = []
    for row in df["nc"]:
        row_tmp = row["var"][:]
        row_tmp.set_fill_value(-mask_value)
        mask = row_tmp.mask
        list_var.append(np.ma.masked_array(row_tmp.filled(fill_value=-mask_value), mask))
    df["yield_map"] = list_var

    # add yield_mean to avoid repeating code
    df["yield_mean"] = df["yield_map"].apply(lambda row: row.data.mean())
    df_by_cereal = df.groupby(["cereal"])

    # nc column not necessary anymore
    df.drop("nc", axis="columns", inplace=True)
    return df
