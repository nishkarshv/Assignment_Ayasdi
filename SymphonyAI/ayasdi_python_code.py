
import db_operations as sql
from mapping_random_data import Mapping_Random
from create_csv import Create_Csv
import multiprocessing as mp
import time
class Ayasdi:
    def main(self):
        n = 1000000
        csvfilename = 'ayasdi_assignment.csv'
        dbname = "ayasdi.db"
        tablename = "ayasdi"
        start_date = 'January 1, 2014'
        end_date = 'December 31, 2014' 
        map_random = Mapping_Random()
        ccsv = Create_Csv()
        start_time = time.time()
        csvmapping_dict = map_random.create_mapping_csv(n, start_date, end_date)
        print("--- mapping time is   --------------  %s seconds ---" % (time.time() - start_time))
        pool = mp.Pool(mp.cpu_count())
        csv_start_time = time.time()
        pool.apply(ccsv.create_csv, args=[csvmapping_dict, csvfilename])
        print("--- csv writing time is   --------------  %s seconds ---" % (time.time() - csv_start_time))
        db_start_time = time.time()
        pool.apply(sql.create_db_from_dataset, args=[dbname, tablename, csvmapping_dict])
        print("--- db writing time is   --------------  %s seconds ---" % (time.time() - db_start_time))
        
        ################uncomment the below call to see data of table########################
        #sql.get_data_from_table('ayasdi.db', 'ayasdi')
if __name__ == "__main__":
    ay = Ayasdi()
    ay.main()
    
    
