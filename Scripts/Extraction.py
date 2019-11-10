import re
import sys
import time
from operator import itemgetter

def ExtractSNP(command, NCBIclinVar, BLASTfile, SeqFile, SNPinDetails, PharmGKB, SNPinDetailsPharmGKB, AwesomeDB, SNPinDetailsAwesome):
    all_hits=[]
    covarage_sorted=[]
    for line in BLASTfile:
        line=re.split('\t',line)
        all_hits.append(line)

    ######first combining sorting
    sorting=sorted(all_hits, key=itemgetter(2,3,10) , reverse=False)
    start=''
    for i,list in enumerate(sorting):
        covarage_sorted.append(list)

    ######second combining sorting
    covarage_eval=sorted(covarage_sorted, key=itemgetter(5,6) , reverse=False)
    for i,list in enumerate(covarage_eval):
        # print(list)
        if i==100:
            break
    #take first result
    for result in covarage_eval:
        final_result = result
        print(final_result)
        break
    subject_start=final_result[8]
    subject_end=final_result[9]
    ChromosomeID = final_result[1]

    seqs={}
    for line in SeqFile:
        line = line.strip()
        if line.startswith(">"):
            name = line[1:]  # discarding the initial >
            seqs[name] = ''
        else:
            seqs[name]+=line
    sequence=seqs[name]
    print(sequence[:20]+'.........')





    lista=set()
    qeury_start=int(final_result[6]) + int(subject_start)
    qeury_end=int(final_result[7]) + int(subject_start)
    try:
        if command =='-modescan':
            time.sleep(2)
            print('Scan Mode Activated')
            time.sleep(2)
            print('Scanning Starts....')
            for snp in NCBIclinVar:
                snp=re.split('\s',snp)
                snp_chr=snp[0]
                snp_pos=snp[1]
                snp_name=snp[2]
                snp_ref=snp[3]
                snp_alt=snp[4]
                snp_qual=snp[5]
                snp_fil=snp[6]
                snp_info=snp[7]
                snp_info = re.split(';', snp[7])
                for info in snp_info:
                    if info.startswith('ALLELEID'):
                        ALLELEID = info.replace('ALLELEID=','')
                    if info.startswith('CLNDISDB'):
                        CLNDISDB = info.replace('CLNDISDB=','')
                    if info.startswith('CLNDN'):
                        CLNDN = info.replace('CLNDN=','')
                    if info.startswith('CLNHGVS'):
                        CLNHGVS = info.replace('CLNHGVS=','')
                    if info.startswith('CLNREVSTAT'):
                        CLNREVSTAT = info.replace('CLNREVSTAT=','')
                    if info.startswith('CLNSIG'):
                        CLNSIG = info.replace('CLNSIG=','')
                    if info.startswith('CLNVC'):
                        CLNVC = info.replace('CLNVC=','')
                    if info.startswith('CLNVCSO'):
                        CLNVCSO = info.replace('CLNVCSO=','')
                    if info.startswith('CLNVI'):
                        CLNVI = info.replace('CLNVI=','')
                    if info.startswith('GENEINFO'):
                        GENEINFO = info.replace('GENEINFO=','')
                    if info.startswith('MC'):
                        MC = info.replace('MC=','')
                    if info.startswith('ORIGIN'):
                        ORIGIN = info.replace('ORIGIN=','')
                    if info.startswith('RS'):
                        RS = info.replace('RS=','rs')

                query_nuc_alt = sequence[int(snp_pos) - int(subject_end):int(snp_pos) - int(subject_end) + len(snp_alt)]
                query_nuc_ref = sequence[int(snp_pos) - int(subject_end):int(snp_pos) - int(subject_end) + len(snp_ref)]
                if int(subject_start)-1 <= int(snp_pos) <= int(subject_end)+1 and ChromosomeID in CLNHGVS : ### filter all snp in range of subject
                    if query_nuc_alt == snp_alt:
                        print(RS)
                        SNPinDetails.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                            snp_chr, snp_name, snp_pos, snp_qual, snp_fil, ALLELEID, CLNDISDB, CLNDN, CLNREVSTAT,
                            CLNSIG, CLNVC, CLNVCSO, CLNVI, GENEINFO, MC, ORIGIN, RS))

                        for record in PharmGKB:
                            record = re.split('\t', record.strip())
                            if RS in record:
                                print(record)
                                variant = record[0]
                                gene = record[1]
                                type = record[2]
                                levelofevidence = record[3]
                                chemicals = record[4]
                                phenotypes = record[5]
                                SNPinDetailsPharmGKB.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(variant,snp_pos, gene, type, levelofevidence, chemicals, phenotypes))


                        for line in AwesomeDB:
                            line = re.split('\t', line.strip())
                            if RS in line:
                                print(line)
                                rsID = line[0]
                                Location = line[1]
                                GeneSymbol = line[2]
                                ENSP = line[3]
                                AAChange = line[4]
                                Phos = line[5]
                                Ubi = line[6]
                                Meth = line[7]
                                SUMO = line[8]
                                OGalNAc = line[9]
                                OGlcNAc = line[10]
                                NGly = line[11]
                                KAce = line[12]
                                NtAce = line[13]
                                ExpScore = line[14]
                                Ref = line[15]
                                Alt = line[16]
                                SNPinDetailsAwesome.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t'
                                                          '%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(rsID, Location, GeneSymbol, ENSP, AAChange, Phos, Ubi,
                                                          Meth, SUMO, OGalNAc, OGlcNAc, NGly, KAce, NtAce, ExpScore, Ref, Alt))
                        print('------------------------------------------------------------')


            print("Scanning Finished!")

        elif command == '-modesearch':
            time.sleep(2)
            print('Search Mode Activated')
            time.sleep(2)
            print('Searching Starts....')
            for snp in NCBIclinVar:
                snp=re.split('\s',snp)
                snp_chr=snp[0]
                snp_pos=snp[1]
                snp_name=snp[2]
                snp_ref=snp[3]
                snp_alt=snp[4]
                snp_qual=snp[5]
                snp_fil=snp[6]
                snp_info=snp[7]
                snp_info = re.split(';', snp[7])
                for info in snp_info:
                    if info.startswith('ALLELEID'):
                        ALLELEID = info.replace('ALLELEID=','')
                    if info.startswith('CLNDISDB'):
                        CLNDISDB = info.replace('CLNDISDB=','')
                    if info.startswith('CLNDN'):
                        CLNDN = info.replace('CLNDN=','')
                    if info.startswith('CLNHGVS'):
                        CLNHGVS = info.replace('CLNHGVS=','')
                    if info.startswith('CLNREVSTAT'):
                        CLNREVSTAT = info.replace('CLNREVSTAT=','')
                    if info.startswith('CLNSIG'):
                        CLNSIG = info.replace('CLNSIG=','')
                    if info.startswith('CLNVC'):
                        CLNVC = info.replace('CLNVC=','')
                    if info.startswith('CLNVCSO'):
                        CLNVCSO = info.replace('CLNVCSO=','')
                    if info.startswith('CLNVI'):
                        CLNVI = info.replace('CLNVI=','')
                    if info.startswith('GENEINFO'):
                        GENEINFO = info.replace('GENEINFO=','')
                    if info.startswith('MC'):
                        MC = info.replace('MC=','')
                    if info.startswith('ORIGIN'):
                        ORIGIN = info.replace('ORIGIN=','')
                    if info.startswith('RS'):
                        RS = info.replace('RS=','rs')

                query_nuc_alt = sequence[int(snp_pos) - int(subject_end):int(snp_pos) - int(subject_end) + len(snp_alt)]
                query_nuc_ref = sequence[int(snp_pos) - int(subject_end):int(snp_pos) - int(subject_end) + len(snp_ref)]
                if int(subject_start)-1 <= int(snp_pos) <= int(subject_end)+1 and ChromosomeID in CLNHGVS : ### filter all snp in range of subject
                    # print(snp_chr)
                    # print(snp_pos)
                    # print(snp_name)
                    # print(snp_ref)
                    # print(snp_alt)
                    # print(snp_qual)
                    # print(snp_fil)
                    # print(ALLELEID)
                    # print(CLNDISDB)
                    # print(CLNDN)
                    # print(CLNREVSTAT)
                    # print(CLNSIG)
                    # print(CLNVC)
                    # print(CLNVCSO)
                    # print(CLNVI)
                    # print(GENEINFO)
                    # print(MC)
                    # print(ORIGIN)
                    print(RS)
                    SNPinDetails.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                        snp_chr, snp_name, snp_pos, snp_qual, snp_fil, ALLELEID, CLNDISDB, CLNDN, CLNREVSTAT,
                        CLNSIG, CLNVC, CLNVCSO, CLNVI, GENEINFO, MC, ORIGIN, RS))

                    for record in PharmGKB:
                        record = re.split('\t', record.strip())
                        if RS in record:
                            print(record)
                            variant = record[0]
                            gene = record[1]
                            type = record[2]
                            levelofevidence = record[3]
                            chemicals = record[4]
                            phenotypes = record[5]
                            SNPinDetailsPharmGKB.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(variant,snp_pos, gene, type, levelofevidence, chemicals, phenotypes))


                    for line in AwesomeDB:
                        line = re.split('\t', line.strip())
                        if RS in line:
                            print(line)
                            rsID = line[0]
                            Location = line[1]
                            GeneSymbol = line[2]
                            ENSP = line[3]
                            AAChange = line[4]
                            Phos = line[5]
                            Ubi = line[6]
                            Meth = line[7]
                            SUMO = line[8]
                            OGalNAc = line[9]
                            OGlcNAc = line[10]
                            NGly = line[11]
                            KAce = line[12]
                            NtAce = line[13]
                            ExpScore = line[14]
                            Ref = line[15]
                            Alt = line[16]
                            SNPinDetailsAwesome.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t'
                                                      '%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(rsID, Location, GeneSymbol, ENSP, AAChange, Phos, Ubi,
                                                      Meth, SUMO, OGalNAc, OGlcNAc, NGly, KAce, NtAce, ExpScore, Ref, Alt))
                    print('------------------------------------------------------------')

    except:
        raise
