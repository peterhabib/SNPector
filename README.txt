#DiseaseCatcher(DC)
According to uncovering of genetic roots of many disease, the need of tool to investigate the DNA of patient to find out what kinds of varients are located in and how it could controbute in the disease. DiseaseCatcher (DC) is a python software combine between different other software could detect variants in given sequence and illustrate to which diseas those variants are contribute






1- Open the directory where scan_dna.py located

2 - Open terminal in current DC directory


#Downloading required data and software
3- Download Datasets
   Download Humen Genome: wget ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz
   Download NCBI BLAST: wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.9.0+-x64-linux.tar.gz
   Download ClinVar Dataset: wget ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar_20190923.vcf.gz
   Download Genome Browser: http://d3gb.usal.es/docs/package/py/D3GB-1.1.tar.gz


#Data and software Preparation
4- Extract zipped downloaded files

5- From "/ncbi-blast-2.9.0+/bin" and copy "makeblastdb" and "blastn" to the same directory of scan_dna.py

6- building BLAST Database: ./makeblastdb -in GRCh38_latest_genomic.fna -dbtype nucl -out Hum_Genom38



#How To Use
7- Run Scanning on sequence: python3 Start_Scan.py fasta_file_name gene_name








