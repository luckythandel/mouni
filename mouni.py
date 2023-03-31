#/bin/env python3
from py_console import console
from browsers.firefox import acquisition
from database import db
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
        json_obj = json.load(filename)
        # retrive Passwords, History, Cookies in a beautiful synthx
        
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
                checksum = checksumPath(profile)
                fullpath = "database/obj_fd/"+checksum+'.json'
                if(isfile(fullpath)):
                   console.warn('the profile has been analyzed already!')
                   view_json(fullpath)
                else:
                    console.success('Starting analyzing...')
                    while(1):
                        print('----acquisition----')
                        print('1. History\n2.Passwords\n3.Cookies\n4.Exit')
                        acq = int(input('>'))
                        if(acq == 1):
                            dump.retriveHistory(profile)
                            HISTORY=1
                            print('added to DB...')
                        elif(acq == 2):
                            dump.retrivePasswords(profile)
                            PASSWORDS=1
                            print('added to DB...')
                        elif(acq == 3):
                            dump.retriveCookies(profile)
                            COOKIES=1
                            print('added to DB...')
                        else:
                            break
                    view_ans = input('Do you want to see the mouni DB(Y/N)')
                    while(1):
                        if(view_ans.lower() == 'Y'):
                            pass
                        elif(view_ans.lower() == 'N'):
                            print('Going back...')
                            break

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
