#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:07:05 2022

@author: vincent
"""

from pfafhydrocode import updwn, upstream, downstream

import time
import pandas as pd

## Example from wikipedia
## 8835 is upstream of segments 8833 and 8811,
## but not segments 8832, 8821 or 9135
dwn = [8833, 8811, 8832, 8821, 9135]
res = [updwn(8835,x) for x in dwn]

print(res)

## Example on a subset of the HydroSHEDS dataset (With the Rhine as Mainbasin).
df = pd.read_csv('data/hybas_eu_lev00_v1c_rhine.csv')

a = 23267093

#upstream
start = time.time()
mask = [upstream(a,b,oddOrZero=True) for b in df['PFAF_8']]
bas = df[mask]
end = time.time()
print('Upstream takes:',end-start)

bas.to_csv('data/example_results/downstream_affected.csv')

#downstream
start = time.time()
mask = [downstream(a,b,oddOrZero=True) for b in df['PFAF_8']]
bas = df[mask]

end = time.time()
print('Downstream takes:',end-start)

bas.to_csv('data/example_results/upstream_watershed.csv')