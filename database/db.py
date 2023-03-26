# UTF-8 encoding
import sqlite3
import pickle
from random import choices
from os import getcwd
from string import ascii_letters 

class DB:
    
    history = dict # url : timestamp
    password = dict # url : password
    
    def saveInFile(self, obj):
        cwd = getcwd()
        if('../' not in cwd):
            filename = ''.join(choices(ascii_letters, k=10))+".mouni"
            try:
                fd = open(filename, 'wb')
                pickle_obj = pickle.dump(obj, fd, protocol=None)
                fd.close()
            except:
                return -1
    
    def extract_from_file(self, fd):
        try:
            _pickle = pickle.load(fd)
            return _pickle
        except:
            print('something went wrong!!')

    def retrive_passwds(self):
        pass

    def store_passwds(self, storage_file):
        pass
    
    def store_history(self, storage_file):
        try:
            connection = sqlite3.connect(storage_file)
            cur = connection.cursor()
            cur.execute('SELECT origin,last_access_time,accessed FROM origin')
            result = cur.fetchall()
            for tup in result:
                self.history.update({tup[0]:tup[1:]})
            self.saveInFile(self.history)
        except:
            pass
        pass
    
    def retrive_history(self, fd):
        print(self.extract_from_file(fd))

    def store_cookies(self):
        pass

    def retrive_cookies(self):
        pass
    
