# coding: utf-8
# ©2020 Jean-Hugues Roy. GNU GPL v3.

import csv, glob

n = total = 0
postIDs = []

toute = "canada.csv"

for fichier in glob.glob("*.csv"):
	print(fichier)
	f = open(fichier)
	posts = csv.reader(f)
	next(posts)
	l = 0

	for post in posts:
		n += 1
		l += 1
		# print(post)
		# print(fichier,l,n)
		part1 = post[2]
		if not post[20].startswith("https"):
			# print(post)
			# print(post[20], post[22])
			part2 = post[22].split("a.")[1].split("/")[0]
			# print(part2)
		else:
			part2 = post[20].split("/")[-1]

		postID = "{}_{}".format(part1,part2)
		# print("https://www.facebook.com/{}_{}".format(part1,part2))

		postIDs.append(postID)

		interactions = int(post[-1].replace(",",""))
		total += interactions
		# print(interactions,total,total/n)

		page = post[0]
		code = post[1]
		fbID = post[2]
		try:
			pageLikes = int(post[3])
		except:
			pageLikes = post[3]
		creation = post[4]
		date = creation[:10]
		annee = creation[:4]
		mois = creation[5:7]
		jour = creation[8:10]
		# print(creation,annee,mois,jour)
		typePost = post[5]
		partages = int(post[8])
		likes = int(post[6])
		love = int(post[9])
		wow = int(post[10])
		haha = int(post[11])
		triste = int(post[12])
		colere = int(post[13])
		solid = int(post[14])
		commentaires = int(post[7])
		statutVideo = post[15]
		vuesPost = int(post[16])
		vuesTotal = int(post[17])
		vuesTotalCrossposts = int(post[18])
		dureeVideo = post[19]
		message = post[21]
		texteImage = post[24]
		texteLien = post[25]
		desc = post[26]
		sponsor = post[28]
		sponsorID = post[27]

		# print(vuesPost,vuesTotal,vuesTotalCrossposts)
		# if int(vuesTotal) > 100000000 and statutVideo == "original":
		# 	print(post)

		# for item in post:
		# 	print(item,type(item))
		# print("...")

		nouveau = [
			page,
			code,
			fbID,
			pageLikes,
			date,
			annee,
			mois,
			jour,
			postID,
			message,
			texteImage,
			texteLien,
			desc,
			sponsor,
			sponsorID,
			typePost,
			statutVideo,
			dureeVideo,
			vuesPost,
			vuesTotal,
			vuesTotalCrossposts,
			partages,
			likes,
			love,
			wow,
			haha,
			triste,
			colere,
			solid,
			commentaires,
			interactions
		]

		print(nouveau)

		mark = open(toute,"a")
		zuck = csv.writer(mark)
		zuck.writerow(nouveau)

### Pour vérifier s'il y a des doublons; il n'y en a pas.

print(len(postIDs))
postIDs = set(postIDs)
print(len(postIDs))
