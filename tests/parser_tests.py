from nose.tools import raises, eq_
from ex48.parser import *

def test_sentence():
    exSentence = Sentence(('noun', 'subj'), ('verb', 'verb'), ('noun','obj'))
    eq_(exSentence.subject, 'subj')
    eq_(exSentence.verb, 'verb')
    eq_(exSentence.object, 'obj')
    
def test_peek():
    word_list = None
    peek(word_list)
    eq_(exSentence.verb, 'verb')
    eq_(exSentence.object, 'obj')