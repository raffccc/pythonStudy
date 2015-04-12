from nose.tools import raises, eq_
from ex48.parser import *

def test_sentence():
    exSentence = Sentence(('noun', 'subj'), ('verb', 'verb'), ('noun','obj'))
    eq_(exSentence.subject, 'subj')
    eq_(exSentence.verb, 'verb')
    eq_(exSentence.object, 'obj')
    
def test_peek():
    word_list = [ ('verb', 'eat'), ('noun', 'spinach'), ('noun', 'brisa')]
    eq_(peek(word_list), 'verb')
    
    word_list = [ ('verb', 'eat'), ('noun', 'spinach'), ('noun', 'brisa')]
    eq_(peek(word_list), 'verb')
    
    word_list = None
    eq_(peek(word_list), None)
    
    word_list = []
    eq_(peek(word_list), None)
    
def test_match():
    word_list = [ ('verb', 'eat'), ('noun', 'spinach'), ('noun', 'brisa')]
    eq_(match(word_list, 'verb'), ('verb', 'eat'))
    eq_(match(word_list, 'verb'), None)
    
    eq_(match(word_list, 'noun'), ('noun', 'brisa'))
    eq_(match(word_list, 'verb'), None)
    
    eq_(match(None, 'noun'), None)

def test_skip():
    word_list = [ ('stop', 'to'), ('stop', 'in'), ('noun', 'brisa')]
    skip(word_list, 'stop')
    
    eq_(peek(word_list), 'noun')

@raises(ParserError)
def test_parse_verb():
    word_list = [ ('verb', 'eat'), ('noun', 'spinach'), ('noun', 'brisa')]
    eq_(parse_verb(word_list), ('verb', 'eat'))
    
    word_list = [ ('stop', 'in'), ('stop', 'the'), ('verb', 'eat')]
    eq_(parse_verb(word_list), ('verb', 'eat'))
    
    parse_verb(word_list)
    
@raises(ParserError)
def test_parse_object():
    word_list = [ ('noun', 'rafael'), ('direction', 'north'), ('verb', 'eats')]
    eq_(parse_object(word_list), ('noun', 'rafael'))
    eq_(parse_object(word_list), ('direction', 'north'))
    
    word_list = [ ('stop', 'in'), ('stop', 'the'), ('noun', 'rafael')]
    eq_(parse_object(word_list), ('noun', 'rafael'))
    
    parse_object(word_list)
    
@raises(ParserError)
def test_parse_subject():
    word_list = [ ('noun', 'rafael'), ('verb', 'does'), ('verb', 'eats')]
    eq_(parse_subject(word_list), ('noun', 'rafael'))
    eq_(parse_subject(word_list), ('noun', 'player'))
    eq_(parse_subject(word_list), ('noun', 'player'))
    
    word_list = [ ('stop', 'in'), ('stop', 'the'), ('noun', 'rafael')]
    eq_(parse_subject(word_list), ('noun', 'rafael'))
    
    parse_subject(word_list)
 
def test_parse_sentence():
    exSentence = parse_sentence( [('noun', 'subj'), ('verb', 'verb'), ('noun','obj')] )
    eq_(exSentence.subject, 'subj')
    eq_(exSentence.verb, 'verb')
    eq_(exSentence.object, 'obj')
        