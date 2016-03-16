import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cartopy

# load ceden data into dataframe
ceden = pd.read_table('data/ceden_sample.txt', low_memory=False)

# take out a few important columns just for demonstration
ceden_lim = ceden[
    ['StationName', 'StationCode', 'SampleDate', 'CollectionTime',
     'LocationCode', 'CollectionDepth', 'Analyte', 'Unit', 'county',
     'TargetLatitude', 'TargetLongitude', 'Result']]

# in this cell we exract the unique xy coordinates found in the dataset
latlon = ceden[['TargetLongitude', 'TargetLatitude']]
# take unique, non-na coords
latlon.dropna(inplace=True)
xyunique = np.unique(
    zip(latlon.TargetLongitude, latlon.TargetLatitude)
)

assert len(xyunique) == 165

ccrs = cartopy.crs
# now we make our map
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())


# get a nice view of Cali and surrounding area
ax.set_extent([-125, -113, 31, 43])

# add features
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS)

state_borders = cartopy.feature.NaturalEarthFeature(
    category='cultural', name='admin_1_states_provinces_lines',
    scale='50m', facecolor='none')

ax.add_feature(state_borders, linestyle=':')

for xy in xyunique:
    ax.plot(xy[0], xy[1], 'ro', markersize=7, transform=ccrs.PlateCarree())

ax.plot(-121.4689, 38.5556, 'bo', markersize=10, transform=ccrs.PlateCarree())
ax.text(-121.3, 38.5,  'Sacramento, CA', transform=ccrs.PlateCarree())
