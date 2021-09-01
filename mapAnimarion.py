import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.basemap import Basemap


fig = plt.figure()
ax = fig.add_subplot(111)
m = Basemap(projection='lcc', resolution='h') 
            #lat_0=40, lon_0=-8,
            #width=0.5E6, height=0.7E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

lons = np.array([-13.7, -10.8, -13.2])
lats = np.array([9.6, 6.3, 8.5])
cases = np.array([1971, 7069, 20,])
places = np.array(['Porto', 'Lisboa', 'Coimbra'])

x, y = m(lons, lats)

m.scatter(x, y, s=cases, c='r', alpha=0.5)

axins = zoomed_inset_axes(ax, 7, loc=1)
axins.set_xlim(-20, 0)
axins.set_ylim(3, 18)

plt.xticks(visible=False)
plt.yticks(visible=False)

map2 = Basemap(llcrnrlon=-20,llcrnrlat=3,urcrnrlon=0,urcrnrlat=18, ax=axins)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

map2.scatter(x, y, s=cases/5., c='r', alpha=0.5)

mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

#plt.draw()
plt.show()
