# -*- coding: cp936 -*-
print '请输入要打开的文件名：'
inputfname=raw_input()
inputf=open(inputfname)
lines=inputf.readlines()
inputf.close()

#提取各物种基因组序列到列表seqs
numln=0     #记录for遍历到的行数   
seqs=[]     #用来存储各基因组序列的列表
for line in lines:
    if 'ORIGIN' in line:
        j=1
        seq=''  #变量初始化
        while lines[numln+j] != '//\n':
            linelist=lines[numln+j].split()
            partseq=''.join(linelist[1:])
            seq+=partseq
            j+=1
        seqs.append(seq)
        
    numln+=1
        
        

inputf=open(inputfname)
lines=inputf.readlines()
inputf.close()
numacc=0
numline=0
import re

for aline in lines:
    if 'ACCESSION ' in aline:    #获取accesion
        oraccession=aline.split()[1]
        if '_' in oraccession:
            accession=oraccession.split('_')[0]+oraccession.split('_')[1]
        else:
            accession=oraccession
        
        
    elif '   gene   ' in aline:  #获取基因名称
        genename=lines[numline+1].split('"')[1]
        outf=open(genename+'NT.fas','a')
        outf.write('>'+accession+'\n')

    elif '  CDS  ' in aline:#获取基因片段范围
        region=re.findall(r'(\d+)',aline)   #提取字符串中的所有数字
        start=int(region[0])
        end=int(region[1])
        if ' complement(' in aline:
            gene_r=seqs[numacc][start-1:end]
            gene_cds=''.join(["atcgywsrmbdhvn"["tagcrwsykvhdbn".index(n)] for n in gene_r[::-1]])   #获得反向互补序列
        else:
            gene_cds=seqs[numacc][start-1:end]
        outf.write(gene_cds+'\n')
        outf.close()
        print accession,genename,'序列提取成功'

    elif 'ORIGIN' in aline: #获取基因片段
        numacc+=1
        
    numline+=1

inputf.close()

print '运行完成'
raw_input()



     
        
