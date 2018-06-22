import re
readfile = open("RESOURCES/1000words.txt", encoding="utf8")
common = readfile.read()
readfile.close()
common = common.lower()
commonlines = common.split('\n')
writeme = []

for line in commonlines:
    if line not in writeme:
        writeme.append(line)

writeme = sorted(writeme)
scribe = ""

for line in writeme:
    scribe = line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("quickie/1000wordsNEW.txt", 'w+', encoding="utf8")
for line in writeme:
    writefile.write(scribe)

writefile.close()