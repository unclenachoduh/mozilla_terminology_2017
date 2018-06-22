####################################################
# This script reads the lines of a Term base Exchange (.tbx) and  saves the terms to a separate file (outTerms.txt)
# You must put the tbx file in the same folder as the .py file compTBX and when prompted for the file name, you
# do not need to add ".tbx"
# The .tbx should be in the following format:
# <termEntry id="#_#"><langSet xml:lang="en-US"><descripGrp><descrip type="definition">text</descrip></descripGrp><ntig><termGrp><term id="#">term</term><termNote type="partOfSpeech">POS</termNote></termGrp></ntig></langSet><langSet xml:lang="es-mx"><ntig><termGrp><term id="#">term</term><termNote type="partOfSpeech">POS</termNote></termGrp></ntig></langSet></termEntry>
####################################################
import re
filename = input("Enter File name: ")
filename = "RESOURCES/" + filename + ".tbx"
readfile = open(filename, encoding="utf8")
common = readfile.read()
readfile.close()
common = common
commonlines = common.split('\n')

content = re.sub("<[^>]>", "\t", common)
content = re.sub("\t", "", content)

chunk = "<termEntry id=\"\d*_\d*\"><langSet xml:lang=\"en-US\"><descripGrp><descrip type=\"definition\">" \
        "[^<]*</descrip></descripGrp><ntig><termGrp><term id=\"\d*\">"

numlines = 0
numout = 0

writeme = []
dntwriteme = []

shortlen = 0

for line in commonlines:
    line = re.sub("xml:lang=\"es-mx\".*", "", line)
    if re.match("^<termEntry.*", line):
        temp = line
        line = re.sub(chunk, "", line)
        line = re.sub("<.*", "", line)

        # This loop prints strings that are left empty after stripping xml
        # if len(line) < 1:
        #     shortlen += 1
        #     print( temp) #str(shortlen) + "\t\t\t" +

        numlines += 1

        line = line.lower()
        line = re.sub(" &amp; ", " and ", line)
        line = re.sub("^&amp; ", "and", line)
        line = re.sub(" &amp;$", "and", line)
        line = re.sub("&amp; ", "and ", line)
        line = re.sub(" &amp;", " and", line)
        line = re.sub("&amp;", " and ", line)

        line = re.sub("[?.,/#!$%^*:;{}=\"—“”|_`~()\[\]…]", "", line)

        if line not in writeme:
            if re.match("^[^\w'\"].*$", line):
                dntwriteme.append(line + "\t\t\tSYMBOL")
            else:
                writeme.append(line)
                numout += 1
        else:
            dntwriteme.append(line + "\t\t\tDUPE")
    else:
        dntwriteme.append(line + "\t\t\tNo Match")

print("Number of Terms: " + str(numlines) + " | Number to file: " + str(numout))
payout = numlines-numout
print("Junk Items: " + str(payout))


writeme = sorted(writeme)
dntwriteme = sorted(dntwriteme)

scribe = ""

for line in writeme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("eTBX/outTerms.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()

scribe = ""

for line in dntwriteme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("eTBX/NotoutTerms.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()
