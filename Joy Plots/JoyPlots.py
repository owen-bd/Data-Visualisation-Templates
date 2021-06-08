import joypy
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.patheffects as PathEffects

#-----------------------------------------------------------------------------------------------------------------------
"""Initialising the DataFrame"""
#Creating the DataFrame
dataframe = pd.read_csv("INSERT PATHWAY HERE")

#Allow the DataFrame to be visible in output window
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Variables we can call"""
#Font
MyFont = 'DIN Alternate'

#-----------------------------------------------------------------------------------------------------------------------
"""Creating the Figure + Plotting the Points"""
#Plotting the figure with one subplot and plotting all of those values
#Dataframe = Dataframe you will use - Good if the dataframe here is extremely clean (ie. just of the two leagues / clubs
# / players you want to compare
#Column - What do we want to look at - Good here if you have renamed the columns as that is what will be used to name them.
#Rest are pretty self explanatory

fig, ax = joypy.joyplot(dataframe, column=['COLUMN 1', 'COLUMN 2', 'COLUMN 3', 'COLUMN 4',
                                           'COLUMN 5', 'COLUMN 6', 'COLUMN 7', 'COLUMN 8'],
                        background='#5c5c5c',
                        ylabels=True, xlabels=True, figsize=(10,5),
                        color='#5370ff', linecolor='w', grid=True)

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
# Add the background colour
fig.patch.set_facecolor('#5c5c5c')

#Title
q = plt.title('TITLE', fontsize=14, color='w', alpha=1, loc='right')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Y Label
s = plt.xlabel("Y LABEL", font=MyFont, fontsize=14, fontweight='bold', color='w')
s.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()