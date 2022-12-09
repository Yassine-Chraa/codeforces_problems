line1 = input()
line2 = input()
line1_inputs  = line1.split(" ")
n = int(line1_inputs[0])
k = int(line1_inputs[1])

scores = line2.split(" ")
count = 0
for i in range(n):
    if int(scores[i]) >= int(scores[k-1]) and int(scores[i]) >0:
        count = count+1
print(count)