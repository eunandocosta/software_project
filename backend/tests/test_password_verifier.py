def verifica_senha(senha):
    if len(senha)>=6 and any(x.isupper() for x in senha) and any(x.islower() for x in senha) and any(x.isdigit() for x in senha):
        return True
    else:
        return False
    
def test_verifica_senha_positivo():
    assert verifica_senha("1234XreBd") == True

def test_verifica_senha_num():
    assert verifica_senha("123cD") == False

def test_verifica_no_dig():
    assert verifica_senha("12345678") == False

def test_verifica_no_dig_up():
    assert verifica_senha("123456fdfe") == False

def test_verifica_no_dig_low():
    assert verifica_senha("123456XFDRE") == False