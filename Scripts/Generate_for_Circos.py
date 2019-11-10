import re

Ref_File = open('/home/peter/Desktop/DiseaseDetector(DD Paper)/RESULTS/FromAwesom.tsv' , 'r').readlines()
Data_File = open('/home/peter/Desktop/DiseaseDetector(DD Paper)/Data/awesome-all.tsv', 'r').readlines()[1:]
For_Circos = open('For_Circos.txt','w')
For_Circos.write('Type	Chromosome	Start	End	-log10(q-value)	G-score	average amplitude	frequency\n')

forbidden = ['Y', 'X', 'MT']

for record in Ref_File:
    record = re.split('\t', record)
    for i, line in enumerate(Data_File):
        line = re.split('\t', line)
        chromosome = re.split(':',line[1])
        chromosomeNum = chromosome[0].replace('chr','')
        location = chromosome[1]
        start = int(location)
        end = int(location)
        if record[4:] == line [4:] and chromosomeNum not in forbidden :
            print(chromosomeNum)
            For_Circos.write('Amp	 %s	%s	%s	0.744936	0.162607	0.985882	0.258824\n' % (chromosomeNum, start, end))
