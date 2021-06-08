import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import matplotlib.font_manager
import matplotlib.patheffects as PathEffects
import re
from adjustText import adjust_text

#-----------------------------------------------------------------------------------------------------------------------
"""Initialising the DataFrame"""
#Creating the DataFrame
dfPrem = pd.read_csv('FILE PATHWAY HERE', engine='python')

#Allow the DataFrame to be visible in output window
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

#-----------------------------------------------------------------------------------------------------------------------
"""Creating the Figure"""
#Plotting the figure with one subplot
fig, ax = plt.subplots()

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Variables we can call"""
#Font
MyFont = 'DIN Alternate'

#Colours we will use for each violin
colors = ['#f7ff74', '#5370ff', '#fb8585', '#0f9d58', '#c2a7ef']

#Lists
players = []
whoIsin = []

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points"""
#Choosing colours to distinguish the player of interest.
# First colour is the player of interest, second colour is the rest
my_color = np.where(df['COLUMN WE ARE USING TO DISTINGUISH (EG. PLAYER)'] == 'PLAYER OF INTEREST', 'yellow', 'skyblue')

#WE CAN ALSO CREATE A LIST IN THE ORDER OF OUR BARS COLOURS THAT WE WANT
#Create an array of equal length to our bars
#Each value is the hex code for the team's colours, in order of our chart
teamColours = ['#034694','#001C58','#5CBFEB','#D00027',
              '#EF0107','#DA020E','#274488','#ED1A3B',
               '#000000','#091453','#60223B','#0053A0',
               '#E03A3E','#1B458F','#000000','#53162f',
               '#FBEE23','#EF6610','#C92520','#BA1F1A']


# Note here is where you define how it will be coloured using either of the above
#Adding a scatterpoint to the end of the vertical line
plt.scatter(df['WHAT ARE WE LOOKING AT'], df['COLUMN WE ARE USING TO DISTINGUISH (EG. PLAYER)'], color=my_color, s=20, alpha=1)

# Adding text to the end of each lollipop
for i, v in enumerate(df['WHAT ARE WE LOOKING AT']):
    ax.text(v+0.01, i , str(v), color='k', size=7)

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
# Add the background colour
ax.set_facecolor('#5c5c5c')
fig.patch.set_facecolor('#5c5c5c')

# Set spines
ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', colors='white')

#-----------------------------------------------------------------------------------------------------------------------
"""Other plotting stuff"""
#Grid
ax.grid(True, alpha=0.25)

#X Lim (no need for Y lim as that is nominal
ax.set_xlim(0,1.8)

#Changing x ticks fonts
for label in ax.get_xticklabels():
    label.set_fontproperties(MyFont)
#Changing y tick fonts
for label in ax.get_yticklabels():
    label.set_fontproperties(MyFont)

# -----------------------------------------------------------------------------------------------------------------------
"""Title and Axes"""
# Writing Title
p = ax.set_title("INSERT TITLE HERE", color='w', font=MyFont, fontsize=16, fontweight='bold', loc='right')
p.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#X label (across)
s = ax.set_xlabel("X LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
s.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Y label (vertical)
q = ax.set_ylabel("Y LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

# Tag and Data
t = ax.text(0, -5, '@obdftbl / Data Provided by FBref', font=MyFont, fontstyle='italic', fontsize=12, color='white')
t.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='black')])

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()