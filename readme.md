# Scalable Walkability Analysis of Accra
Repository of a data science project at Ghana Telecom University Accra.

## Why ?
'Walkability Index' of a suburb measures how 'walkable' a given neighborhood is, in terms of road connectivity, population density, and land use mix.

It analyses and quantifies how pedestrian-friendly or walkable a neighborhood or suburb is. A higher walkability index indicates that the area is more conducive to walking and has better amenities, services, and infrastructure for pedestrians.

### Data Acquisition 
Obtain the necessary data from OpenStreetMap (OSM) for the suburb you want to analyze. You can download the data in OSM XML format or use an OSM data API. There are Python libraries available, such as osmnx, that simplifies this process by providing a convenient interface to access OSM data.

### Data Preparation
Once you have the OSM data, you need to preprocess it to extract the relevant features for calculating the Walkability Index. Some of the key features to consider are road connectivity, population density, and land use mix. You may need to filter the OSM data to include only the road network within the suburb boundary, and gather additional data like population density and land use information from other sources if not available in the OSM data directly.

### Calculating Walkability Components
Assign weights to each component (road connectivity, population density, and land use mix) based on their importance and relevance to walkability. For example, you may consider road length and intersections for road connectivity, population count per unit area for population density, and a mix of land use types (residential, commercial, parks, etc.) for land use mix. Normalize each component to a common scale, such as between 0 and 1, to ensure equal weightage during aggregation.

### Aggregation and Weighted Sum
Divide the suburb into smaller chunks, such as grid cells, and calculate the Walkability Index for each chunk based on the weighted sum of the normalized components. The aggregation can be done using spatial operations like overlaying the grid cells on the road network and land use polygons. Finally, you can assign the Walkability Index to the suburb as the average or weighted average of all the grid cells within its boundaries.

### Visualization
Visualize the Walkability Index using maps or other graphical representations to understand the spatial distribution of walkability within the suburb. You can use libraries like geopandas, folium, or matplotlib to create visualizations and overlays.

## Notebooks and Analysis
[Data Manipulation and Viz](./visualized.ipynb)

[Link to Jupyter File](./visualized.ipynb)


## Tech
The following technologies were used for this part of the project:

- Python 2
- iPython Notebooks: For interactive code development and result presentation.
- Pandas: Python package for data analysis.
- Matplotlib and Seaborn: Python 2D plotting library.
- Leaflet Maps + Folium: Python package for building choropleth-maps.
