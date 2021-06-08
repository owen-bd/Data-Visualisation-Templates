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
"""Creating Variables we can call"""
#Font
MyFont = 'DIN Alternate'

#-----------------------------------------------------------------------------------------------------------------------
"""Creating the Figure"""
#Plotting the figure with one subplot
fig, ax1 = plt.subplots()

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points and Names"""
#Plotting lineplot with different colours for each line
sns.lineplot(data=dfFull, x="COLUMN (USUALLY DATE)", y='WHAT WE WANT TO MEASURE', hue='HOW ARE WE SPLITTING THE DATA', palette=('#f7ff74', '#5370ff'), dashes=True, marker='o')

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
# Add the background colour
ax1.set_facecolor('#5c5c5c')
fig.patch.set_facecolor('#5c5c5c')

# Set spines
ax1.spines["bottom"].set_color("white")
ax1.spines["left"].set_color("white")
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='both', colors='white')

#-----------------------------------------------------------------------------------------------------------------------
"""Other plotting stuff"""
#Grid
ax1.grid(True, alpha=0.2)

#Tight layout
plt.tight_layout()

# Making x go tight so we aren't left with weird gaps.
plt.margins(0)

#Rotating xTicks so easier to read
plt.xticks(rotation=58)

#Changing x ticks fonts
for label in ax1.get_xticklabels():
    label.set_fontproperties(MyFont)
#Changing y tick fonts
for label in ax1.get_yticklabels():
    label.set_fontproperties(MyFont)

#-----------------------------------------------------------------------------------------------------------------------
"""Titles and Axes"""
#SubText for Tag and Data
t = ax.text(0, -0.05, '@obdftbl / Data Provided by FBref', font=MyFont, fontstyle='italic', fontsize=9, color='white')
t.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='black')])

#Title
p = ax1.set_title("TITLE",color='w', font=MyFont, fontsize=16, fontweight='bold', loc='right')
p.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#X Label
q = ax1.set_xlabel("X LABEL /// (PROBABLY DATES)", font=MyFont, fontsize=14, fontweight='bold', color='w')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Y Label
s = ax1.set_ylabel("Y LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
s.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Changing x and y tick fonts
for label in ax1.get_xticklabels():
    label.set_fontproperties(MyFont)

for label in ax1.get_yticklabels():
    label.set_fontproperties(MyFont)

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()