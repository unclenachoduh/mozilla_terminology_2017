import re
readfile = open("RESOURCES/msTerms.txt", encoding="utf8")
ms = readfile.read()
readfile.close()
msterms = ms.split('\n')

readfile = open("mTerm/mozTerms.txt", encoding="utf8")
mz = readfile.read()
readfile.close()

mzterms = mz.split('\n')

writeme = []
dntwriteme = []
dupewriteme = []
for line in mzterms:
    if line not in msterms:
        if line not in writeme:
            writeme.append(line)
        else:
            dupewriteme.append(line)
    else:
        dntwriteme.append(line)

writeme = sorted(writeme)
dupewriteme = sorted(dupewriteme)
dntwriteme = sorted(dntwriteme)


scribe = ""

for line in writeme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("mTerm/MozDiff.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()

scribe = ""

for line in dntwriteme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("mTerm/MozSame.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()

scribe = ""

for line in dupewriteme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("mTerm/MozDUPES.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()
