import os
import time
import re
from operator import itemgetter
import sys
import glob

from Scripts.Circos import DrawCircos
from Scripts.Network import DrawNetwork
from Scripts.Run_BLAST import RunBLAST
from Scripts.Extraction import ExtractSNP
from Scripts.APIcommands import APIcommands
from Scripts.Visualizations import visualization
from Scripts.DataVisualization.DownloadWithAPI.LDmatrix import LDmatrix
from Scripts.DataVisualization.DownloadWithAPI.LDhap import LDhap
from Scripts.DataVisualization.DownloadWithAPI.LDproxy import LDproxy
from Scripts.DataVisualization.CompleteScripts.Ready.ContourPlotWithSeaborn import CounterPlot
from Scripts.DataVisualization.CompleteScripts.Ready.CustomLinearRegressionFitSeaborn import LinearReg
from Scripts.DataVisualization.CompleteScripts.Ready.CustomLollipopPlot import Lollipop
from Scripts.DataVisualization.CompleteScripts.Ready.DendrogramWithHeatmapAndColouredLeaves import DendoWithHeatMap
from Scripts.DataVisualization.CompleteScripts.Ready.DensityPlotWithMatplotlib import DenistyPlot
from Scripts.DataVisualization.CompleteScripts.Ready.HistogramWithBoxPlot import HistWithBoxPlot
from Scripts.DataVisualization.CompleteScripts.Ready.MarginalPlotWithSeaborn import MarginalPlot
from Scripts.DataVisualization.CompleteScripts.Ready.ThreeDscatterplot import ThreeDimPlot
from Scripts.DataVisualization.CompleteScripts.Ready.UseNormalizationOnSeabornHeatmap import SeabornHeatMap
from Scripts.DataVisualization.CompleteScripts.Ready.AnnotatedHeatMap import AnnoHeatMap
from Scripts.DataVisualization.CompleteScripts.Ready.NumericalSemantics import NumSChem
from Scripts.DataVisualization.CompleteScripts.Ready.ThreeDscatterplot import ThreeDimPlot
from Scripts.DataVisualization.CompleteScripts.Ready.VolcanoLD import VolLD


file_name = sys.argv[7]

PharmGKB = open('./Data/clinicalVariants.tsv', 'r').readlines()
BLAST_RESULT = open('./RESULTS/BLAST_RESULT.txt','w')
AwesomeDB = open('./Data/awesome-all.tsv').readlines()
NCBIclinVar=open('./Data/clinvar_20191001.vcf','r').readlines()[28:]
SNPinDetails = open('./RESULTS/FromNCBI.tsv','w')
SNPinDetailsPharmGKB = open('./RESULTS/FromPharmGKB.tsv','w')
SNPinDetailsAwesome = open('./RESULTS/FromAwesom.tsv','w')
BLASTfile=open('./RESULTS/BLAST_RESULT.txt','r').readlines()
SeqFile=open(file_name,'r').readlines()
SNPinDetails.write('Chromosome\tSNP_Name\tPosition\tQuality\tFilter\tALLELEID\tCLNDISDB\tCLNDN\tCLNREVSTAT\tCLNSIG\tCLNVC\tCLNVCSO\tCLNVI\tGENEINFO\tMC\tORIGIN\tRS\n')




print("*****Welcome In SNPector Software*****")




RunBLAST(sys.argv[1])
ExtractSNP(sys.argv[2], NCBIclinVar, BLASTfile, SeqFile, SNPinDetails, PharmGKB, SNPinDetailsPharmGKB, AwesomeDB, SNPinDetailsAwesome)
SNPinDetails.close()
SNPinDetailsPharmGKB.close()
SNPinDetailsAwesome.close()
DrawCircos(sys.argv[3])
DrawNetwork(sys.argv[4])

APIcommands(sys.argv[5])
visualization(sys.argv[6])






