def calculate_population_density(population, area):
    """
    This function takes the population and area of a city and calculates its population density.
    """
    density = population / area
    return density

import geopandas as gpd
from shapely.geometry import Polygon

def create_land_use_polygons(dataframe):
    polygons = []
    
    # Iterate over each row in the DataFrame
    for index, row in dataframe.iterrows():
        land_use = row['land_use']
        count = row['count']
        
        # Create a square polygon centered at (0, 0) with a side length based on the count value
        side_length = count * 100  # Adjust the multiplier based on your data and desired polygon size
        half_side = side_length / 2
        polygon = Polygon([(-half_side, -half_side), (-half_side, half_side), (half_side, half_side), (half_side, -half_side)])
        
        # Add the land use and polygon to the list as a tuple
        polygons.append((land_use, polygon))
    
    return polygons