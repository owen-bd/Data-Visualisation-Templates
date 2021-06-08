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

## parameter value
values = [
    [0.11, 0.53, 0.70, 27.66, 1.05],  ## for PLAYER ONE
    [0.07, 0.36, 0.16, 32.14, 1.04]  ## for PLAYER TWO
]

#-----------------------------------------------------------------------------------------------------------------------
"""Titles and Endnotes"""
#Title values
title = dict(
    title_name='PLAYER ONE NAME',
    title_color='#9B3647',
    subtitle_name='PLAYER ONE CLUB',
    subtitle_color='#ABCDEF',
    title_name_2='PLAYER TWO NAME',
    title_color_2='#3282b8',
    subtitle_name_2='PLAYER TWO CLUB',
    subtitle_color_2='#ABCDEF',
    title_fontsize=18,
    subtitle_fontsize=15,
)

#Add an endnote
endnote = '@obdftbl / Data Provided by FBref \nAll units standardised per90'

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
#Radar colourings
radar = Radar(background_color="#121212", patch_color="#28252C", label_color="#F0FFF0",
              range_color="#F0FFF0")

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points"""
#Plotting the above
fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values,
                           radar_color=['#9B3647', '#3282b8'],
                           title=title, endnote=endnote,
                           alphas=[0.55, 0.5], compare=True)

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()