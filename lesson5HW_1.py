score = []
x = int(input('學生數量?'))

for i in range(x):
        
    y = int(input('學生成績?'))
    score.append(y)


print(score)
mean = sum(score)/ len(score)

print(mean)