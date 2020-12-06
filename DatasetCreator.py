# Imports
import numpy as np
import music21 as m21

def stream_to_annotations(stream):
    part = stream.parts[0]
    list_annotation = []
    flag,count = False,0
    for measure in part:
        for element in measure:
            if isinstance(element,m21.meter.TimeSignature):
                if element.ratioString == '4/4':
                    flag,count = True,count+1
                    list_annotation.append([])
                if element.ratioString != '4/4':
                    flag = False
            if isinstance(element,m21.stream.Voice) and flag:
                measure_annotation = [[],[]]
                for note in element:
                    measure_annotation[1].append(note)
                    if len(note.lyrics)==1:
                        measure_annotation[0].append(note.lyrics[0].text)
                    else:
                        measure_annotation[0].append('')
                list_annotation[count - 1].append(measure_annotation)
    return list_annotation
                
    
def annotation_to_pairs(stream_annotated):
    annotations = []
    for part in stream_annotated:
        for i in range(len(part)-1):
            couple = [[],[]]
            if (len(np.unique(part[i][0])[np.unique(part[i][0])!='']),len(np.unique(part[i+1][0])[np.unique(part[i+1][0])!=''])) == (1,1) and part[i][0][0]!='' and part[i+1][0][0]!='':
                couple[0].append((np.unique(part[i][0])[np.unique(part[i][0])!=''],part[i][1]))
                couple[1].append((np.unique(part[i+1][0])[np.unique(part[i+1][0])!=''],part[i+1][1]))
            annotations.append(couple)
    return annotations
