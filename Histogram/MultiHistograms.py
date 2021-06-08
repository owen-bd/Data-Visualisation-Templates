import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import matplotlib.font_manager
import matplotlib.patheffects as PathEffects

#-----------------------------------------------------------------------------------------------------------------------
"""Initialising the DataFrame"""
#Load DataFrame
df = pd.read_csv('INSERT PATHWAY HERE')

#Allow the DataFrame to be visible in output window
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

# -----------------------------------------------------------------------------------------------------------------------
"""Warping the DataFrame"""
#It is important we have many values for one column (Eg. Different team's pressing in attacking third across 8 games).
#How are we splitting the data
cols_to_plot = ['COLUMN1', 'COLUMN2', 'COLUMN3', 'COLUMN4', 'COLUMN5', 'COLUMN6']

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Variables we can call"""
#Font
MyFont = 'DIN Alternate'

#Colours
colors = ['#f7ff74', '#5370ff', '#fb8585', '#0f9d58', '#c2a7ef']

#-----------------------------------------------------------------------------------------------------------------------
"""Creating the figure"""
#Figure with 6 subplots subplots (increase this as per necessary)
fig, axs = plt.subplots(nrows=3, ncols=2)

#Setting size of figure
fig.set_size_inches(20, 10)

#Adjusting whitespace
fig.subplots_adjust(wspace=0.2)
fig.subplots_adjust(hspace=0.5)

#-----------------------------------------------------------------------------------------------------------------------
"""PLOTTING"""
#For loop to divide by the columns we want to plot and plot them in a subplot
for col, ax in zip(cols_to_plot, axs.flatten()):
    #Getting the individual columns
    IndivPlayer = df[col]

    #ACTUAL Plotting of the points
    sns.kdeplot(data=cols_to_plot,x=list(IndivPlayer), ax=ax, fill=True, color='#5370ff')
    sns.rugplot(data=cols_to_plot, x=list(IndivPlayer), ax=ax, color='k', expand_margins=True)

    #Setting the title
    ax.set_title(col, font=MyFont, fontsize=14)

    #Tick Params
    ax.tick_params(axis='x', labelrotation=30)
    ax.tick_params(axis='both', colors='white')

    #Spines
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Changing x ticks fonts
    for label in ax.get_xticklabels():
        label.set_fontproperties(MyFont)
    # Changing y tick fonts
    for label in ax.get_yticklabels():
        label.set_fontproperties(MyFont)

    #Facecolor
    ax.set_facecolor('#5c5c5c')

    #Limits
    ax.set_xlim(0,1)
    ax.set_ylim(0,4)

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
#Figure Title
fig.suptitle('SET TITLE', font=MyFont, fontsize=28,)

#Figure Color
fig.patch.set_facecolor('#5c5c5c')

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()