import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import matplotlib.font_manager
import matplotlib.patheffects as PathEffects
#-----------------------------------------------------------------------------------------------------------------------
"""Initialising the DataFrame"""
#Allow the DataFrame to be visible in output window
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

#Creating the DataFrame
df = pd.read_csv('INSERT PATHWAY HERE', engine='python')

#Print df
print(df)

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Variables we can call"""
#Font
MyFont = 'DIN Alternate'

#Colours
colors = ['#f7ff74', '#5370ff', '#fb8585', '#0f9d58', '#c2a7ef']

#Width of Bars
width=0.35
#-----------------------------------------------------------------------------------------------------------------------
"""Creating the figure"""
#Figure with one subplot
fig, ax1 = plt.subplots()

#-----------------------------------------------------------------------------------------------------------------------
"""PLOTTING"""
#Plotting the x ticks properly (and spacing) and creating a varaible to use later on
x = np.arange(len(df['COLUMN WE ARE SPLITTING BY']))
ax1.set_xticks(x)
ax1.set_xticklabels(df['COLUMN WE ARE SPLITTING BY'])

# Note we add the `width` parameter now which sets the width of each bar.
b1 = ax1.bar(x, df['COLUMN OF INVESTIGATION'],width=width, color='#f7ff74', alpha=1, zorder=5, label='LABEL')

#-----------------------------------------------------------------------------------------------------------------------
"""Title and Axes"""
#Writing Title
p = ax1.set_title("TITLE", color='w', font=MyFont, fontsize=16, fontweight='bold', loc='right')
p.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#X label (across)
q = ax1.set_xlabel("HOW WE SPLIT THE DATA", font=MyFont, fontsize=14, fontweight='bold', color='w')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Y label (up)
s = ax1.set_ylabel("WHAT ARE WE COUNTING / LOOKING AT", font=MyFont, fontsize=14, fontweight='bold', color='w')
s.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Adding tag
t = plt.text(-0.655 , -5, '@obdftbl / Data Provided by FBref', font=MyFont, fontstyle='italic', fontsize=9, color='white')
t.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='black')])

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

#-----------------------------------------------------------------------------------------------------------------------
"""Other plotting stuff"""
#Grid
ax1.grid(True, alpha=0.3, zorder=1)

ax1.tick_params('x', bottom=False)

#Changing xTicks font and alignment
for label in ax1.get_xticklabels():
    label.set_fontproperties(MyFont)
    label.set_horizontalalignment('center')

#Changing yTicks font
for label in ax1.get_yticklabels():
    label.set_fontproperties(MyFont)

#Setting y Lim
ax1.set_ylim(0,70)

#Labelling the Bars on top of the bars
def autolabel(Bars):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for Bar in Bars:
        height = Bar.get_height()
        ax1.annotate('{}'.format(height),
                    xy=(Bar.get_x() + Bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', font=MyFont, color='w')
autolabel(b1)

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()