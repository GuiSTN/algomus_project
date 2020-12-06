# imports
import numpy as np
import music21 as m21

def measures_to_annotations(stream):
    part = stream.parts[0]
    list_annotation = []
    flag,count = False,0
    for a in part:
        for b in a:
            if isinstance(b,m21.meter.TimeSignature):
                print(b.ratioString)
                if b.ratioString == '4/4':
                    flag,count = True,count+1
                    list_annotation.append([])
                if b.ratioString != '4/4':
                    flag = False
            if isinstance(b,m21.stream.Voice) and flag:
                measure_annotation = []
                for c in b:
                    if len(c.lyrics)==1:
                        measure_annotation.append(c.lyrics[0].text)
                    else:
                        measure_annotation.append('')
                list_annotation[count - 1].append(measure_annotation)
    return list_annotation
                
    
def annotation_to_pairs():
    couple_annotation =[]
    for part in list_annotation:
        annotations = []
        for i in range(len(part)-1):
            # VERIFIER QUE LANNOTATiON EST AU DEBUT
            if (len(np.unique(part[i])[np.unique(part[i])!='']),len(np.unique(part[i+1])[np.unique(part[i+1])!=''])) == (1,1) and np.unique(part[i])!='' and np.unique(part[i+1])!='':
                annotations.append((np.unique(part[i])[np.unique(part[i])!=''],np.unique(part[i+1])[np.unique(part[i+1])!='']))
        couple_annotation.append(annotations)
    return couple_annotation
