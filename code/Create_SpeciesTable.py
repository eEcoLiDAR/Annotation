
def create_speciestable(vegdb_dataframe):
    groupby_spname = vegdb_dataframe.groupby("scientificName")
    sp_table=""
    for sp_name, group in groupby_spname:
        sp_table += "(%s,%s),\n" % (sp_name,group["family"].unique()[0])
    return sp_table
