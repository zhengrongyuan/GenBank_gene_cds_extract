# -*- coding: cp936 -*-
print '������Ҫ�򿪵��ļ�����'
inputfname=raw_input()
inputf=open(inputfname)
lines=inputf.readlines()
inputf.close()

#��ȡ�����ֻ��������е��б�seqs
numln=0     #��¼for������������   
seqs=[]     #�����洢�����������е��б�
for line in lines:
    if 'ORIGIN' in line:
        j=1
        seq=''  #������ʼ��
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
    if 'ACCESSION ' in aline:    #��ȡaccesion
        oraccession=aline.split()[1]
        if '_' in oraccession:
            accession=oraccession.split('_')[0]+oraccession.split('_')[1]
        else:
            accession=oraccession
        
        
    elif '   gene   ' in aline:  #��ȡ��������
        genename=lines[numline+1].split('"')[1]
        outf=open(genename+'NT.fas','a')
        outf.write('>'+accession+'\n')

    elif '  CDS  ' in aline:#��ȡ����Ƭ�η�Χ
        region=re.findall(r'(\d+)',aline)   #��ȡ�ַ����е���������
        start=int(region[0])
        end=int(region[1])
        if ' complement(' in aline:
            gene_r=seqs[numacc][start-1:end]
            gene_cds=''.join(["atcgywsrmbdhvn"["tagcrwsykvhdbn".index(n)] for n in gene_r[::-1]])   #��÷��򻥲�����
        else:
            gene_cds=seqs[numacc][start-1:end]
        outf.write(gene_cds+'\n')
        outf.close()
        print accession,genename,'������ȡ�ɹ�'

    elif 'ORIGIN' in aline: #��ȡ����Ƭ��
        numacc+=1
        
    numline+=1

inputf.close()

print '�������'
raw_input()



     
        
