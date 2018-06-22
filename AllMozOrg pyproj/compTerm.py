# last Run 6/26/17 12:34 PM - 1849 words
# Additional suffix filters: 's al useBasicForm superlatives
import re
readfile = open("RESOURCES/msTerms.txt", encoding="utf8")
ms = readfile.read()
readfile.close()
msterms = ms.split('\n')

readfile = open("eTerm/mywords.csv", encoding="utf8")
mw = readfile.read()
readfile.close()

mw = re.sub(",\d*", "", mw)
mwterms = mw.split('\n')

writeme = []
dntwriteme = []
dupewriteme = []
for word in mwterms:
    wordsx = re.sub("s$", '', word)
    wordesx = re.sub("es$", '', word)
    wordntx = re.sub("n't$", '', word)
    wordedx = re.sub("ed$", '', word)
    worddx = re.sub("d$", '', word)
    wordenx = re.sub("en$", '', word)
    wordingx = re.sub("ing$", '', word)
    wordlyx = re.sub("ly$", '', word)

    words = word + "s"
    wordes = word + "es"
    wordnt = word + "n't"
    worded = word + "ed"
    wordd = word + "d"
    worden = word + "en"
    wording = word + "ing"
    wordly = word + "ly"

    if word not in msterms and words not in msterms and wordes not in msterms and wordnt not in msterms \
            and worded not in msterms and wordd not in msterms and worden not in msterms \
            and word not in msterms and wordsx not in msterms and wordesx not in msterms \
            and wordntx not in msterms and wordedx not in msterms and worddx not in msterms \
            and wordenx not in msterms and wording not in msterms and wordingx not in msterms \
            and wordly not in msterms and wordlyx not in msterms:
        if word not in writeme:
            writeme.append(word)
        else:
            dupewriteme.append(word)
    else:
        dntwriteme.append(word)

writeme = sorted(writeme)
dupewriteme = sorted(dupewriteme)
dntwriteme = sorted(dntwriteme)


scribe = ""

for line in writeme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("cTerm/Diff.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()

scribe = ""

for line in dntwriteme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("cTerm/Same.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()

scribe = ""

for line in dupewriteme:
    scribe += line + "\n"

scribe = re.sub("\n$", "", scribe)

writefile = open("cTerm/DUPES.txt", 'w+', encoding="utf8")
writefile.write(scribe)

writefile.close()
