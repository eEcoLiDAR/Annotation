from shapely.geometry import mapping
from shapely.wkt import loads
from fiona import collection

def polygonize_dwc(vegdb_dataframe,shapefile):

    groupbypoly = vegdb_dataframe.groupby('footprintWKT')
    schema = {'geometry': 'Polygon',
              'properties': {'nof_sp': 'str'}, }

    with collection(shapefile, "w", "ESRI Shapefile", schema) as output:
        for footprintWKT, group in groupbypoly:
            geometry = loads(footprintWKT)
            output.write({'geometry': mapping(geometry),'properties': {'nof_sp': str(group['species'].shape)}, })