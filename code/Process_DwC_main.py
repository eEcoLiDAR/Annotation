# -*- coding: utf-8 -*-
"""
Aim: Converting Dutch Vegetation Database (LVD) data into annotation data for EcoLiDAR project
@Author: Zsófia Koma (UvA)

Example usage from command line (Anaconda prompt):
python Process_DwC_main.py [filepath]\occurrence.txt
"""

import argparse
import pandas as pd

import ConvertDwC_into_Polygon as cp

parser = argparse.ArgumentParser()
parser.add_argument('occurrence', help='Name of the occurrence data (txt)')
parser.add_argument('shapefile', help='Name of the output shapefile (shp)')
args = parser.parse_args()

vegdb=pd.read_csv(args.occurrence,sep='\t')

footprint_wegdb=cp.polygonize_dwc(vegdb,args.shapefile)



