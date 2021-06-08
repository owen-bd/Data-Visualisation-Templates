import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import matplotlib.font_manager
import matplotlib.patheffects as PathEffects

#-----------------------------------------------------------------------------------------------------------------------
"""Initialising the DataFrame"""
#Creating the DataFrame
df = pd.read_csv('INSERT PATHWAY HERE', engine='python')

#Allow the DataFrame to be visible in output window
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

#-----------------------------------------------------------------------------------------------------------------------
"""Creating the Figure"""
#Plotting the figure with one subplot
fig1, ax1 = plt.subplots()

# Set up our plot area, then define the size
fig1.set_size_inches(14, 5)

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Variables we can call"""
#Colours we will use for each violin
colors = ['#f7ff74','#5370ff', '#fb8585', '#0f9d58', '#c2a7ef']

#Font
MyFont = 'DIN Alternate'

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points"""
#Use the names of the columns to plot what we want to plot
sns.violinplot(x="WHAT WE WANT TO SPLIT UP EG. NOMINAL (LEAGUE, TEAM)", y="WHAT WE WANT TO COMPARE", data=df_new, ax=ax1, palette=colors)

#-----------------------------------------------------------------------------------------------------------------------
"""Titles and Axes"""
#Title
ax1.set_title("TITLE", color='white', font=MyFont, fontsize=16, fontweight='bold', loc='right')

#X Label
q =ax1.set_xlabel("X LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Y Label
s = ax1.set_ylabel("Y LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
s.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Tag and Data
t = ax1.text(3.42, 3100, '@obdftbl / Data Provided by FBref', font=MyFont, fontstyle='italic', fontsize=12, color='w')
t.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='black')])

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
# Add the background colour
ax1.set_facecolor('#5c5c5c')
fig1.patch.set_facecolor('#5c5c5c')

# Set spines
ax1.spines["bottom"].set_color("white")
ax1.spines["left"].set_color("white")
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='both', colors='white')

# Set the font name for axis tick labels
for tick in ax1.get_xticklabels():
    tick.set_fontname(MyFont)
for tick in ax1.get_yticklabels():
    tick.set_fontname(MyFont)

#-----------------------------------------------------------------------------------------------------------------------
"""Other plotting stuff"""
#With seaborn have to use ax=ax1 to assign subplots in a figure
ax1.grid(linewidth=.23, zorder=1, color='k', alpha=0.4)

#Set y lim. No Need for X lim in violin plots
ax1.set_ylim(500)

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()