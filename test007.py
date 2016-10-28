fin = open (u'C:\搬家\eBS学习\python\python\in.txt',encoding='utf8')
fout = open (u'C:\搬家\eBS学习\python\python\out.txt','a',encoding='utf8')
for each_line in fin:
    fout.writelines(each_line)
fin.close()
fout.close()
