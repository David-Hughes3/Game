
row = ['W2V_0.3', 'W2V_0.5','W2V_0.7', 
'Glove300_0.3','Glove300_0.5','Glove300_0.7', 
'Glove200_0.3','Glove200_0.5','Glove200_0.7', 
'Glove100_0.3','Glove100_0.5','Glove100_0.7',
'Glove50_0.3','Glove50_0.5','Glove50_0.7',
'W2V_Glove300_0.3', 'W2V_Glove300_0.5','W2V_Glove300_0.7', 
'W2V_Glove200_0.3', 'W2V_Glove200_0.5','W2V_Glove200_0.7', 
'W2V_Glove100_0.3', 'W2V_Glove100_0.5','W2V_Glove100_0.7', 
'W2V_Glove50_0.3', 'W2V_Glove50_0.5','W2V_Glove50_0.7']

column = ['W2V', 'Glove300','Glove200', 'Glove100','Glove50',
'W2V_Glove_300', 'W2V_Glove200', 'W2V_Glove_100', 'W2V_Glove50',
'Wordnet_Path','Wordnet_Wup', 'Wordnet_Lin','Wordnet_Res','Wordnet_Lch','Wordnet_Jcn']

table = []
# for i in row:
# 	for j in column:
# 		table.append([i,j])


# val1 = []
# with open('bot-results/A_w2v.txt') as infile:
# 	for line in infile:
# 		line = line.rstrip().split(' ')
# 		val1.append(line)

# counter1 = 0
# minimum = 100
# c = []
# for i in val1:
# 	try:
# 		head, sep, tail = i[0].partition(':')
# 		int_val = int(tail)

# 		if int_val < minimum:
# 			minimum = int_val

# 		if 'SEED:1550' in i:
# 			c.append(minimum)
# 			minimum = 100
# 	except:
# 		continue
		

# print(c)

# for i in c:
# 	head, sep, tail = i[0].partition(':')
# 	int_tail = int(tail)

# 	if 'SEED:1550' in i:
# 		print(minimum)
# 		minimum = 100




table = [[100, 100, 100, 76.67, 66.67, 56.67, 90, 86.67, 53.33, 90, 93.33, 70, 86.67, 86.67, 76.67, 93.33, 93.33, 93.33, 93.33, 93.33, 93.33, 96.67, 96.67, 76.67, 90, 86.67, 66.67],
        [86.67, 86.67, 76.67, 100, 100, 100, 96.67, 96.67, 96.67, 96.67, 96.67, 90, 100, 83.33, 83.33, 100, 100, 100, 100, 100, 100, 100, 100, 93.33, 96.67, 96.67, 73.33],
		[80, 80, 76.67, 100, 100, 100, 100, 100, 100, 93.33, 93.33, 96.67, 90, 80, 56.67, 100, 100, 100, 100, 100, 100, 96.67, 96.67, 83.33, 93.33, 93.33, 70],
		[73.33, 73.33, 63.33, 100, 100, 100, 90, 90, 80, 100, 100, 100, 93.33, 80, 73.33, 100, 100, 96.67, 96.67, 96.67, 100, 100, 100, 90, 96.67, 96.67, 86.67],
		[73.33, 73.33, 56.67, 90, 90, 90, 86.67, 86.67, 86.67, 93.33, 93.33, 80, 100, 100, 100, 90, 90, 83.33, 93.33, 93.33, 83.33, 96.67, 96.67, 90, 96.67, 96.67, 93.33],
		[90, 90, 86.67, 100, 100, 100, 96.67, 96.67, 96.67, 93.33, 90, 90, 93.33, 73.33, 73.33, 100, 100, 100, 100, 100, 100, 100, 100, 100, 93.33, 93.33, 80],
		[86.67, 86.67, 83.33, 100, 100, 100, 100, 100, 100, 93.33, 86.67, 86.67, 90, 80, 66.67, 100, 100, 100, 100, 100, 100, 100, 100, 90, 96.67, 96.67, 66.67],
		[86.67, 86.67, 76.67, 96.67, 96.67, 96.67, 90, 90, 83.33, 96.67, 96.67, 100, 93.33, 83.33, 86.67, 100, 100, 100, 96.67, 96.67, 100, 100, 100, 100, 96.67, 96.67, 86.67],
		[80, 80, 73.33, 96.67, 93.33, 93.33, 96.67, 96.67, 93.33, 93.33, 86.67, 93.33, 73.33, 80, 90, 100, 100, 100, 100, 100, 100, 100, 100, 90, 86.67, 83.33, 100],
		[23.33, 23.33, 13.33, 20, 23.33, 13.33, 23.33, 26.67, 20, 20, 16.67, 20, 13.33, 16.67, 16.67, 20, 20, 20, 20, 20, 10, 23.33, 30, 20, 33.33, 10, 20],
		[36.67, 36.67, 26.67, 20, 20, 23.33, 16.67, 20, 20, 20, 26.67, 26.67, 16.67, 20, 13.33, 23.33, 23.33, 23.33, 16.67, 16.67, 20, 20, 16.67, 10, 26.67, 26.67, 13.33],
        [26.67, 26.67, 20, 20, 23.33, 33.33, 16.67, 23.33, 26.67, 10, 23.33, 20, 10, 16.67, 13.33, 16.67, 20, 33.33, 23.33, 16.67, 23.33, 23.33, 20, 10, 16.67, 16.67, 10],
        [36.67, 36.67, 20, 16.67, 16.67, 33.33, 16.67, 20, 23.33, 16.67, 16.67, 13.33, 16.67, 20, 23.33, 23.33, 26.67, 36.67, 36.67, 23.33, 33.33, 33.33, 30, 20, 26.67, 20, 16.66],
        [30, 30, 20, 23.33, 33.33, 23.33, 13.33, 23.33, 33.33, 30, 26.67, 13.33, 20, 20, 10, 20, 23.33, 23.33, 36.67, 20, 23.33, 26.67, 10, 20, 10, 16.67, 23.33],
        [16.67, 16.67, 23.33, 10, 20, 16.67, 13.33, 13.33, 26.67, 10, 16.67, 13.33, 13.33, 6.67, 3.33, 13.33, 13.33, 16.67, 16.67, 16.67, 16.67, 16.67, 13.33, 13.33, 20, 10, 10]]

for i in table:
	for j in i:
		print(j/100)
	print("\n")




