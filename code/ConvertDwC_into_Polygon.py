from shapely.geometry import mapping
from shapely.wkt import loads
from fiona import collection

from geopandas import GeoDataFrame

def polyarea(vegdb_dataframe):
    geometry = vegdb_dataframe['footprintWKT'].map(loads)
    crs = {'init': 'epsg:18992'}
    geovegdb_dataframe = GeoDataFrame(vegdb_dataframe, crs=crs, geometry=geometry)
    return geovegdb_dataframe['geometry'].area


def polygonize_dwc(vegdb_dataframe,shapefile):

    groupbypoly = vegdb_dataframe.groupby('footprintWKT')
    schema = {'geometry': 'Polygon',
              'properties': {'plotID': 'str'}, }

    with collection(shapefile, "w", "ESRI Shapefile", schema) as output:
        for footprintWKT, group in groupbypoly:
            geometry = loads(footprintWKT)
            output.write({'geometry': mapping(geometry),'properties': {'plotID': str(group["plotID"].unique()[0])}, })