# Imports
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import music21 as m21


class ChenEncoder(Encoder):
   
    def _init_(self,tuning,numFret,numString):
        '''Initiating the encoder'''
        super().__init__(tuning,numFret,numString)
        
    def getTokensFromMeasure(self,measure):
        '''Returns a measure translated in tokens as Chen proposes'''
        measure_lemmas = ['bar']
        for note in measure.flat:
            if isinstance(note, m21.chord.Chord):
                for a in note:
                    measure_lemmas = measure_lemmas + ['position_'+str(int((0.25+note.offset)*4))+'/16','Note_on('+str(a.pitch.midi)+')','Note_duration('+str(int(note.duration.quarterLength*4))+')','String('+str(a.articulations[0].number)+')','Fret('+str(a.articulations[1].number)+')']
            elif isinstance(note, m21.note.Note):
                measure_lemmas = measure_lemmas + ['position_'+str(int((0.25+note.offset)*4))+'/16','Note_on('+str(note.pitch.midi)+')','Note_duration('+str(int(note.duration.quarterLength*4))+')','String('+str(note.articulations[0].number)+')','Fret('+str(note.articulations[1].number)+')']
            else:
                pass
        return np.reshape(np.array(measure_lemmas),newshape=(len(measure_lemmas),1))

    def getOneHotFromTokens(self,tokens):
        '''Returns the tokens encoded as one-hot vectors'''
        # vocabulary of 140 categories
        vocabulary = ['bar', 'position_1/16', 'position_2/16', 'position_3/16', 'position_4/16', 'position_5/16', 'position_6/16', 'position_7/16', 'position_8/16', 'position_9/16', 'position_10/16', 'position_11/16', 'position_12/16', 'position_13/16', 'position_14/16', 'position_15/16', 'position_16/16', 'Note_on(21)','Note_on(22)','Note_on(23)','Note_on(24)','Note_on(25)','Note_on(26)','Note_on(27)','Note_on(28)','Note_on(29)','Note_on(30)','Note_on(31)','Note_on(32)','Note_on(33)','Note_on(34)','Note_on(35)','Note_on(36)','Note_on(37)','Note_on(38)','Note_on(39)','Note_on(40)','Note_on(41)','Note_on(42)','Note_on(43)','Note_on(44)','Note_on(45)','Note_on(46)','Note_on(47)','Note_on(48)','Note_on(49)','Note_on(50)','Note_on(51)','Note_on(52)','Note_on(53)','Note_on(54)','Note_on(55)','Note_on(56)','Note_on(57)','Note_on(58)','Note_on(59)','Note_on(60)','Note_on(61)','Note_on(62)','Note_on(63)','Note_on(64)','Note_on(65)','Note_on(66)','Note_on(67)','Note_on(68)','Note_on(69)','Note_on(70)','Note_on(71)','Note_on(72)','Note_on(73)','Note_on(74)','Note_on(75)','Note_on(76)','Note_on(77)','Note_on(78)','Note_on(79)','Note_on(80)','Note_on(81)','Note_on(82)','Note_on(83)','Note_on(84)','Note_on(85)','Note_on(86)','Note_on(87)','Note_on(88)','Note_on(89)','Note_on(90)','Note_on(91)','Note_on(92)','Note_on(93)','Note_on(94)','Note_on(95)','Note_on(96)','Note_on(97)','Note_on(98)','Note_on(99)','Note_on(100)','Note_on(101)','Note_on(102)','Note_on(103)','Note_on(104)','Note_on(105)','Note_on(106)','Note_on(107)','Note_on(108)', 'String(0)', 'String(1)', 'String(2)', 'String(3)', 'String(4)', 'String(5)', 'String(6)', 'Fret(0)', 'Fret(1)', 'Fret(2)', 'Fret(3)', 'Fret(4)', 'Fret(5)', 'Fret(6)', 'Fret(7)', 'Fret(8)', 'Fret(9)', 'Fret(10)', 'Fret(11)', 'Fret(12)', 'Fret(13)', 'Fret(14)', 'Fret(15)', 'Fret(16)', 'Fret(17)', 'Fret(18)', 'Fret(19)', 'Fret(20)', 'Fret(21)', 'Fret(22)', 'Fret(23)', 'Fret(24)', 'Note_duration(1)', 'Note_duration(2)', 'Note_duration(3)', 'Note_duration(4)', 'Note_duration(5)', 'Note_duration(6)', 'Note_duration(7)', 'Note_duration(8)', 'Note_duration(9)', 'Note_duration(10)', 'Note_duration(11)', 'Note_duration(12)', 'Note_duration(13)', 'Note_duration(14)', 'Note_duration(15)', 'Note_duration(16)', 'Note_duration(17)', 'Note_duration(18)', 'Note_duration(19)', 'Note_duration(20)', 'Note_duration(21)', 'Note_duration(22)', 'Note_duration(23)', 'Note_duration(24)', 'Note_duration(25)', 'Note_duration(26)', 'Note_duration(27)', 'Note_duration(28)', 'Note_duration(29)', 'Note_duration(30)', 'Note_duration(31)', 'Note_duration(32)', 'Note_duration(33)', 'Note_duration(34)', 'Note_duration(35)', 'Note_duration(36)', 'Note_duration(37)', 'Note_duration(38)', 'Note_duration(39)', 'Note_duration(40)', 'Note_duration(41)', 'Note_duration(42)', 'Note_duration(43)', 'Note_duration(44)', 'Note_duration(45)', 'Note_duration(46)', 'Note_duration(47)', 'Note_duration(48)', 'Note_duration(49)', 'Note_duration(50)', 'Note_duration(51)', 'Note_duration(52)', 'Note_duration(53)', 'Note_duration(54)', 'Note_duration(55)', 'Note_duration(56)', 'Note_duration(57)', 'Note_duration(58)', 'Note_duration(59)', 'Note_duration(60)', 'Note_duration(61)', 'Note_duration(62)', 'Note_duration(63)', 'Note_duration(64)']
        vocabulary = np.reshape(vocabulary,newshape=(len(vocabulary),1))

        # Fitting the one hot encoder to the vocabulary
        one_hot_encoder = OneHotEncoder()
        one_hot_encoder.fit(vocabulary)

        # Encoding the score
        list_onehot = one_hot_encoder.transform(tokens).toarray()

        return list_onehot

    def getOneHotFromMeasure(self,measure):
        '''Returns the measure as one-hot vectors'''
        return self.getOneHotFromTokens(self.getTokensFromMeasure(measure))
    
    def getOneHotFromStream(self,stream):
        '''Returns the stream as a list one-hot vectors'''
        part = stream.parts[0]
        return [self.getOneHotFromMeasure(measure) for measure in part]
