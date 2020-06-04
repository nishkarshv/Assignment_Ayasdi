import urllib
import random
import datetime
from datetime import date,timedelta
from random import randrange
import urllib.request
from doctest import testmod

class RandomGeneration:
    '''
        This class is to generate all random data like numbers, English_words and Dates
        
        >>> randomlist=[1,2,3,4,5]
        >>> RandomGeneration.gen_mean(RandomGeneration, randomlist)
        3.0
        >>> print(isinstance(RandomGeneration.gen_random_numbers(RandomGeneration,1, 10),float))
        True
        >>> print(isinstance(RandomGeneration.gen_random_dates(RandomGeneration,'June 10, 2018', 'July 15, 2019'),str))
        True
        >>> print("debit" in RandomGeneration.read_english_words(RandomGeneration))
        True
        '''
    
    def read_english_words(self):
        '''
        Get English words form the free bsd url
        '''
        word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = urllib.request.urlopen(word_url)
        long_txt = response.read().decode()
        words = long_txt.splitlines()
        return words
    
    def read_english_words_txt(self):
        '''
        Get English words form the free bsd url
        '''
        englist = []
        with open("english_words.txt", "r") as eng:
            for line in eng:
                englist.append(line.strip('\n'))
        return englist
            
      
    def gen_random_words(self, wordslist):
        '''
        get random words
        '''
        random_word = wordslist[random.randint(0,200)]
        return random_word
    
    def gen_random_words_list(self, n, wordslist):
        '''
        generate list of random words
        '''
        randomlist = []
        for i in range(n):
            randomlist.append(self.gen_random_words(wordslist))
        return randomlist
    
    def gen_random_numbers_list(self, n, start, end, nullpercent):
        '''
        generate list of random numbers
        '''
        randomlist = []
        nullnumberlist = []
        null_n = (n*nullpercent)//100
        for i in range(null_n):
            nullnumberlist.append(None)
        random_n = (n*(100-nullpercent))//100
        
        for i in range(random_n):
            randomlist.append(self.gen_random_numbers(start, end))
        
        mean = self.mean(randomlist)
        randomlistcombined = randomlist + nullnumberlist
        
        random.shuffle(randomlistcombined)
        
        return randomlistcombined, mean
     
    def gen_random_dates_list(self, n, start, end):
        '''
        generate list of random dates
        '''
        randomlist = []
        for i in range(n):
            randomlist.append(self.gen_random_dates(start ,end))
        return randomlist
        
    def gen_random_numbers(self, start, end):
        '''
        To get the random numbers between two end points
        
        '''
        return random.gauss(start, end)
    
    def gen_random_dates(self,start ,end):
        '''
        To get the random dates between two dates
        
        
        '''
        stdate = datetime.datetime.strptime(start, '%B %d, %Y').strftime('%m-%d-%Y')
        startdate = datetime.datetime.strptime(stdate, '%m-%d-%Y')
        edate = datetime.datetime.strptime(end, '%B %d, %Y').strftime('%m-%d-%Y')
        enddate = datetime.datetime.strptime(edate, '%m-%d-%Y')
        delta =  enddate - startdate
        intdelta = randrange(delta.days)
        rand_date = (startdate + timedelta(intdelta)).date()
        randomdate = rand_date.strftime('%B %d, %Y')
        return randomdate
    
    def mean(self, numbers):
        '''
        Mean from list of numbers
        '''
        return sum(numbers) / len(numbers)
    
    def gen_mean(self, randomlist):
        '''
        generate mean by removing None from list
        '''
        return self.mean(list(filter(None.__ne__, randomlist)))
    
if __name__ == '__main__':
    testmod(verbose=True)
    
