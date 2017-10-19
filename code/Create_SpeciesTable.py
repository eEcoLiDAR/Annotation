
def create_speciestable(vegdb_dataframe):
    selcols_fromvegdb=vegdb_dataframe[["taxonID","scientificNameID","acceptedNameUsageID","scientificName","higherClassification",
                                       "kingdom","phylum","class","order","family","genus","vernacularName"]]
    groupby_spname = selcols_fromvegdb.groupby('scientificName')
    for sp_name, group in groupby_spname:
        print(sp_name,)