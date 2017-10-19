
def create_speciestable(vegdb_dataframe):
    groupby_spname = vegdb_dataframe.groupby("speciesKey")
    sp_table=""
    for speciesKey, group in groupby_spname:
        sp_table += "%i;%s;%s;%s;%s;%s;%s;%s;%s \n" % (group["speciesKey"].unique()[0],group["kingdom"].unique()[0],group["phylum"].unique()[0],group["class"].unique()[0],group["order"].unique()[0],group["family"].unique()[0],
                                group["genus"].unique()[0],group["species"].unique()[0],group["vernacularName"].unique()[0])
    return sp_table

def create_plottable(vegdb_dataframe):
    groupby_plotid = vegdb_dataframe.groupby("eventID")
    plot_table=""
    for eventID, group in groupby_plotid:
        plot_table+= "%s;%f;%f;%s;%s;%s;%f;%s \n" % (group["eventID"].unique()[0],group["decimalLatitude"].unique()[0],group["decimalLongitude"].unique()[0],group["footprintWKT"].unique()[0],
                                                        group["habitat"].unique()[0],group["samplingProtocol"].unique()[0],group["sampleSizeValue"].unique()[0],
                                                        group["sampleSizeUnit"].unique()[0])
    return plot_table

def create_observtable(vegdb_dataframe,nameofoutput):
    obs_table = vegdb_dataframe[["occurrenceID", "eventID","speciesKey","year","eventDate","organismQuantity","organismQuantityType"]]
    obs_table.to_csv(nameofoutput+'.csv',sep=";",index=False)

def export_table(table,header,nameofoutput):
    fileout = open(nameofoutput+'.csv', "a")
    fileout.write(header)
    fileout.write(table)
    fileout.close()