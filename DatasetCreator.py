# Imports
import numpy as np
import music21 as m21
import os

# Check that there is only one part for every song because it does not seem to be the case
# Do we unzip before or we unzip in python ?

def stream_to_labels(stream):
    part = stream.parts[0]
    list_labels = []
    flag,count = False,0
    for measure in part:
        for element in measure:
            if isinstance(element,m21.meter.TimeSignature):
                if element.ratioString == '4/4':
                    flag,count = True,count+1
                    list_labels.append([])
                if element.ratioString != '4/4':
                    flag = False
            if isinstance(element,m21.stream.Voice) and flag:
                measure_annotation = [[],measure]
                for note in element:
                    if len(note.lyrics)==1:
                        measure_annotation[0].append(note.lyrics[0].text)
                    else:
                        measure_annotation[0].append('')
                list_labels[count - 1].append(measure_annotation)
    return list_labels
                
def labels_to_pairs(stream_labeled):
    labels = []
    for part in stream_labeled:
        for i in range(len(part)-1):
            couple = [[],[]]
            if (len(np.unique(part[i][0])[np.unique(part[i][0])!='']),len(np.unique(part[i+1][0])[np.unique(part[i+1][0])!=''])) == (1,1) and part[i][0][0]!='' and part[i+1][0][0]!='':
                couple[0].append((np.unique(part[i][0])[np.unique(part[i][0])!=''],part[i][1]))
                couple[1].append((np.unique(part[i+1][0])[np.unique(part[i+1][0])!=''],part[i+1][1]))
            labels.append(couple)
    return labels

def getSamplesFromStream(stream):
    labels = stream_to_labels(stream)
    return labels_to_pairs(labels)

def getDataset(files_type=['gp','gpif'],dir_path=os.getcwd()):
    dataset=[0,0,0]
    parser = ParserGP()
    os.chdir(dir_path)
    i=0
    for file_name in os.listdir():
        if  file_name[-4:]=='gpif':
            stream = parser.parseFile(XMLFileName = file_name)
            dataset[i] = getSamplesFromStream(stream)
            i+=1
    os.chdir(os.getcwd())
    return dataset
