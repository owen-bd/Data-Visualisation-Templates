import joypy
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.patheffects as PathEffects

#-----------------------------------------------------------------------------------------------------------------------
"""Initialising the DataFrame"""
#Creating the DataFrame
df = pd.read_csv('INSERT PATHWAY HERE')

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
#By = How do you want to split the data (eg. by league, player, team) - Good to have renamed here also
#Rest are pretty self explanatory
#IT IS BEST TO KEEP COLUMN'S ON GRAPH TO 4 OR BELOW OTHERWISE IT CAN LOOK VERY CLUTTERED.

fig, ax = joypy.joyplot(df_new, column=['COLUMN ON GRAPH 1', 'COLUMN ON GRAPH 2', 'COLUMN ON GRAPH 3'],
                        by='COLUMN WE ARE USING TO SPLIT THE DATA (IE. ON THE Y AXIS SPLIT)',
                        background='#5c5c5c', ylabels=True, xlabels=True, legend=True, figsize=(10,5),
                        #COLOR HERE IS ASSIGNED TO COLUMNS ON GRAPH
                        color=['#5370ff','#0f9d58', '#f7ff74'], linecolor='w', grid=True, alpha=0.5)

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