#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
@pytest.fixture
def subject():
    return ["single","single word test","SINGLE","Test"]

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
def test_word(subject):
    for i in subject:
        assert cipher(i,shift=2)
def test_negative_shift(subject):
    for i in subject:
        assert cipher(i,-4),"Not working"
def test_symbols():
    assert cipher("si&gle",2),"Not working"

