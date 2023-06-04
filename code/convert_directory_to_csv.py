# coding: utf-8
from pathlib import Path
import pandas as pd

dwi_mask_dir = Path('/mnt/HDD16TB/till/ingrid/')
masks = [f for f in dwi_mask_dir.glob('**/*') if f.is_file() and 'mask' in f.name]

subjects = []
for s in masks:
    s_id = s.parts[5]
    subjects.append(s_id)
    
pd.DataFrame({'subject-id':subjects, 'DWI-segmentation':True})

pd.DataFrame({'subject-id':subjects, 'DWI-segmentation':True}).to_csv('DWI_segmentations.csv')
