import csv
from itertools import zip_longest
class Create_Csv:
    def create_csv(self, mapdict, filename):
        colnames = mapdict.keys()
        coldata = mapdict.values()
    
        export_data = zip_longest(*coldata, fillvalue='')
        tup = tuple(colnames)
    
        with open(filename, 'w',  newline='') as onefile:
            wr = csv.writer(onefile, dialect="excel", delimiter = '\t')
            wr.writerow(tup)
            wr.writerows(export_data)
        onefile.close()