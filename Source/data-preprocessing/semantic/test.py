# -*- coding: utf-8 -*-

import csv
import pandas as pd

df = pd.read_csv("plz_linkname.csv")
df[["link"]] = df[["link"]].replace(to_replace=r' ', value='-', regex=True)
df[["link"]] = df[["link"]].replace(to_replace=r'Ä', value='ae', regex=True)
df[["link"]] = df[["link"]].replace(to_replace=r'ä', value='ae', regex=True)
df[["link"]] = df[["link"]].replace(to_replace=r'Ü', value='ue', regex=True)
df[["link"]] = df[["link"]].replace(to_replace=r'ü', value='ue', regex=True)
df[["link"]] = df[["link"]].replace(to_replace=r'Ö', value='oe', regex=True)
df[["link"]] = df[["link"]].replace(to_replace=r'ö', value='oe', regex=True)
df[["link"]] = df[["link"]].replace(to_replace=r'ß', value='ss', regex=True)
link = [i.lower() for i in pd.unique(df["link"])]

pd.DataFrame(link).to_csv("plz_link.csv", header = False, index = False)