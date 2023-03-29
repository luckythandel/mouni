import subprocess
import os
from configparser import ConfigParser
from checksumdir import dirhash
#from firepwd.firepwd import decryptItAll
import sqlite3

class Dump:

    profiles = {}
    history = {}
    passwords = {}
    cookies = {}

    def __init__(self, *profiles):
        if(profiles):
            self.profiles = profiles

    def checksumPath(self, path: str):
        return dirhash(path)      
    
    def getProfiles(self):
        for name, path in self.profiles.items():
            print(name, end='')
            print("path: %s, checksum: %s"% (path[0], path[1]))

    def retriveProfiles(self):
        print("console")
        if (os.name == "posix"):
            user = os.getenv("USER")
            if user == 'root':  
                profile_path = '/root/.mozilla/firefox/'
            else:
                profile_path = '/home/'+user+'/.mozilla/firefox/'
            try:
                configur = ConfigParser()
                fd_ini = configur.read(profile_path+'profiles.ini')
                for each_section in configur.sections():
                    try:
                        name, path = configur.get(each_section, 'Name'), configur.get(each_section, 'Path')
                        self.profiles.update({name:[profile_path+path, self.checksumPath(profile_path+path)]})
                    except:
                        pass
            except Exception as e:
                print("profiles.ini dosen't exist", e)
        # under construction....
        elif (os.name == "nt"):
            print("under construction....")
        return 0;

    def retriveHistory(self, storage_file): # not working...
        if(os.name == "posix"):
            try:
                connection = sqlite3.connect(storage_file)
                cur = connection.cursor()
                cur.execute('SELECT origin,last_access_time,accessed FROM origin')
                result = cur.fetchall()
                for tup in result:
                    self.history.update({tup[0]:tup[1:]})
            except Exception as e:
                print("no data found!", e)
                pass
        # under construction
        elif(os.name == "nt"):
            pass

    def retrivePasswords(self, profile_path):
        json_output = decryptItAll(profile_path)
        self.passwords = json_output

    def retriveCookies(self, cookies_path):
        if(os.name == "posix"):
            try:
                connection = sqlite3.connect(cookies_path+'cookies.sqlite')
                cur = connection.cursor()
                cur.execute('SELECT name,value,host FROM moz_cookies')
                result = cur.fetchall()
                prev = result[0]
                key_value = []
                # prev[2] -> host, prev[1] -> value, prev[0] -> name 
                self.cookies.update({prev[2]:key_value})
                for tup in range(1, len(result)):
                    if(result[tup][2] == prev[2]):
                        key_value.append({result[tup][0]:result[tup][1]})
                        self.cookies.update({result[tup][2]:key_value})
                    else:
                        key_value = []
                        key_value.append({result[tup][0]:result[tup][1]})
                        self.cookies.update({result[tup][2]:key_value})
                        
            except Exception as e:
                print("no data found!", e)
                pass
        # under construction
        elif(os.name == "nt"):
            pass
        pass

if __name__ == "__main__":
    dump = Dump()
    dump.retriveCookies('/root/.mozilla/firefox/abm78pza.default-esr/')
    # print(dump.cookies)
    #print(dump.profiles)
    pass