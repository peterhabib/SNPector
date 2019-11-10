import re

SourceFile = open('/home/peter/Desktop/DiseaseDetector(DD Paper)/Data/clinicalVariants.tsv', 'r').readlines()
ExpectedFile = open('/home/peter/Desktop/DiseaseDetector(DD Paper)/RESULTS/FromPharmGKB.tsv' , 'r').readlines()
RS_Pos = open('/home/peter/Desktop/DiseaseDetector(DD Paper)/Data/clinvar_20191001.vcf', 'r').readlines()
FromPharmGKBtoCircos = open('FromPharmGKBtoCircos.py.tsv', 'w')

for hit in ExpectedFile:
    hit = re.split('\t', hit)
    drug = hit[4]
    RSName = hit[0]
    for record in RS_Pos:
        if RSName in record:
            print(record)
    # for record in SourceFile:
    #     record = re.split('\t', record)
    #     if drug in record:
    #         print(record)

