import sys
import time
def DrawNetwork(command):
    try:
        if command == '-networkon':
            time.sleep(2)
            print('Network Analysis Activated')
            time.sleep(2)
            Network = []
            import re
            SourceFile = open('./Data/clinical_ann_metadata.tsv', 'r').readlines()
            GeneFile = open('./RESULTS/FromAwesom.tsv', 'r').readlines()
            for line in GeneFile:
                line = re.split('\t', line)
                GeneName = line[2]
                break

            for record in SourceFile:
                record = re.split('\t', record)
                Gene = record[2].replace('","', '    ')
                SNP = record[1].replace('","', '    ')
                drug = record[11].replace('","', '    ')
                disease = record[12].replace('","', '    ')
                Annotations = record[6].replace('","', '    ')

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
                    NewList.append(Annotations)
                    NewList.append(drug)
                Network.append(NewList)






            Network = [x for x in Network if x != []]
            # print(Network)

            from webweb import Web
            edge_list = Network
            Web(edge_list).save("./RESULTS/%sVarPhenoDrugNetwork.html" % GeneName)
            # Web(edge_list).show()

            print("Network Analysis Finished")
        elif command == '-networkoff':
            print("Network Analysis Switched OFF")
    except:
        raise
        # print('Please, Enter The Network Construction Option [-networkoff] [-networkon] ')
        # sys.exit()
