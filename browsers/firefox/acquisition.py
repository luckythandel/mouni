import subprocess
import os
from configparser import ConfigParser
from checksumdir import dirhash

class Dump:

    profiles = {}
    history = {}
    checksums = {}

    def __init__(self, *profiles):
        if(profiles):
            self.profiles = profiles

    def checksumPath(self, path: str):
        return dirhash(path)      
    
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
                for each_section in fd_init.sections():
                    name, path = configur.get(each_section, 'Name'), configur.get(each_section, 'Path')
                    print(name, path)
                    self.profiles.update({name:profile_path+path})
                    checksumPath.update({each_section: checksumPath(profile_path+path)})
            except:
                yield "profiles.ini dosen't exist"
        # under construction....
        elif (os.name == "nt"):
            pass
    

    def getProfiles(self):
        # error
        for name, path in self.profiles.items():
            print(name, path)

    def setProfile(self, profiles : list):
        self.profiles = profiles

    def retriveHistory(self, storage_file):
        if(os.name == "posix"):
            try:
                connection = sqlite3.connect(storage_file)
                cur = connection.cursor()
                cur.execute('SELECT origin,last_access_time,accessed FROM origin')
                result = cur.fetchall()
                for tup in result:
                    self.history.update({tup[0]:tup[1:]})
            except:
                yield "no data found!"
            
        # under construction
        elif(os.name == "nt"):
            pass


