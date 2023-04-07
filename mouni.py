#/bin/env python3
from py_console import console
from browsers.firefox import acquisition
from database.db import DB 
import argparse
from checksumdir import dirhash
from os.path import isfile, isdir
import json

'''
@luckythandel - mouni
For now, it can only work for mozilla forensics but we will 
impliment it for other browsers too, soon.
still in development...
'''
HISTORY=0;PASSWORDS=0;COOKIES=0
FLAGS = (HISTORY, PASSWORDS, COOKIES)

def checksumPath(path: str) -> str:
    return dirhash(path)

def view_json(filename):
    try:
        json_obj = json.load(open(filename))
        print("sex")
        # retrive Passwords, History, Cookies in a beautiful synthx
        json_pretty = json.dumps(json_obj, indent=2)
        print(json_pretty)
    except Exception as e:
        print('JSON DB doesn\'t exist')
        pass
    pass

def dump_obj():
    dump = acquisition.Dump()
    return dump

def interactive():
    # when no agrument is supplied
    while(1):
        print("-----profiles------")
        dump = dump_obj()
        dump.retriveProfiles()
        profiles = dump.profiles
        for name, l in profiles.items():
            print("name: %s, path: %s"% (name, l[0]))
        print('-----browsers-----')
        print('1. Firefox\n2. Chrome\n3.Safari')
        browser = input('> ')
        if(int(browser) == 1):
            profile = input('profile: ')
            if(isdir(profile)):
                if(not profile.endswith('/')):
                    profile+='/'
                checksum = checksumPath(profile)
                fullpath = "database/obj_fd/"+checksum+'_ape.json'
                if(isfile(fullpath)):
                   console.warn('the profile has been analyzed already!')
                   view_json(fullpath)
                else:
                    console.success('Starting analyzing...')
                    print('----acquisition----')
                    dump.retriveCookies(profile)
                    dump.retriveHistory(profile)
                    dump.retrivePasswords(profile)
                    console.log("Saving to database..")
                    view_ans = input('Do you want to see the mouni DB(Y/N)')
                    if(view_ans.lower() == 'y'):
                        console.success('JSON database...')
                        # creating database under database/obj_df/
                        _db = DB(checksum, dump.cookies, dump.passwords, dump.history)
                        fullpath = "database/obj_fd/"+checksum+'_ape.json'
                        view_json(fullpath)
            else:
                print("no such profile")
                
        elif(int(browser) == 2):
            pass
        elif(int(browser) == 3):
            pass
    pass

def main():
    # view or acquisition

    pass

interactive()
