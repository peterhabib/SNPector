
from Scripts.DataVisualization.DownloadWithAPI.LDmatrix import LDmatrix
from Scripts.DataVisualization.DownloadWithAPI.LDhap import LDhap
from Scripts.DataVisualization.DownloadWithAPI.LDproxy import LDproxy

def APIcommands(command):
    if command == '-download':
        LDmatrix('./RESULTS/FromNCBI.tsv')
        LDhap('./RESULTS/FromNCBI.tsv')
        LDproxy('./RESULTS/FromNCBI.tsv')
    elif command == '-off':
        pass