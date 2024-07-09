a = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		a.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(a))
print('檔案讀取完了，總共有', len(a), '筆留言')

sum_len = 0
for d in a:
	sum_len += len(d)


print('每筆留言平均長度為：', sum_len / count,)
