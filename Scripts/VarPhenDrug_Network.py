

# Clinical Annotation ID	Location	Gene	Level of Evidence	Clinical Annotation Types	Genotype-Phenotype IDs	Annotation Text	Variant Annotations IDs	Variant Annotations	PMIDs	Evidence Count	Related Chemicals	Related Diseases	Race	Chromosome

Network = []
GeneName = 'EGFR'
import re
SourceFile= open('/home/peter/Desktop/Biotechnology/DiseaseCatcher2/PharmGKB/annotations/clinical_ann_metadata.tsv', 'r').readlines()

for record in SourceFile:
    record = re.split('\t', record)
    Gene = record[2].replace('","','    ')
    SNP = record[1].replace('","','    ')
    drug = record[11].replace('","','    ')
    disease = record[12].replace('","','    ')
    Annotations = record[6].replace('","','    ')
    population = record[13].replace('","','    ')


    NewList = []
    if GeneName in record[2]:
        NewList.append(Gene)
        NewList.append(SNP)
    Network.append(NewList)

    NewList = []
    if GeneName in record[2]:
        NewList.append(SNP)
        NewList.append(disease)
    Network.append(NewList)


    NewList = []
    if GeneName in record[2]:
        NewList.append(disease)
        NewList.append(drug)
    Network.append(NewList)

    NewList = []
    if GeneName in record[2]:
        NewList.append(drug)
        NewList.append(Annotations)
    Network.append(NewList)












Network = [x for x in Network if x != []]
from webweb import Web
edge_list = Network
Web(edge_list).show()