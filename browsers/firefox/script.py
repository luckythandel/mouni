from acquisition import Dump
db = Dump()
print(db.retriveProfiles())
print(db.checksumPath('/root/Documents/mouni/'))
print(db.profiles)