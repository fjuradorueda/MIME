# MIME Microbiome Metagenomic Data Simulator

<p align="center">
  <img src="https://github.com/fjuradorueda/MIME/blob/main/version%202.png" alt="drawing" width="400"/>
</p>

Python pipeline devised to simulate multiple microbial Illumina sequences like data. The strength of this pipeline is the broad number of sequences' features that can be tuned. It takes as input bacterial genomes and outputs a file with all microbial sequences with the characteristics previously tuned.

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
