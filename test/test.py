From mypackage import myModule

def test_top_n():
    """
    make sure top_n works correcly
"""

    assert myModule.top_n([8,3,2,7,4,6,6,7]], 3 == [2,3,4], 'inorrect' )
    assert myModule.top_n([8,3,2,7,4]], 3 == [8,7,4,], 'inorrect' )
    assert myModule.top_n([1,2,3,4,5]], 3 == [8,8,5,6,1], 'inorrect' )