# -*- coding: utf-8 -*-




l = []
for i in range(1,10):
    for s in range(1,10):
        if i <= s:
            try:
                l[s-1].append(str(s) +'X'+str(i))
            except:
                l.append([])
                l[s - 1].append(str(s) + 'X' + str(i))

for ss in l:
    print(ss)






