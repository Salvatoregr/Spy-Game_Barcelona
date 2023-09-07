from gps_class import GPSVis

vis = GPSVis(
    data_path=5,                                    # <--- data file with GSM positions (change only this row)
    locations="data-locations.csv",                 # restaurants and residences
    map_path="data-map.png",                        # Map downloaded from OSM (https://www.openstreetmap.org/export)
    points=(41.4733, 1.9720, 41.3281, 2.3209)     # Two coordinates of the map (upper left, lower right)
)

vis.create_image(color=(0, 0, 255), width=5)  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')

# print()
