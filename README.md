# MIME ***Microbiome Metagenomic Data Simulator***

<p align="center">
  <img src="https://github.com/fjuradorueda/MIME/blob/main/version%202.png" alt="drawing" width="400"/>
</p>

MIME is a python pipeline to simulate multiple microbial Illumina sequences like data. The strength of this pipeline is the broad number of sequences' features that can be tuned, perfectly controlling up to 11 features of your data

## Features

| Parameters | [Values]/Default | Description |
| :---: | :---: | :---: |
| --number | [0-inf]/Mandatory | **Number of reads** you want to obtain from each genome.Alternatively, the cover rate can be provided, in this case, the number of sequences is modified for each genome in order to cover them equally |
| --mean |  [0-inf]/Mandatory| **Mean sequence length** Final sequence length is subtracted out of a normal distribution|
| --sd | [0-inf]/ 0| **Standard Deviation** If not specified or set to 0, all sequences will have mean length. Final sequence length is subtracted out of a normal distribution||
| --cover | [0-1]/Mandatory | **Genome Coverage** Is the alternative to set --number and --mean. When defining cover, all read will have the same length to fulfill the Lander/Waterman equilibrium. You still may set --mean as well|
| --q | [16-40]/35 | **Mean base call quality** Number equivalent to the mean phred quality score. A "bad quality tail" is added to the end of all sequences to mimic real illumina performance |
| --ER | [0-1]/0 | **Error rate** It is a nucleotide rate. Random nucleotides switches |
| --contaminant_rate | [0-1]/0 | **Contaminant rate**  It is a reads rate. Phage PhiX174 is used as a contaminant (i.e. it is used as + control for Illumina) |
| --dupli_rate| [0-1]/0| **Duplicate rate** It is a reads rate. |
| --adapters_rate | [0-1]/0 | **Duplicate rate** It is a reads rate. Forward reads: i5. Backwards reads: i7 .Obtained from illumina manual https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/experiment-design/illumina-adapter-sequences-1000000002694-14.pdf|
| --adapters_size | [0-32]/8 | **Adapters Size** |
| --molecule_type | ['RNA','DNA']/'DNA' | **Molecule type** for output files|
| --paired | [Boolean]/False | **Sequenences can be single or paired** |
| --formatt | ['FASTQ_i','FASTQ_s','SAM']/'SAM' | **Type of file format** Fasta interleaved for paired sequences. Fasta separated, meaning that forward and backwards reads are collected in separated files. SAM file |
| --read_name | [str()]/'MIME' | **Read name** Initial part of each read's name|
| --select_pro | ['random','non-random']/'non-random' | **Sequences selection process** Non-random process consist of a ORF search along all the genome. All of the positions of the initial codons are stored and used as point of initiation |
## Setting up

MIME takes as input bacterial genomes in fasta format. We recommend you download your "Complete genomes" from NCBI Nucleotide repository 

https://www.ncbi.nlm.nih.gov/nuccore

Make sure one one sequence is present in the fasta, **NO PLASMIDS are allowed**

NCBI's fasta file name is "sequence.fasta.txt". Please rename the fasta file with the species name separated by '_' **This process is key for naming final files**

```
mv sequence.fasta.txt Genus_species.fa
```
## Usage 
The genomes are always mandatory, then you can either specify the genome coverage or the numers of reads and mean length. 

```
./HM2.py --number 100 --mean 50 --genomes *.fa
```

## Output
By default it will generate all files in the same folder,therefore we recommend you create and work on a brand new folder

and outputs a file with all microbial sequences with the characteristics previously tuned.

Parameters to be tuned:

#### Number of sequences
The number of reads coming from each genome. Alternatively, the cover rate can be provided, in this case, the number of sequences is modified for each genome in order to cover them equally

#### Sequence length
Mean and standard deviation can be tuned. Final sequence length is subtracted out of a normal distribution

#### Mean base call quality
Number equivalent to the mean phred quality score. A "bad quality tail" is added to the end of all sequences to mimic real illumina performance

#### Paired sequences (logic)
Sequenences can be single or paired

#### Error rate
It is a nucleotide rate. Default == 0

#### Contaminant rate
Phage PhiX174 is used as a contaminant (i.e. it is used as + control for Illumina). It is a reads rate. Default == 0

#### Duplicate rate
It is a reads rate. Default == 0

#### Molecule output type
it can be 'RNA' or 'DNA'. Default =='DNA'

#### Output Format
It can be SAM, FASTA_i, FASTA_s

#### Reads Name
Character. Default == 'MIME'

#### File Name: character
Default == Name of microbial genome
