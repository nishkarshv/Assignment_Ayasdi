from random_generation import RandomGeneration
class Mapping_Random:
    randomgen = RandomGeneration()
    '''
    This class is to Create Mapping based on Random Data
    '''
    def create_mapping_index(self,index, n):
        '''
        Mapping to create index dictionary like {col1:[1,2,3]}
        '''
        return {'col{}'.format(index): [x+1 for x in range(n)]}
    
    def create_mapping_random_numbers(self, startindex, endindex, n, start, end):
        '''
        Mapping to create column dictionary based on random numbers like {col2_mean(col):[1,2,3]}
        '''
        randomnumbers_dict = {}
        for col in range(startindex,endindex):
            
            randomnumberlist = self.randomgen.gen_random_numbers_list(n, start, end)
            mean_x = self.randomgen.gen_mean(randomnumberlist)
            
            colkey = 'col{}_{}'.format(col, mean_x)
            if colkey not in randomnumbers_dict:
                randomnumbers_dict[colkey] = randomnumberlist
        
        return randomnumbers_dict
    
    def create_mapping_random_words(self, startindex, endindex, n, wordslist):
        '''
        Mapping to create column dictionary based on random words like {col11:["hello","debit","deactivate"]}
        '''
        randomnumbers_dict = {}
        for col in range(startindex, endindex):
            colkey = 'col{}'.format(col)
            if colkey not in randomnumbers_dict:
                randomnumbers_dict[colkey] = self.randomgen.gen_random_words_list(n, wordslist)
        return randomnumbers_dict
    
    def create_mapping_random_dates(self, index, n, start, end):
        '''
        Function to create dictionary for col20 with random dates
        '''
        randomnumbers_dict = {}
        colkey = 'col{}'.format(index)
        if colkey not in randomnumbers_dict:
            randomnumbers_dict[colkey] = self.randomgen.gen_random_dates_list(n, start, end)
        return randomnumbers_dict
    
    def create_mapping_csv(self, n, start_date, end_date):
        '''
        This function creates mapping dictionary for csv
        '''
        gaussian_mean = 10
        gaussian_variance = 2
        mappingdict = dict()
        
        wordslist = self.randomgen.read_english_words()
        mappingdict.update(self.create_mapping_index(1, n))
        mappingdict.update(self.create_mapping_random_numbers(2, 11,n, gaussian_mean, gaussian_variance))
        mappingdict.update(self.create_mapping_random_words(11,20,n, wordslist))
        mappingdict.update(self.create_mapping_random_dates(20, n, start_date, end_date))
        return mappingdict