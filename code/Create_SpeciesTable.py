
def create_speciestable(vegdb_dataframe):
    groupby_spname = vegdb_dataframe.groupby("scientificName")
    sp_table=""
    for sp_name, group in groupby_spname:
        if group["speciesKey"].unique()[0]>0:
            sp_table += "%i;%s;%s;%s;%s;%s;%s;%s;%s \n" % (group["speciesKey"].unique()[0],group["kingdom"].unique()[0],group["phylum"].unique()[0],group["class"].unique()[0],group["order"].unique()[0],group["family"].unique()[0],
                                  group["genus"].unique()[0],group["species"].unique()[0],group["genericName"].unique()[0])
    return sp_table

def export_table(sp_table,nameofoutput):
    fileout = open(nameofoutput+'.csv', "w")
    fileout.write(sp_table)
    fileout.close()