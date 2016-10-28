count = 1
f = open ('C:\\record.txt')
fa = open ('C:\\A' + str(count) + '.txt', 'a')
fb = open ('C:\\B' + str(count) + '.txt', 'a')
for each_line in f:
    if each_line[:6] != '======':
        (role, line) = each_line.split(':',1)

        if role == 'A':
            fa.writelines(temp)
        else:
            fb.writelines(temp)
    else:
        fa.close
        fb.close
        count += 1
        fa = open ('C:\\A' + str(count) + '.txt', 'a')
        fb = open ('C:\\B' + str(count) + '.txt', 'a')

fa.close()
fb.close()
f.close()
