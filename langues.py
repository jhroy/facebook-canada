# coding: utf-8
# ©2020 Jean-Hugues Roy. GNU GPL v3.

import csv, langid
# from textblob import TextBlob
from langdetect import detect
from polyglot.detect import Detector
from collections import Counter

fichMedias = "pages-canada.csv"
fichCan = "canada.csv"
fichOut = "canada-avec-langues.csv"

mediasID = []

f = open(fichMedias)
medias = csv.reader(f)
next(medias)

for media in medias:
	if media[4] == "media":
		# print(media)
		mediasID.append(media[0])

print(mediasID)

f = open(fichCan)
can = csv.reader(f)
	# next(can)

for c in can:
	post = c
	langues = []
	texte = c[9].strip() + " " + c[10].strip() + " " + c[11].strip() + " " + c[12].strip()
	texte = texte.lower().strip()
	print("«")
	print(texte)
	print("»")

	try:
		if texte is not None and texte != "":
			# print(detect(texte))
			langues.append(detect(texte)) # Utilisation de langdetect
			# lang = TextBlob(texte)
			# print(lang.detect_language())
			# langues.append(lang.detect_language())
			# print(langid.classify(texte),type(langid.classify(texte)))
			# for l in langid.classify(texte):
				# print(langid.classify(texte).index(l),l)
			# print(langid.classify(texte)[0])
			langues.append(langid.classify(texte)[0]) # Utilisation de langid
			detecteur = Detector(texte)
			langues.append(detecteur.language.code) # Utilisation de polyglot
			# print(detecteur.language.code)
			print(langues)
			freq = Counter(langues)
			# print(freq.most_common(1)[0][0],freq.most_common(1)[0][1])
			if freq.most_common(1)[0][1] > 1:
				langue = freq.most_common(1)[0][0]
			else:
				langue = "inconnue"
		else:
				langue = "inconnue"
	except:
		langue = "inconnue"
		# print("##############################")
		# print("### Pas pu faire l'analyse ###")
		# print("##############################")
	print(langue)

	if c[2] in mediasID:
		print(c)
		ctu1media = "oui"
	else:
		ctu1media = "non"
	
	post.append(ctu1media)
	post.append(langue)

	print(post)

	mark = open(fichOut, "a")
	zuck = csv.writer(mark)
	zuck.writerow(post)

	print("...")
