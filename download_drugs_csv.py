#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 12:46:00 2018

@author: fangyucheng
"""

import time
import urllib
import pandas as pd

df = pd.read_csv("state_full_short_name.csv")

shortName_list = df["shortname"].tolist()

# initiate downloader
opener = urllib.request.build_opener()
urllib.request.install_opener(opener)
for state in shortName_list:
    url = ("https://www.dea.gov/clan_lab/export/dea_clan_lab_export.csv?state=%s"
           "&date=&_wrapper_format=drupal_ajax" % state)
    csv_name = "%s.csv" % state
    urllib.request.urlretrieve(url, csv_name)
    time.sleep(5)
    print(url)

