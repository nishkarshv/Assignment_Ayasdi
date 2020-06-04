from random_generation import RandomGeneration
import multiprocessing as mp
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
    
    def create_mapping_random_numbers(self, startindex, endindex, n, start, end, nullpercent):
        '''
        Mapping to create column dictionary based on random numbers like {col2_mean(col):[1,2,3]}
        '''
        randomnumbers_dict = {}
        for col in range(startindex,endindex):
            # getting list with None value
            randomnumberlist = self.randomgen.gen_random_numbers_list(n, start, end, nullpercent)[0]
            # getting mean
            mean_x = self.randomgen.gen_random_numbers_list(n, start, end, nullpercent)[1]
            
            colkey = 'col{}_{}'.format(col, mean_x)
            if colkey not in randomnumbers_dict:
                randomnumbers_dict[colkey] = randomnumberlist
        
        return randomnumbers_dict
    
    def create_mapping_random_words(self, startindex, endindex, n, wordslist):
        '''
        Mapping to create column dictionary based on random words like {col11:["hello","debit","deactivate"]}
        '''
        randomwords_dict = {}
        for col in range(startindex, endindex):
            colkey = 'col{}'.format(col)
            if colkey not in randomwords_dict:
                randomwords_dict[colkey] = self.randomgen.gen_random_words_list(n, wordslist)
        return randomwords_dict
    
    def create_mapping_random_dates(self, index, n, start, end):
        '''
        Function to create dictionary for col20 with random dates
        '''
        randomdates_dict = {}
        colkey = 'col{}'.format(index)
        if colkey not in randomdates_dict:
            randomdates_dict[colkey] = self.randomgen.gen_random_dates_list(n, start, end)
        return randomdates_dict
    
    def create_mapping_csv(self, n, start_date, end_date):
        '''
        This function creates mapping dictionary for csv
        '''
        gaussian_mean = 10
        gaussian_variance = 2
        mappingdict = dict()
        nullpercent = 10
        wordslist = self.randomgen.read_english_words_txt()
        
        pool = mp.Pool(mp.cpu_count())
        res1 = pool.apply(self.create_mapping_index, args=[1,n])
        res2 = pool.apply(self.create_mapping_random_numbers, args=[2, 11,n, gaussian_mean, gaussian_variance, nullpercent])
        res3 = pool.apply(self.create_mapping_random_dates, args =[20, n, start_date, end_date])
        res4 = pool.apply(self.create_mapping_random_words, args =[11,20,n, wordslist])
        mappingdict.update(res1)
        mappingdict.update(res2)
        mappingdict.update(res3)
        mappingdict.update(res4)
        pool.close()
        pool.join()
        return mappingdict
