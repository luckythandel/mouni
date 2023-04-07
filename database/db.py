# UTF-8 encoding
import json

class LOG:
    def __init__(self, checksum:str, len_passwords: int, len_cookies: int, len_history: int):
        fd = open('logs.mouni', 'w+')
        temp = 'profile checksum: %s\n'%(checksum)
        temp+="  total passwords: %s\n"%(len_passwords)
        temp+="  total cookies: %s\n"%(len_cookies)
        temp+="  total history links: %s\n"%(len_history)
        fd.write(temp)

class DB:

    passwords = {}
    history = {}
    cookies = {}
    checksum = ""

    def __init__(self, checksum: str, cookies: dict, passwords: dict, history: dict) -> None:
        self.cookies = cookies
        self.history = history
        self.passwords = passwords
        self.checksum = checksum
        self.createDB(checksum)
        log =   LOG(checksum,
                len(passwords),
                len(cookies),
                len(history))

    def createDB(self, checksum: str):
        all_dump = {
                    "passwords": self.passwords,
                    "history": self.history,
                    "cookies": self.cookies
                    }
        try:
            # print(all_dump)
            all_json_dump = json.dumps(all_dump, indent=2)
            filename = 'database/obj_fd/'+checksum+'_ape.json'
            fd = open(filename, 'w')
            fd.write(all_json_dump)
            fd.close()
        except Exception as e:
            print("R/W error with database:", e)

