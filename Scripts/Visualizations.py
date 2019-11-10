import os

from Scripts.DataVisualization.CompleteScripts.Ready.AnnotatedHeatMap import AnnoHeatMap
from Scripts.DataVisualization.CompleteScripts.Ready.ContourPlotWithSeaborn import CounterPlot
from Scripts.DataVisualization.CompleteScripts.Ready.CustomLinearRegressionFitSeaborn import LinearReg
from Scripts.DataVisualization.CompleteScripts.Ready.CustomLollipopPlot import Lollipop
from Scripts.DataVisualization.CompleteScripts.Ready.DendrogramWithHeatmapAndColouredLeaves import DendoWithHeatMap
from Scripts.DataVisualization.CompleteScripts.Ready.DensityPlotWithMatplotlib import DenistyPlot
from Scripts.DataVisualization.CompleteScripts.Ready.HistogramWithBoxPlot import HistWithBoxPlot
from Scripts.DataVisualization.CompleteScripts.Ready.MarginalPlotWithSeaborn import MarginalPlot
from Scripts.DataVisualization.CompleteScripts.Ready.NumericalSemantics import NumSChem
from Scripts.DataVisualization.CompleteScripts.Ready.ThreeDscatterplot import ThreeDimPlot
from Scripts.DataVisualization.CompleteScripts.Ready.UseNormalizationOnSeabornHeatmap import SeabornHeatMap
from Scripts.DataVisualization.CompleteScripts.Ready.VolcanoLD import VolLD


def visualization(command):
    if command == '-vis':
        AllFiles = os.listdir('./')
        for file in AllFiles:
            if 'rs' in file:
                read = open(file, 'r').read()
                if 'not in 1000G reference panel' in read or os.stat(file).st_size < 500:
                    print(file)
                    os.remove(file)
        for file in AllFiles:
            if 'rs' in file:
                FileName = file
                print(FileName)
                try:
                    CounterPlot("./%s" % file, file.replace('.csv', ''))
                    DenistyPlot('%s' % FileName, file.replace('.csv', ''))
                    DendoWithHeatMap('/home/peter/Desktop/SNPector/LDmatrix.csv')

                except:
                    pass

                SeabornHeatMap('/home/peter/Desktop/SNPector/LDmatrix.csv')

                LinearReg('%s' % FileName, file.replace('.csv', ''))
                Lollipop('%s' % FileName, file.replace('.csv', ''))
                HistWithBoxPlot('%s' % FileName, file.replace('.csv', ''))
                MarginalPlot('%s' % FileName, file.replace('.csv', ''))
                ThreeDimPlot('%s' % FileName, file.replace('.csv', ''))
                AnnoHeatMap('%s' % FileName, file.replace('.csv', ''))
                NumSChem('%s' % FileName, file.replace('.csv', ''))
        VolLD('/home/peter/Desktop/SNPector/LDmatrix.csv')
    elif command == '-off':
        pass