
def DrawCircos(command):
    import time
    import os
    import sys
    import re
    import pandas
    import matplotlib
    if not 'DISPLAY' in os.environ:
        matplotlib.use('Agg')  # if DISPLAY is not set
    import pycircos
    import matplotlib.pyplot as plt
    try:
        if command == '-circoson':
            print('Circos Activated')
            time.sleep(2)
            print('Circos Drawing SNP Associations.....')

            Ref_File = open('./RESULTS/FromAwesom.tsv', 'r').readlines()

            for i, record in enumerate(Ref_File):
                file = open('./Pre_Results/For_Circos.txt', 'r').readlines()[1:]

                CNV = pandas.read_table("./Pre_Results/For_Circos.txt")
                CNV['chrom'] = 'chr' + CNV.Chromosome.astype(str)
                CNV = CNV.sort_values(['Chromosome', 'Start'])
                CNV.loc[CNV.Type == 'Del', 'frequency'] *= -1

                AMP = CNV.loc[CNV.Type == 'Amp', :]
                DEL = CNV.loc[CNV.Type == 'Del', :]

                chromsizes = pandas.read_table("./Data/hg19.fa.sizes", index_col=0, header=None, names=['length'])
                cg = pycircos.Circos(chromsizes, gap=2)
                # draw cytoband
                cg.draw_cytobands(8.1, 0.3, "./Data/cytoBand.txt.gz")

                # draw chrom region
                cg.draw_scaffold(8.1, 1.8)
                cg.draw_ticks(8.1, 0.2, inside=True)
                cg.draw_scaffold_ids(9.2, inside=True, fontsize=15)

                # CNV
                cg.draw_scaffold(5.5, 1.1)
                cg.fill_between(5.5, AMP.iloc[:100, :], start='Start', end='End', score='frequency', scale=9.0,
                                facecolor='red',
                                alpha=1)
                cg.fill_between(5.5, DEL.iloc[:100, :], start='Start', end='End', score='frequency', scale=9.0,
                                facecolor='blue',
                                alpha=1)

                # draw links

                Data_File = open('./Data/awesome-all.tsv', 'r').readlines()[1:]
                For_Circos = open('For_Circos.txt', 'w')
                For_Circos.write(
                    'Type	Chromosome	Start	End	-log10(q-value)	G-score	average amplitude	frequency\n')
                forbidden = ['Y', 'X', 'MT']
                For_Circos = open('For_Circos.txt', 'w')
                For_Circos.write(
                    'Type	Chromosome	Start	End	-log10(q-value)	G-score	average amplitude	frequency\n')
                record = re.split('\t', record)
                RS = record[0]
                chr = re.split(':', record[1])
                chrNum = chr[0].replace('chr', '')
                position = chr[1]
                for i, line in enumerate(Data_File):
                    # print('Drawing Circos For SNP: %s'%line[0])
                    line = re.split('\t', line)
                    chromosome = re.split(':', line[1])
                    chromosomeNum = chromosome[0].replace('chr', '')
                    location = chromosome[1]
                    start = int(location)
                    end = int(location)
                    if record[4:] == line[4:] and chromosomeNum not in forbidden:
                        # print(chromosomeNum)
                        For_Circos.write('Amp	 %s	%s	%s	0.744936	0.162607	0.985882	0.258824\n' % (
                        chromosomeNum, start, end))

                for line in file:
                    line = re.split('\t', line.strip())
                    # print(line[1],line[2])
                    cg.draw_link(5.5, ['chr%s' % int(line[1]), 'chr%s' % int(chrNum)], [int(line[2]), int(position)],
                                 [int(line[3]), int(position)], color='Red', alpha=0.03)
                plt.savefig('./RESULTS/Circos(%s)_Fig%s.pdf' % (RS, i))
                # plt.savefig('Circos(%s).png'%RS)
                # plt.savefig('Circos(%s).svg'%RS)
            print("Circos Finished")
        elif command == '-circosoff':
            print("Circos Switched OFF")
    except:
        print('Please, Enter The Circos Option [-circoson] [-circosoff] ')
