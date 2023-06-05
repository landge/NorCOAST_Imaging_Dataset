# coding: utf-8
from pathlib import Path
import pandas as pd

# dwi_mask_dir = Path('/mnt/HDD16TB/till/ingrid/')
stolav_36 = Path('/Volumes/Photo_BU/nc_36_mon_zips/StOlav_T3/')

stolav_all_36 = [f for f in stolav_36.glob('*.zip')]

subjects = []
for s in stolav_all_36:
    s_id = s.name.split('_')[0]
    subjects.append('sub-'+s_id)
    
pd.DataFrame({'subject-id':subjects, 'stolav_36':True}).to_csv('st_olav_36.csv')
