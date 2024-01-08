import transposition_code
def test_transposition():
    pass

def test_arranger():
    key="HACK"
    assert transposition_code.arranger(key) == [2,0,1,3]

def test_make_matrix_from_key():
    key="geeks for geeks"
    assert transposition_code.make_matrix_from_key(key,4)==[['g','e','e','k'],['s',' ','f','o'],['r',' ','g','e'],['e','k','s',' ']]

def test_all():
    assert transposition_code.transposition("hack","geeks for geeks")==[['r', ' ', 'g', 'e'], ['g', 'e', 'e', 'k'], ['s', ' ', 'f', 'o'], ['e', 'k', 's', ' ']]
