
def create_speciestable(vegdb_dataframe):
    groupby_spname = vegdb_dataframe.groupby("speciesKey")
    sp_table=""
    for speciesKey, group in groupby_spname:
        sp_table += "%i;%s;%s;%s;%s;%s;%s;%s;%s \n" % (group["speciesKey"].unique()[0],group["kingdom"].unique()[0],group["phylum"].unique()[0],group["class"].unique()[0],group["order"].unique()[0],group["family"].unique()[0],
                                group["genus"].unique()[0],group["species"].unique()[0],group["vernacularName"].unique()[0])
    return sp_table

def export_table(sp_table,header,nameofoutput):
    fileout = open(nameofoutput+'.csv', "a")
    fileout.write(header)
    fileout.write(sp_table)
    fileout.close()