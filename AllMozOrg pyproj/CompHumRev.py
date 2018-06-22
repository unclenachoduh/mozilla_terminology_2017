import re
readfile = open("RESOURCES/MSDiff.txt", encoding="utf8")
my = readfile.read()
readfile.close()
myterms = my.split('\n')

readfile = open("RESOURCES/HumRev.txt", encoding="utf8")
hr = readfile.read()
readfile.close()

hrterms = hr.split('\n')

writeme = []
dntwriteme = []
dupewriteme = []
for line in myterms:
    if line not in hrterms:
        if line not in writeme:
            writeme.append(line)
        else:
            if line not in dupewriteme:
                dupewriteme.append(line)
    else:
        if line not in dntwriteme:
            dntwriteme.append(line)

writeme = sorted(writeme)
dupewriteme = sorted(dupewriteme)
dntwriteme = sorted(dntwriteme)


scribe = ""

for line in writeme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("hRev/hRevDiff.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()

scribe = ""

for line in dntwriteme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("hRev/hRevSame.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()

scribe = ""

for line in dupewriteme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("hRev/hRevDUPES.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()
