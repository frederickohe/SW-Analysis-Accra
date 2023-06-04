import osmnx as ox

location = "Suburb Name, City Name, Australia"

graph = ox.graph_from_place(location, network_type="walk")

buildings = ox.footprints.footprints_from_place(location)
