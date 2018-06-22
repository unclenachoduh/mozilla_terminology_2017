# Last Run: 6/26/17 12:34 pm - 2262 strings
import re


def add_word():
    print("no")

file = open('mytext.txt', encoding="utf8")

content = file.read()
file.close()
content = re.sub("&lt;[^;]*&gt;", "~", content)
content = re.sub("&amp;[^;]*;", "~", content)
# content = re.sub("&amp;[^;]*;", "~", content)
content = re.sub("[‘’]", "'", content)
content = re.sub("[?.,#!$%^*:;{}=\"—“”|_`~()\[\]…]", "~", content)  # / -
content = re.sub("\s['-]", "", content)
content = re.sub("['-]\s", "", content)

text = content.split("\n")

print("CONTENT ready for cleaning\n")

acceptedline = []  # array of strings - desired lines from the original file

for line in text:
    if re.match("^.*<tuv xml~lang~~en-US~><seg>.*$", line):
        line = re.sub('<(.|\n)*?>', '~', line)
        line = re.sub('[\t+­–\d]', '~', line)
        line = re.sub('~', '', line)
        acceptedline.append(line)
#        print("YESSSSS: " + line)
    else:
        rom = 1
        rom += 1
#        print("NOPE: " + line)

cleanlines = []

for line in acceptedline:
    if line not in cleanlines:
        cleanlines.append(line)

writefile = open("eTerm/mozorgStrings.txt", 'w+', encoding="utf8")

for line in cleanlines:
    writefile.write(line + "\n")

writefile.close()


print("LINES ready for splitting\n")

acceptedwords = []  # array of strings - non duplicate words

# for line in cleanlines:
#     words = line.split("\s")
#     for each in words:
#         print(each)

strang = ""

for line in cleanlines:
    if line == cleanlines[0]:
        strang += line.lower()
    else:
        strang += " " + line.lower()

print("WORDS ready for common compare\n")

wordbase = strang.split(' ')
wordlist = []

readfile = open("RESOURCES/1000words.txt", encoding="utf8")
common = readfile.read()
readfile.close()

commonwords = common.split('\n')

duperejects = []
comrejects = []
shittyrejects = []

for word in wordbase:
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

    if word not in wordlist and words not in wordlist and wordes not in wordlist and wordnt not in wordlist \
            and worded not in wordlist and wordd not in wordlist and worden not in wordlist \
            and word not in wordlist and wordsx not in wordlist and wordesx not in wordlist \
            and wordntx not in wordlist and wordedx not in wordlist and worddx not in wordlist \
            and wordenx not in wordlist and wording not in wordlist and wordingx not in wordlist \
            and wordly not in wordlist and wordlyx not in wordlist:
        if word not in commonwords and words not in commonwords not in commonwords and wordes not in commonwords \
                and wordnt not in commonwords and worded not in commonwords and wordd not in commonwords \
                and worden not in commonwords and word not in commonwords and wordsx not in commonwords \
                and wordesx not in commonwords and wordntx not in commonwords and wordedx not in commonwords \
                and worddx not in commonwords and wordenx not in commonwords and wording not in commonwords \
                and wordingx not in commonwords and wordly not in commonwords and wordlyx not in commonwords:
            if re.match("^https.*$", word):
                temp = word + "\n"
                if temp not in shittyrejects:
                    shittyrejects.append(temp)
            elif len(word) < 2:
                temp = word + "\n"
                shittyrejects.append(temp)
            else:
                wordlist.append(word)
        else:
            temp = word + "\n"
            if temp not in comrejects:
                comrejects.append(temp)
    else:
        temp = word + "\n"
        if temp not in duperejects:
            duperejects.append(temp)

writefile = open("eTerm/shitrejectedwords.csv", 'w+', encoding="utf8")
for line in shittyrejects:
    writefile.write(line)
writefile.close()

writefile = open("eTerm/duperejectedwords.csv", 'w+', encoding="utf8")
for line in duperejects:
    writefile.write(line)
writefile.close()

writefile = open("eTerm/comrejectedwords.csv", 'w+', encoding="utf8")
for line in comrejects:
    writefile.write(line)
writefile.close()

print("WORDS ready for counting\n")

wordfreq = []
for w in wordlist:
    wordfreq.append(wordbase.count(w))

print("TERMS ready for writing\n")

writefile = open("eTerm/mywords.csv", 'w+', encoding="utf8")
#writefile.write("TERM,FREQ\n")
i = 0

wordlist = sorted(wordlist)

for word in wordlist:
    # writefile.write(word + "," + str(wordfreq[i]) + "\n")
    writefile.write(word + "\n")
    i += 1

writefile.close()

