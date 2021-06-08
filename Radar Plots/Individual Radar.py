import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import matplotlib.font_manager
import matplotlib.patheffects as PathEffects
import re
from adjustText import adjust_text
from RadarTemplate import Radar

#-----------------------------------------------------------------------------------------------------------------------
"""Setting up the Radar Parameters"""
#Parameter Names
params = ['VARIABLE_ONE', 'VARIABLE_TWO', 'VARIABLE_THREE', 'VARIABLE_FOUR', 'VARIABLE_FOUR']

#Range Values for each parameters
ranges = [(0.0, 0.15), (0.0, 1), (75,100), (0, 3), (0,0.5)]

#Parameter Values
values = [0.11,0.53,88,2.04, 0.26]

#-----------------------------------------------------------------------------------------------------------------------
"""Titles and Endnotes"""
#Title values
title = dict(
    title_name = 'PLAYER NAME',
    title_color = 'w',
    subtitle_name = 'CLUB',
    subtitle_color = 'w',
    title_name_2 = 'SEASON',
    title_color_2 = 'w',
    subtitle_name_2 = 'POSITION',
    subtitle_color_2 = 'w',
    title_fontsize = 18,
    subtitle_fontsize = 15)

#Add an endnote
endnote = '@obdftbl / Data Provided by FBref \nAll units standardised per90'

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
#Radar colourings
radar = Radar(background_color='#5c5c5c', patch_color='#28252C', label_color='#28252C', range_color='#FFFFFF',
              range_fontsize=9, label_fontsize=14,)

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points"""
#Plotting the above
fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values, radar_color=['#763892', '#996fab'], title=title,
                           endnote=endnote, end_color='w', )

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()