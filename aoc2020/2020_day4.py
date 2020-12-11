# AOC 2020 Day 4
# Chris O
#
# Goal is to find the amount of valid passports
# We need the following info

#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)      This one is optional


import re

filename = '2020_d4.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n\n')

validcount = 0
totalentries = len(datas)

p1 = re.compile('byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:')
p2 = re.compile('byr:19[2-9]\d|byr:200[0-2]|'
                'iyr:201\d|iyr:2020|eyr:202\d|eyr:2030|'
                'hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in|'
                'hcl:#[0-9a-f]{6}|ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth|'
                    r'pid:[0-9]{9}\b')
p = p2

usinput = input('Enter "1" or "2" for respective part: ')

if usinput == '1':
    p = p1
    print('For part 1')
else:
    print('For part 2')
    
for e in datas:
    collect = p.findall(e)
    if len(collect) == 7:
        validcount +=1

print('The valid amount of entries in the report is: ',validcount)