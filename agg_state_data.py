#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:58:41 2019

@author: fangyucheng
Email: 664947387@qq.com
"""


import pandas as pd

df = pd.read_csv("state_full_short_name.csv")

shortName_list = df["shortname"].tolist()

new_df = pd.DataFrame()

for state in shortName_list:
    state_df = pd.read_csv("%s.csv" % state)
    new_df = new_df.append(state_df)
    print(len(new_df))

new_df.to_csv("agg_data.csv", encoding="UTF-8", index=False)