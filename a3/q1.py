f1 = open('ciphertext1','r')
f2 = open('ciphertext2','r')
f1 = f1.read()
f2 = f2.read()

def btoc(c1,c2):
    return chr(ord(c1) ^ ord(c2))

s = ""
lf1 = len(f1)
for i in range(lf1):
    s += btoc(f1[i], f2[i])

print s

s_new = ""

#https://en.wikipedia.org/wiki/Srm_%28Unix%29
#https://en.wikipedia.org/wiki/OBD_Memorial

#the_string = "Attempting to secure delete a file with multiple hard links results in a warning from srm stating that the current access path has been unlinked, but the data itself was not overwritten or truncated. This is an undocumented feature of srm 1.2.8 on Mac OS X 10.9, and is erroneously documented in 1.2."
#the_string = "The project was launched in November 2006 and the online database was opened for the public access on March 31, 2007. The main sources of information are funds of the Central Archive of the Russian Ministry of Defence (TsAMO) and funds of Military-Memorial Center of the Armed Forces of Russia, inclu"
ts2 = ""
ts_len = len(the_string)

i = 0
while i < lf1:
    y = 0
    s_new = ""
    for j in range(i,i+ts_len):
        s_new += btoc(the_string[y],s[j])
        y += 1
#    print str(i) + ": " + s_new                #to get the plaintext
    i += 1
    if i+ts_len >= lf1:
        i = lf1

p1 = "Attempting to secure delete a file with multiple hard links results in a warning from srm stating that the current access path has been unlinked, but the data itself was not overwritten or truncated. This is an undocumented feature of srm 1.2.8 on Mac OS X 10.9, and is erroneously documented in 1.2."
p2 = "The project was launched in November 2006 and the online database was opened for the public access on March 31, 2007. The main sources of information are funds of the Central Archive of the Russian Ministry of Defence (TsAMO) and funds of Military-Memorial Center of the Armed Forces of Russia, inclu"

##verification program##
c1p1 = ""
c1p2 = ""
c2p1 = ""
c2p2 = ""
#print s
for i in range(lf1):
    c1p1 += btoc(p1[i], f1[i])
    c1p2 += btoc(p2[i], f1[i])
    c2p1 += btoc(p1[i], f2[i])
    c2p2 += btoc(p2[i], f2[i])

#c1p1, c2p2 are the K that encoded ciphertext1, ciphertext2

#verification step
#if c1p1 == c2p2:
#    print "ciphertext1 = plaintext1"
#elif c1p2 == c2p1:
#    print "ciphertext1 = plaintext2"

test_STRING1 = ""

##sanity check to make sure encoded keys c1p1 is the key##
#input: f1 to output ciphertext1, f2 to output ciphertext3
for i in range(lf1):
    test_STRING1 += btoc(c1p1[i],f2[i])
#print test_STRING1
