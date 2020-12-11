from collections import Counter
file = open("test.txt")
lines = file.readlines()

for i,line in enumerate(lines):
    lines[i] = list(line.strip("\n"))



print(len(lines))
coll = len(lines)
out = 1
last = 0
ran = 0
while out != last:
    ran += 1
    print("ran = " + str(ran))
    out = 0
    for i in range(coll):
        rowl = len(lines[i])
        for j in range(rowl):

            cell = lines[i][j]
            if cell == '.':
                continue
            surrounded = []
            if j != 0:
                surrounded.append(lines[i][j-1])
            if i != 0 and not j >= len(lines[i-1]):
                surrounded.append((lines[i-1][j]))
            if i != 0 and j != 0 and not j >= len(lines[i-1]):
                surrounded.append((lines[i - 1][j-1]))
            if i+1 < coll-1 and not j >= len(lines[i+1]):
                a = lines[i + 1]
                b = a[j]
                surrounded.append(b)
            if j+1 < rowl-1:
                surrounded.append(lines[i ][j+1])
            if i+1 < coll-1 and j+1 < rowl-1 and not j+1 >= len(lines[i+1]):
                a = lines[i + 1]
                b = a[j + 1]
                surrounded.append(b)

            if i+1 < coll-1 and j+1 != 0 and not j >= len(lines[i+1]):
                surrounded.append(lines[i + 1][j - 1])
            if i != 0 and j+1 < rowl-1 and not j+1 >= len(lines[i-1]):
                surrounded.append(lines[i - 1][j +1 ])

            if cell == 'L' and '#' not in surrounded:
                lines[i][j] = '#'
            cn = Counter(surrounded)
            if cell == '#' and cn['#'] >= 4:
                lines[i][j] = 'L'
    for line in lines:
        print(line)
        cn = Counter(line)
        out += cn['#']

# 1934


print(out)
print(ran)
