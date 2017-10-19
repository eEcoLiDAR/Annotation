"""
Aim: Converting Dutch Vegetation Database (LVD) data into annotation data for EcoLiDAR project
@Author: Zsófia Koma (UvA)

Example usage from command line (Anaconda prompt):
python Process_DwC_main.py [filepath]\occurrence.txt
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

#Create tables --> Species Table, Observation Table, Plot Table and shapefile related the plot measurements

speciesheader="speciesKey;kingdom;phylum;class;order;family;genus;species;vernacularName \n"

sp_table=ct.create_speciestable(vegdb)
ct.export_table(sp_table,speciesheader,args.shapefile+"SpeciesTable")

footprint_wegdb=cp.polygonize_dwc(vegdb,args.shapefile)



