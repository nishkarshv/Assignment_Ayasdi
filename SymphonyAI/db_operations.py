import csv, sqlite3
from sqlite3 import OperationalError 

def _get_col_datatypes(csvfile):
    '''
    To create the column datatypes
    '''
    dr = csv.DictReader(csvfile, delimiter= "\t") 
    
    fieldTypes = {}
    for entry in dr:
        feildslLeft = [f for f in dr.fieldnames if f not in fieldTypes.keys()]        
        if not feildslLeft: break 
        for field in feildslLeft:
            data = entry[field]

            if len(data) == 0:
                continue
            
            fieldTypes[field] = "TEXT"
        

    if len(feildslLeft) > 0:
        raise Exception("Failed to find all the columns data types, please check again.")

    return fieldTypes

def create_connection(dbname):
    '''
    function to create connections
    '''
    try:
        
        connection =  sqlite3.connect(dbname)
        return connection
    except (ValueError, sqlite3.OperationalError):
        import warnings
        warnings.warn("Make sure the database file %s is installed and uncompressed." % dbname)
        raise 
    
def execute_query(dbname, query):
    '''
    function to execute queries
    '''
    try:
        
        connection =  create_connection(dbname)
        cur = connection.cursor()
        return cur.execute(query)
    except (ValueError, sqlite3.OperationalError):
        import warnings
        warnings.warn("Make sure the database file %s is installed and uncompressed." % dbname)
        raise 

def create_table_statement(dbname, tablename, columnlist):
    '''
    Generate create table statement:
    '''
    stmt = "create table if not exists \"" + tablename + "\" (%s)" % ",".join(columnlist)
    return stmt
        
def insert_to_table_statement(tablename, sqldict):
    '''
    insert statement creation
    '''
    columns_string= '('+','.join(sqldict.keys())+')'  
            
    values_string = '('+','.join(map(str,sqldict.values()))+')'   
    
    sql = """INSERT INTO %s %s
        VALUES %s"""%(tablename, columns_string,values_string)
        
    return sql

def csvToDatabase(csvFile,dbname,tablename, outputToFile = False):
    '''
    csv to database function
    '''
  
    with open(csvFile,mode='r', encoding="ISO-8859-1") as readcsv:
        dt = _get_col_datatypes(readcsv)

        readcsv.seek(0)

        reader = csv.DictReader(readcsv, delimiter= "\t")
        
        # Keep the order of the columns name just as in the CSV
        fields = reader.fieldnames
        columnlist = []

        # Set field and type
        for f in fields:
            columnlist.append("\"%s\" %s" % (f, dt[f]))
        
        # create table
        create_table = create_table_statement(dbname, tablename, columnlist)
        execute_query(dbname, create_table)
        
        
        for row in reader:
            # insert to table
            sql = insert_to_table_statement(tablename, row)
            try:
                execute_query(dbname, sql)
            except sqlite3.OperationalError:
                pass
    readcsv.close()
    
    
def get_data_from_table(dbname, tablename):
    '''
    Select query from table
    '''
    conn =  sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * FROM ayasdi.ayasdi31""")
    except OperationalError:
        return(False)        
        


#get_data_from_table('ayasdi.db', 'ayasdi31')