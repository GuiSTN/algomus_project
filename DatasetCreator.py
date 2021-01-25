# Imports
import os
import music21 as m21
import numpy as np

# Check that there is only one part for every song because it does not seem to be the case

def getLabelsFromStream(stream):
    
    '''Returns the chord labels of each measure of a stream'''
    
    part = stream.parts[0] # Retrieving the first part
    
    # Initializing
    list_labels = []
    flag,count = False,0
    
    # Iterating on the measures
    for measure in part:
        for element in measure:
            if isinstance(element,m21.meter.TimeSignature): # To look only at 4/4 time signatures
                if element.ratioString == '4/4':
                    flag,count = True,count+1
                    list_labels.append([])
                if element.ratioString != '4/4':
                    flag = False
            if isinstance(element,m21.stream.Voice) and flag: # If 4/4 time signature we keep couples of chord labels and measure
                measure_label = [[],measure]
                for note in element:
                    if len(note.lyrics)==1:
                        measure_label[0].append(note.lyrics[0].text)
                    else:
                        measure_label[0].append('') # Empty chord label
                list_labels[count - 1].append(measure_label)
                
    return list_labels

                
def getPairsFromLabels(stream_labeled):
    
    '''Returns the pairs of measures and labels when only one label by measure'''
    
    # Initializing
    labels = []
    
    # Iterating on the pairs
    for part in stream_labeled:
        for i in range(len(part)-1):
            pair = [[],[]]
            
            # Checking that only one label and at the beginning of the measures
            if (len(np.unique(part[i][0])[np.unique(part[i][0])!='']),len(np.unique(part[i+1][0])[np.unique(part[i+1][0])!=''])) == (1,1) and part[i][0][0]!='' and part[i+1][0][0]!='': 
                
                # Creating the pairs
                pair[0].append((np.unique(part[i][0])[np.unique(part[i][0])!=''],part[i][1]))
                pair[1].append((np.unique(part[i+1][0])[np.unique(part[i+1][0])!=''],part[i+1][1]))
                labels.append(pair)
                
    return labels


def getSamplesFromStream(stream):
    
    '''Returns the pairs given a stream'''
    
    labels = getLabelsFromStream(stream)
    return getPairsFromLabels(labels)


def getDataset(files_type='gpif',dir_path=os.getcwd()):
    
    '''Returns the dataset of pairs given the paths of the gpif folder'''
    
    dataset=[] # Initializing
    os.chdir(dir_path) # Looking in the folder
    
    # Iterating on the gpif files to construct the dataset
    for file_name in os.listdir():
        if  file_name[-4:]==files_type:
            parser = ParserGP()
            stream = parser.parseFile(XMLFileName = file_name)
            dataset = dataset + getSamplesFromStream(stream)
            
    return dataset
