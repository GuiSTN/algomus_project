# imports
import numpy as np
import music21 as m21

def measure_to_lemmas(measure):
    measure_lemmas = ['bar']
    for note in measure.flat:
        if isinstance(note, m21.chord.Chord):
            for a in note:
                measure_lemmas = measure_lemmas + ['position_'+str(int((0.25+note.offset)*4))+'/16','Note_on('+a.nameWithOctave+')','Note_duration('+str(int(note.duration.quarterLength*4))+')','String('+str(a.articulations[0].number)+')','Fret('+str(a.articulations[1].number)+')']
        else:
            pass
    return np.reshape(np.array(measure_lemmas),newshape=(len(measure_lemmas),1))

def lemmas_to_onehot(measure_lemmas):
    
    # vocabulary of 140 categories
    vocabulary = ['bar', 'position_1/16', 'position_2/16', 'position_3/16', 'position_4/16', 'position_5/16', 'position_6/16', 'position_7/16', 'position_8/16', 'position_9/16', 'position_10/16', 'position_11/16', 'position_12/16', 'position_13/16', 'position_14/16', 'position_15/16', 'position_16/16', 'Note_on(E2)', 'Note_on(F2)', 'Note_on(G2)', 'Note_on(A2)', 'Note_on(B2)', 'Note_on(C3)', 'Note_on(D3)', 'Note_on(E3)', 'Note_on(F3)', 'Note_on(G3)', 'Note_on(A3)', 'Note_on(B3)', 'Note_on(C4)', 'Note_on(D4)', 'Note_on(E4)', 'Note_on(F4)', 'Note_on(G4)', 'Note_on(A4)', 'Note_on(B4)', 'Note_on(C5)', 'Note_on(D5)', 'Note_on(E5)', 'Note_on(F5)', 'Note_on(G5)', 'Note_on(A5)', 'Note_on(B5)', 'Note_on(C6)', 'String(0)', 'String(1)', 'String(2)', 'String(3)', 'String(4)', 'String(5)', 'String(6)', 'Fret(0)', 'Fret(1)', 'Fret(2)', 'Fret(3)', 'Fret(4)', 'Fret(5)', 'Fret(6)', 'Fret(7)', 'Fret(8)', 'Fret(9)', 'Fret(10)', 'Fret(11)', 'Fret(12)', 'Fret(13)', 'Fret(14)', 'Fret(15)', 'Fret(16)', 'Fret(17)', 'Fret(18)', 'Fret(19)', 'Fret(20)', 'Fret(21)', 'Fret(22)', 'Fret(23)', 'Fret(24)', 'Note_duration(1)', 'Note_duration(2)', 'Note_duration(3)', 'Note_duration(4)', 'Note_duration(5)', 'Note_duration(6)', 'Note_duration(7)', 'Note_duration(8)', 'Note_duration(9)', 'Note_duration(10)', 'Note_duration(11)', 'Note_duration(12)', 'Note_duration(13)', 'Note_duration(14)', 'Note_duration(15)', 'Note_duration(16)', 'Note_duration(17)', 'Note_duration(18)', 'Note_duration(19)', 'Note_duration(20)', 'Note_duration(21)', 'Note_duration(22)', 'Note_duration(23)', 'Note_duration(24)', 'Note_duration(25)', 'Note_duration(26)', 'Note_duration(27)', 'Note_duration(28)', 'Note_duration(29)', 'Note_duration(30)', 'Note_duration(31)', 'Note_duration(32)', 'Note_duration(33)', 'Note_duration(34)', 'Note_duration(35)', 'Note_duration(36)', 'Note_duration(37)', 'Note_duration(38)', 'Note_duration(39)', 'Note_duration(40)', 'Note_duration(41)', 'Note_duration(42)', 'Note_duration(43)', 'Note_duration(44)', 'Note_duration(45)', 'Note_duration(46)', 'Note_duration(47)', 'Note_duration(48)', 'Note_duration(49)', 'Note_duration(50)', 'Note_duration(51)', 'Note_duration(52)', 'Note_duration(53)', 'Note_duration(54)', 'Note_duration(55)', 'Note_duration(56)', 'Note_duration(57)', 'Note_duration(58)', 'Note_duration(59)', 'Note_duration(60)', 'Note_duration(61)', 'Note_duration(62)', 'Note_duration(63)', 'Note_duration(64)']
    vocabulary = np.reshape(vocabulary,newshape=(len(vocabulary),1))
    
    # Fitting the one hot encoder to the vocabulary
    one_hot_encoder = OneHotEncoder()
    one_hot_encoder.fit(vocabulary)
    
    # Encoding the score
    list_onehot = one_hot_encoder.transform(measure_lemmas).toarray()
    
    return list_onehot

def measure_to_onehot(measure):
    return lemmas_to_onehot(measure_to_lemmas(measure))
