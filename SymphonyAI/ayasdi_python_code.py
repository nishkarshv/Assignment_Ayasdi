
import db_operations as sql
from mapping_random_data import Mapping_Random
from create_csv import Create_Csv

class Ayasdi:
    def main(self):
        n = 1000
        csvfilename = 'ayasdi_assignment.csv'
        start_date = 'January 1, 2014'
        end_date = 'December 31, 2014' 
        map_random = Mapping_Random()
        ccsv = Create_Csv()
        csvmapping_dict = map_random.create_mapping_csv(n, start_date, end_date)
        ccsv.create_csv(csvmapping_dict, csvfilename)
        sql.csvToDatabase('ayasdi_assignment.csv','ayasdi.db','ayasdi_random', outputToFile = False)
if __name__ == "__main__":
    ay = Ayasdi()
    ay.main()
    
    