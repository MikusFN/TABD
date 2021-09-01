from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111)
#ax1 = plt.subplot2grid((5,4), (0,0))
#ax2 = plt.subplot2grid((5,4), (1,1))
##ax3 = plt.subplot2grid((5,4), (2, 2))
##ax4 = plt.subplot2grid((5,4), (3, 3))
##ax5 = plt.subplot2grid((5,4), (4, 0))
map = Basemap(projection='cyl', 
              lat_0=0, lon_0=0)

map.shadedrelief()
map.drawcoastlines(color='gray')
map.drawcountries(color='gray')
map.drawstates(color='gray')

lons = np.array([-13.7, -10.8, -13.2, -96.8, -7.99, 7.5, -17.3, -3.7])
lats = np.array([9.6, 6.3, 8.5, 32.7, 12.5, 8.9, 14.7, 40.39])
cases = np.array([1971, 7069, 6073, 4, 6, 20, 1, 1])
places = np.array(['Guinea', 'Liberia', 'Sierra Leone','United States', 'Mali', 'Nigeria', 'Senegal', 'Spain'])

x, y = map(lons, lats)

map.scatter(x, y, s=cases, c='r', alpha=0.5)

axins = zoomed_inset_axes(ax, 14, loc=2)
#axins.set_xlim(-20, 0)
#axins.set_ylim(3, 18)

plt.xticks(visible=False)
plt.yticks(visible=False)

map2 = Basemap(llcrnrlon=-10,llcrnrlat=35,urcrnrlon=-6,urcrnrlat=45, ax=axins, resolution='h')
map2.shadedrelief()
map2.drawcoastlines(color='gray')
map2.drawcountries(color='gray')
map2.drawstates(color='gray')

map2.scatter(x, y, s=cases/5., c='r', alpha=0.5)

mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

#axins2 = zoomed_inset_axes(ax, 14, loc=1)
###axins.set_xlim(-20, 0)
###axins.set_ylim(3, 18)


#map3 = Basemap(llcrnrlon=-8,llcrnrlat=35,urcrnrlon=-9,urcrnrlat=45, ax=axins2, resolution='h')
##map3.drawmapboundary(fill_color='#7777ff')
##map3.fillcontinents(color='#ddaa66', lake_color='#7777ff', zorder=0)
##map3.drawcoastlines()
##map3.drawcountries()

##map3.scatter(x, y, s=cases/5., c='r', alpha=0.5)

#mark_inset(ax, axins2, loc1=2, loc2=4, fc="none", ec="0.5")

plt.show()