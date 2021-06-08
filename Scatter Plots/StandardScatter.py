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
dfPrem = pd.read_csv('INSERT PATHWAY HERE', engine='python')

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

#List to append player names to
players = []
WhoIsInHere = []

#Colours
colors = ['#f7ff74', '#5370ff', '#fb8585', '#0f9d58', '#c2a7ef']

#-----------------------------------------------------------------------------------------------------------------------
"""Getting median lines to plot"""
#Getting the median for X axes
MedianX = dfAll['COLUMN OF INTEREST 1'].median()
print(MedianX)

#Getting the median for Y axes
MedianY = dfAll['COLUMN OF INTEREST 2'].median()
print(MedianY)

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points and Names"""
#Creating a for loop to loop over the columns we want and plot the data
for index, row in dfAll.iterrows():
    #Player names column
    player_name = row[2]
    #X axes column
    xAxes = row[28]
    #Y Axes column
    yAxes = row[26]

    #Plotting specifics based on values
    if player_name == 'PLAYER OF INTEREST 1':
        ax.scatter(xAxes, yAxes, c='yellow', s=55, alpha=0.8, edgecolors='k', zorder=6)
        players.append(ax.annotate(player_name, xy=(xAxes, yAxes), size=8, font=MyFont, color='#f9ff92', zorder=4))

    #Plotting Names due to them being high ability points
    elif xAxes >= 0.24 or yAxes >= 0.55:
            ax.scatter(xAxes, yAxes, c='#5370ff', s=40, alpha=0.5, edgecolors='k', zorder=6)
            players.append(ax.annotate(player_name, xy=(xAxes, yAxes), size=8, font=MyFont, color='w', zorder=4))

    #CAN ALSO CREATE BOXES TO HIGHLIGHT NAMES WITHIN. //// EG. OVER AND UNDER X AXES POINTS / OVER AND UNDER Y AXES POINTS

    #Else just plot but not of interest
    else:
        ax.scatter(xAxes, yAxes, c='white', alpha=0.3, zorder=5)
        #Seeing who is in here
        WhoIsInHere.append(player_name)

#Printing that list so we can see
print(WhoIsInHere)

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

#Changing x ticks fonts
for label in ax.get_xticklabels():
    label.set_fontproperties(MyFont)
#Changing y tick fonts
for label in ax.get_yticklabels():
    label.set_fontproperties(MyFont)

#-----------------------------------------------------------------------------------------------------------------------
"""Other plotting stuff"""
#Grid
ax.grid(True, alpha=0.25)

#X and Y limits
plt.xlim(0,0.45)
plt.ylim(0,0.8)

#-----------------------------------------------------------------------------------------------------------------------
"""Titles and Axes"""
#SubText for Tag and Data
t = ax.text(0, -0.05, '@obdftbl / Data Provided by FBref', font=MyFont, fontstyle='italic', fontsize=9, color='white')
t.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='black')])

#Creating where the title starts
myx = 0.09
myY = 0.815

#Creating that title and spacing it correctly
myText1 = ax.text(myx,myY, 'PLAYER OF INTEREST 1', font=MyFont, color='#f9ff92', fontsize=16)
myText2 = ax.text(myx+0.040,myY, 'Y AXES THEN X AXES', font=MyFont, color='white', fontsize=16)
myText3 = ax.text(myx+0.330,myY, 'AGAINST WHO WE ARE COMPARING TO', font=MyFont, color='#5370ff', fontsize=16)

#Adding background to title
myText1.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])
myText2.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])
myText3.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#X label
q = ax.set_xlabel("X LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Y label
s = ax.set_ylabel("Y LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
s.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Median lines"""
#Creating x line
x1, y1 = [0.14, 0.14], [0, 100]

#Creating y line
x2, y2 = [0, 100], [0.25, 0.25]

#Plotting those lines
plt.plot(x1, y1, x2, y2, color='c', linestyle='dashed', alpha=0.55)

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()

