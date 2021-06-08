import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import squarify
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
#Create our plot and resize it.
fig = plt.gcf()
ax = fig.add_subplot()
fig.set_size_inches(16, 4.5)

#-----------------------------------------------------------------------------------------------------------------------
"""Creating Variables we can call"""
#Font
MyFont = 'DIN Alternate'

#-----------------------------------------------------------------------------------------------------------------------
"""Plotting Points"""
#Utilise matplotlib to scale our goal numbers between the min and max, then assign this scale to our values.
norm = matplotlib.colors.Normalize(vmin=min(dataframe["COLUMN WE ARE INVESTIGATING"]),
                                   vmax=max(dataframe["COLUMN WE ARE INVESTIGATING"]))
colors = [matplotlib.cm.cividis(norm(value)) for value in dataframe["COLUMN WE ARE INVESTIGATING"]]

#Can create a list like this to use for the label. Then just pass in label = labels in squarify.plot
labels = ['Arsenal\n73','Bournemouth\n45','Brighton\n33','Burnley\n35','Chelsea\n60','Crystal Palace\n44',
          'Everton\n42','Huddersfield\n25','Leicester City\n53','Liverpool\n82','Manchester City\n103','Manchester Utd\n67',
          'Newcastle Utd\n38','Southampton\n36','Stoke City\n34','Swansea City\n27','Tottenham\n70','Watford\n42','West Brom\n31',
          'West Ham\n48']

#Use squarify to plot our data, label it and add colours. We add an alpha layer to ensure black labels show through
squarify.plot(label=dataframe["COLUMN WE ARE USING TO SPLIT THE DATA"],
              sizes=dataframe["COLUMN WE ARE INVESTIGATING"], color = colors, alpha=.6,
              text_kwargs={'fontsize':30, 'font':MyFont, 'color':'w'},
              linewidth=2, edgecolor='#e4ea91')

#-----------------------------------------------------------------------------------------------------------------------
"""Titles and Tags"""
#Title
q = plt.title("TITLE", color='white', font=MyFont, fontsize=16, fontweight='bold', loc='center')
q.set_path_effects([PathEffects.withStroke(linewidth=2.25, foreground='black')])

#Tag and Data
t = ax.text(0, -10, '@obdftbl / Data Provided by FBref', font=MyFont, fontstyle='italic', fontsize=12, color='w')
t.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='black')])

#-----------------------------------------------------------------------------------------------------------------------
"""Making the graph look nice"""
# Add the background colour
ax.set_facecolor('#5c5c5c')
fig.patch.set_facecolor('#5c5c5c')

#Remove our axes and display the plot
plt.axis('off')

#-----------------------------------------------------------------------------------------------------------------------
"""Other plotting stuff"""
#Grid
ax.grid(True, alpha=0.2)

#Tight layout
plt.tight_layout()

#-----------------------------------------------------------------------------------------------------------------------
"""Showing the Graph"""
#Show the graph
plt.show()