import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
import matplotlib.patheffects as PathEffects

#-----------------------------------------------------------------------------------------------------------------------
"""Initialising the DataFrame"""
#Creating the DataFrame
df = pd.read_csv('FILE PATHWAY', engine='python')

#So we can see the whole DataFrame in the output
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

#-----------------------------------------------------------------------------------------------------------------------
"""Getting Quartile Lines"""
#Getting the median for one column
MedianX = df['COLUMN 1'].median()
print(MedianX)
Q1 = df['COLUMN 1'].quantile(0.25)
Q2 = df['COLUMN 1'].quantile(0.5)
Q3 = df['COLUMN 1'].quantile(0.75)
print(Q1, Q2, Q3)

#-----------------------------------------------------------------------------------------------------------------------
"""Creating the Figure"""
#Plotting the figure with one subplot
fig, ax = plt.subplots(figsize=(5,2))

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Variables we can call"""
#Creating a list we can append player names to
players = []
#Font
MyFont = 'DIN Alternate'

#Colours we will use for each violin
colors = ['#f7ff74', '#5370ff', '#fb8585', '#0f9d58', '#c2a7ef']

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

#X Lim
plt.xlim(1, 7)

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Quartile Lines"""
#Creating the 25,50,75 quartile lines
x1, y1 = [1.85, 1.85], [-2000,2000]
x2, y2 = [2.31, 2.31], [-2000,2000]
x3, y3 = [3.03, 3.03], [-2000,2000]

#Plotting such lines
plt.plot(x1, y1, x2, y2, x3, y3, color='w', linestyle='dashed', alpha=0.3, zorder=1)

#-----------------------------------------------------------------------------------------------------------------------
"""Titles and Axes"""
#Title
p = ax.set_title("TITLE \n@obdftbl / Data Provided by FBref", color='w', font=MyFont, fontsize=16, fontweight='bold', loc='right')
p.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#X title /// no need for Y title really
q = ax.set_xlabel("X TITLE", font=MyFont, fontsize=14, fontweight='bold', color='w')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points"""
#Plotting main points
ax = sns.swarmplot(x=dfFW['COLUMN 1'], color='#fb8585', alpha=0.5, size=7, edgecolor='k', linewidth=1)

#Plotting our point of interest
ax = sns.swarmplot(x=dfPLAYER['COLUMN 1'], color='#f7ff74', alpha=0.7, size=8, edgecolor='k', linewidth=2)

#Plotting the name of our point of interest
ax = ax.annotate('PLAYER NAME', xy=(dfPLAYER['COLUMN 1'], 0), size=8, font=MyFont, color='#f7ff74', zorder=4)

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()