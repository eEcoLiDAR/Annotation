"""
Aim: Converting Dutch Vegetation Database (LVD) data into annotation data for EcoLiDAR project
@Author: Zsófia Koma (UvA)

Example usage from command line (Anaconda prompt):
python Process_DwC_main.py [filepath]\occurrence.txt [filepath]\output
"""

import argparse
import pandas as pd

import ConvertDwC_into_Polygon as cp
import Create_Tables as ct

parser = argparse.ArgumentParser()
parser.add_argument('occurrence', help='Name of the occurrence data (txt)')
parser.add_argument('shapefile', help='Name of the output shapefile (shp)')
args = parser.parse_args()

#Read the DwC data

vegdb=pd.read_csv(args.occurrence,sep='\t')

#Exclude fungi and algea and where the coordinateUncertaintyInMeters is lower than 1 km -- specific application for the BSc course
vegdb= vegdb[pd.isnull(vegdb.habitat)==False]
vegdb = vegdb[(vegdb["kingdom"]== "Plantae")]
#vegdb = vegdb[(vegdb["sampleSizeValue"]<1000)] # sampleSizeValue they do not correctly identified the squaremeter - squarekm
vegdb = vegdb[(vegdb["coordinateUncertaintyInMeters"]<1000)]

#Add area
area=cp.polyarea(vegdb)
vegdb = vegdb[(area<1000)]

# Create plotID
vegdb=ct.create_plotID(vegdb)

#Create tables --> Species Table, Plot Table, Observation Table

sp_table=ct.create_speciestable(vegdb)
plot_table=ct.create_plottable(vegdb)

ct.create_observtable(vegdb,args.shapefile+"ObservationTable")

#Export tables --> Species Table, Observation Table, Plot Table and shapefile related the plot measurements

speciesheader="speciesKey;species;kingdom;phylum;class;order;family;genus;specificEpithet;vernacularName \n"
plotheader="plotID;decimalLatitude;decimalLongitude;coordinateUncertaintyInMeters;footprintWKT;habitat;samplingProtocol;sampleSizeValue;sampleSizeUnit \n"

ct.export_table(sp_table,speciesheader,args.shapefile+"SpeciesTable")
ct.export_table(plot_table,plotheader,args.shapefile+"PlotTable")
footprint_wegdb=cp.polygonize_dwc(vegdb,args.shapefile)



