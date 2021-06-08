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

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Variables we can call"""
#Font
MyFont = 'DIN Alternate'

#Colours
colors = ['#f7ff74', '#5370ff', '#fb8585', '#0f9d58', '#c2a7ef']

#-----------------------------------------------------------------------------------------------------------------------
"""Creating the figure"""
#Figure with one subplot
fig, ax1 = plt.subplots()

#-----------------------------------------------------------------------------------------------------------------------
"""PLOTTING"""
#Plotting the kde Plot (Density one)
sns.kdeplot(data=df_new, x='WHAT WE WANT TO MEASURE', hue="HOW WE WANT TO SPLIT THE HISTOGRAMS", palette=colors, bw_adjust=.7, fill=True, alpha=0.15)

#Placing a rug with it too
sns.rugplot(data=df_new, x='WHAT WE WANT TO MEASURE', hue="HOW WE WANT TO SPLIT THE HISTOGRAMS", palette=colors, expand_margins=True)

#-----------------------------------------------------------------------------------------------------------------------
"""Title and Axes"""
#Writing Title
p = ax1.set_title("INSERT TITLE HERE", color='w', font=MyFont, fontsize=16, fontweight='bold', loc='right')
p.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#X label (across)
q = ax1.set_xlabel("X LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Y label (up)
s = ax1.set_ylabel("Y LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
s.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
# Add the background colour
ax1.set_facecolor('#5c5c5c')
fig.patch.set_facecolor('#5c5c5c')

# Set spines + Ticks
ax1.spines["bottom"].set_color("white")
ax1.spines["left"].set_color("white")
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='both', colors='white')

#Changing x ticks fonts
for label in ax1.get_xticklabels():
    label.set_fontproperties(MyFont)
#Changing y tick fonts
for label in ax1.get_yticklabels():
    label.set_fontproperties(MyFont)

#-----------------------------------------------------------------------------------------------------------------------
"""Other plotting stuff"""
#Grid
ax1.grid(True, alpha=0.2)

#Limits
ax1.set_xlim(0,2000)
ax1.set_ylim(0,2000)

#Tight Layout
plt.tight_layout()

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()
