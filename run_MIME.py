#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import sys
import random

# This script requires:
# 
# n:    number of sequences desired for each genome \n
#
# l:    reads length desired \n
#
# q:    quality per base \n
#
# paired:    logical \n
#
# format:    SAM,FASTA_i,FASTA_s \n
#
# genoma_name(s):    genomes downloaded. Must be in multifastq format\n



# In[ ]:
numero=int(sys.argv[1])
l=int(sys.argv[2])
q=sys.argv[3]
paired=sys.argv[4]
formatt='SAM'
genomes=sys.argv[6:]


#### Sequences are paired-end. Which means that "mate" is complementary reverse to "read" chain in 50% of the cases

# In[39]:


def reverscomp(a): #You SHOULD regard a case in which you get a read containing other letters. For instance RNA, errors...
    tr=[]
    for i in a:
        if i=='A':
            tr.append('T')
        if i=='T':
            tr.append('A')
        if i=='C':
            tr.append('G')
        if i=='G':
            tr.append('C')
    return ''.join(tr)[::-1]



if formatt=='SAM':
    fe=open('generated.sam','wb') #We generate a sam file. this time the inside structure is diferent obviously
    
    for genome in genomes: #ALL GENOMES SHOULD CONTAIN JUST ONLY ONE LONG SEQUENCE. WITHOUT PLASMID AND OTHER STUFF
        
        file=open(genome,'r') 
        f=file.readlines()   
        
        header=f[0]  
        fi=f[1:]
        fi=''.join(fi)
        fi=fi.replace('\n','')
        
        for y in range(numero):
	    gz=random.randint(80,120)
	    pfinal=(len(fi)-(l*2+gz)) #there should be '+120' but we provide in here a wider buffer zone just in case. It did yielded problems
            pi=random.randint(0,pfinal)
    
            first=fi[pi:pi+l]
            if paired=='TRUE':
                second=fi[pi+gz+l:pi+gz+l*2]
		second_rc=reverscomp(second)
                L=[second,second_rc] 
                
		#we preserve the 11 fields structure.
                a='CNIO:{}:{}'.format(header[1:-1],y)+"\t77\t*\t0\t0\t*\t*\t0\t0\t"+first+'\t'+l*q+'\n'
                b='CNIO:{}:{}'.format(header[1:-1],y)+"\t141\t*\t0\t0\t*\t*\t0\t0\t"+L[int(np.random.randint(2,size=1))]+'\t'+l*q+'\n'
        
                #byte format before writing 
                a=a.encode('utf-8') 
                b=b.encode('utf-8')
         
                fe.write(a)
                fe.write(b)
                del (a,b)
            else:
                a='CNIO:{}:{}'.format(header[1:-1],y)+"\t4\t*\t0\t0\t*\t*\t0\t0\t"+first+'\t'+l*q+'\n'
                a=a.encode('utf-8') 
                fe.write(a)
                del(a)
    fe.close()

