# SNPector
According to uncovering of genetic roots of many disease, the need of tool to investigate the DNA of patient to find out what
kinds of varients are located in and how it could controbute in the disease. SNPector is a python software combine
between different other software could detect variants in given sequence and illustrate to which diseas those variants are
contribute




-Open the directory where scan_dna.py located

-Open terminal in current DC directory


# Downloading required data and software
-Download Humen Genome: wget ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz
-Download NCBI BLAST: wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.9.0+-x64-linux.tar.gz
-Download ClinVar Dataset: wget ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar_20190923.vcf.gz
-Download Genome Browser: http://d3gb.usal.es/docs/package/py/D3GB-1.1.tar.gz


# Data and software Preparation
-Extract zipped downloaded files

-From "/ncbi-blast-2.9.0+/bin" and copy "makeblastdb" and "blastn" to the same directory of scan_dna.py

-building BLAST Database: ./makeblastdb -in GRCh38_latest_genomic.fna -dbtype nucl -out Hum_Genom38


# Publication
https://f1000research.com/articles/8-2133/v1

# zenodo source code
https://zenodo.org/record/3558393#.Xf1FKnUzZnw

# Supplementary of Study
https://zenodo.org/record/3569790#.Xf1FLnUzZnw



# How To Use
[Usage](https://raw.githubusercontent.com/peterhabib/SNPector/master/Updated_Figure(2).jpg)

**A)** Python3 compiler; 
**B)** scan_dna.py: program main script that contain all functions; 
**C)** -blaston / -blastoff: in order to initiate BLAST process to provide sequence alignment against the genome to locate 
wherethe sequence is situated, if the -blastoff is chosen it will use previous BLAST results; 
**D)** -modescan: to scan the given sequence and find out whether SNP occurs or exists in sequence or not, and -modesearch:
to extract all SNPs occur in this range of sequence regardless they are exist or not; 
**E)** -circoson: draws a Circos figure to illustrate where SNPs with same properties/effect are located; 
**F)** -networkon: in order to link between SNPs, diseases and drugs and produces network HTML file; 
**G)** -download: activates the API to download data for identified SNPs from LDlink database; 
**H)** -vis: produces different figures and plots; 
**I)**  GivenSequence.fasta: Tte user-provided sequence in FASTA file format. Any of the previous parameters can be
deactivated when replaced with -off.
