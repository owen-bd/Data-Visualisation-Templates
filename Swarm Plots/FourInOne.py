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
"""Creating the Figure"""
#Plotting the figure with 4 subplots
fig, axes = plt.subplots(4,1)

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points"""
#Plotting Graph 1 w/ Point of Interest
ax = sns.swarmplot(x=df['COLUMN 1'], color='w', alpha=1, size=4, edgecolor='k', linewidth=1, ax=axes[0])
ax = sns.swarmplot(x=dfPLAYER['COLUMN 1'], color='#f7ff74', alpha=1, size=15, edgecolor='k', linewidth=2, ax=axes[0])

#Plotting Graph 2 w/ Point of Interest
ax2 = sns.swarmplot(x=df['COLUMN 2'], color='w', alpha=1, size=4, edgecolor='k', linewidth=1, ax=axes[1])
ax2 = sns.swarmplot(x=dfPLAYER['COLUMN 2'], color='#f7ff74', alpha=1, size=15, edgecolor='k', linewidth=2 , ax=axes[1])

#Plotting Graph 3 w/ Point of Interest
ax3 = sns.swarmplot(x=df['COLUMN 3'], color='w', alpha=1, size=4, edgecolor='k', linewidth=1, ax=axes[2])
ax3 = sns.swarmplot(x=dfPLAYER['COLUMN 3'], color='#f7ff74', alpha=1, size=15, edgecolor='k', linewidth=2 , ax=axes[2])

#Plotting Graph 4 w/ Point of Interest
ax4 = sns.swarmplot(x=df['COLUMN 4'], color='w', alpha=1, size=4, edgecolor='k', linewidth=1, ax=axes[3])
ax4 = sns.swarmplot(x=dfPLAYER['COLUMN 4'], color='#f7ff74', alpha=1, size=15, edgecolor='k', linewidth=2 , ax=axes[3])

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
#Full graph background colour
fig.patch.set_facecolor('#5c5c5c')

# Graph 1 Settings
ax.set_facecolor('#5c5c5c')
ax.set_xlabel("COLUMN 1")
ax.set_xlim(1,7)
ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', colors='white')

# Graph 2 Settings
ax2.set_facecolor('#5c5c5c')
ax.set_xlabel("COLUMN 2")
ax2.spines["bottom"].set_color("white")
ax2.spines["left"].set_color("white")
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.tick_params(axis='both', colors='white')

# Graph 3 Settings
ax3.set_facecolor('#5c5c5c')
ax.set_xlabel("COLUMN 3")
ax3.spines["bottom"].set_color("white")
ax3.spines["left"].set_color("white")
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.tick_params(axis='both', colors='white')

# Graph 4 Settings
ax4.set_facecolor('#5c5c5c')
ax.set_xlabel("COLUMN 4")
ax4.spines["bottom"].set_color("white")
ax4.spines["left"].set_color("white")
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.tick_params(axis='both', colors='white')

#-----------------------------------------------------------------------------------------------------------------------
"""Other plotting stuff"""
#Tight layout
plt.tight_layout()

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()