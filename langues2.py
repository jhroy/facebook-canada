# coding: utf-8
# ©2020 Jean-Hugues Roy. GNU GPL v3.

import csv
import pandas as pan
import numpy as np

fichIn = "canada-avec-langues.csv"

f1 = pan.read_csv(fichIn, names = ["page","code","fbID","pageLikes","date","annee","mois","jour","postID","message","texteImage","texteLien","desc","sponsor","sponsorID","typePost","statutVideo","dureeVideo","vuesPost","vuesTotal","vuesTotalCrossposts","partages","likes","love","wow","haha","triste","colere","solid","commentaires","interactions","media","langue"], low_memory=False)
f1.fbID = f1.fbID.astype(str)
pan.pivot_table(f1,index=["fbID","page","code"],values=["interactions"],aggfunc=[len],columns=["langue"],fill_value=0).to_csv("tablo-croise-langues.csv")
