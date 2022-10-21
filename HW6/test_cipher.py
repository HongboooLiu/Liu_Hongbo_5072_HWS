#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def test_single_word():
    assert cipher("single",3),"Not working"

def test_negative_shift():
    assert cipher("single",-4),"Not working"

def test_symbols():
    assert cipher("si&gle",-4),"Not working"
    
def test_shift_string():
    with pytest.raises(TypeError):
        cipher("single","two")

