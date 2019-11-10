import sys
import os
def RunBLAST(arg):
    if arg == '-blaston':
        print('BLASTing....Please, Wait')
        os.system('./Scripts/blastn -query GivenSequence.fasta -db ./Data/Hum_Genom38 -outfmt 6  -out ./RESULTS/BLAST_RESULT.txt')
        print('BLAST Finished!')
    elif arg == '-blastoff':
        print('BLAST Switched OFF!, Program Will Use The Previous BLAST Results')

    else:
        print('BLAST Option You Entered Is Not Supported.')
        sys.exit()

    return
