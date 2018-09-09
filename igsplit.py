#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:53:29 2018

@author: Sal Garcia
"""

import imageio
import numpy as np

ratio_height = 5
ratio_width  = 4
file_name='IMG_0178.jpg'
im = imageio.imread(file_name)
print(im.shape)
cols_needed=np.floor(im.shape[0]*(ratio_width/ratio_height));
print(cols_needed)
col_start = 0;
col_end   = cols_needed-1;
end_image = 0;
counter = 1
while (col_end<=im.shape[1]-1)  : 
    print([col_start ,col_end])
    new_file_name=file_name[0:-4] + '_' + str(counter)+'.jpg'
    counter = counter +1;
    print(new_file_name)
    imageio.imwrite(new_file_name,im[:,int(col_start):int(col_end),:],format='jpg',quality=100)
    col_start = col_end+1;
    if (col_end + cols_needed > im.shape[1]-1) and end_image==0:
        col_end = im.shape[1]-1
        end_image = 1
    else :   
        col_end = col_end + cols_needed;
        

  
#