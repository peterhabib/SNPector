from DataVisualization.DownloadWithAPI.LDmatrix import LDmatrix
from DataVisualization.DownloadWithAPI.LDhap import LDhap
from DataVisualization.DownloadWithAPI.LDproxy import LDproxy
from DataVisualization.CompleteScripts.Ready.ContourPlotWithSeaborn import CounterPlot
from DataVisualization.CompleteScripts.Ready.CustomLinearRegressionFitSeaborn import LinearReg
from DataVisualization.CompleteScripts.Ready.CustomLollipopPlot import Lollipop
from DataVisualization.CompleteScripts.Ready.DendrogramWithHeatmapAndColouredLeaves import DendoWithHeatMap
from DataVisualization.CompleteScripts.Ready.DensityPlotWithMatplotlib import DenistyPlot
from DataVisualization.CompleteScripts.Ready.HistogramWithBoxPlot import HistWithBoxPlot
from DataVisualization.CompleteScripts.Ready.MarginalPlotWithSeaborn import MarginalPlot
from DataVisualization.CompleteScripts.Ready.ThreeDscatterplot import ThreeDimPlot
from DataVisualization.CompleteScripts.Ready.UseNormalizationOnSeabornHeatmap import SeabornHeatMap
from DataVisualization.CompleteScripts.Ready.AnnotatedHeatMap import AnnoHeatMap
from DataVisualization.CompleteScripts.Ready.NumericalSemantics import NumSChem
from DataVisualization.CompleteScripts.Ready.ThreeDscatterplot import ThreeDimPlot
from DataVisualization.CompleteScripts.Ready.VolcanoLD import VolLD



def RunLinDisVis():
    LDmatrix('/home/peter/Desktop/SNPector/RESULTS/FromNCBI.tsv')
    LDhap('/home/peter/Desktop/SNPector/RESULTS/FromNCBI.tsv')
    LDproxy('/home/peter/Desktop/SNPector/RESULTS/FromNCBI.tsv')
    # CounterPlot('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # LinearReg('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # Lollipop('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # DendoWithHeatMap('/home/peter/Desktop/DataVisualization/CompleteScripts/LDmatrix100.csv')
    # DenistyPlot('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # HistWithBoxPlot('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # MarginalPlot('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # ThreeDimPlot('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # SeabornHeatMap('/home/peter/Desktop/DataVisualization/CompleteScripts/LDmatrix100.csv')
    # AnnoHeatMap('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # NumSChem('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # ThreeDimPlot('/home/peter/Desktop/SNPector/Scripts/DataVisualization/CompleteScripts/rs516316.csv')
    # VolLD('/home/peter/Desktop/DataVisualization/CompleteScripts/LDmatrix100.csv')




RunLinDisVis()






