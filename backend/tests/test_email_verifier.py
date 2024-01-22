def verificar_email(email):
    # Lógica para verificar se o email é válido
    if "@" in email and "." in email:
        return True
    else:
        return False
    
def test_verificar_email_valido():
    assert verificar_email("usuario@example.com") == True

def test_verificar_email_invalido():
    assert verificar_email("usuario@invalido") == False

def test_verificar_email_sem_arroba():
    assert verificar_email("usuarioexample.com") == False

def test_verificar_email_sem_ponto():
    assert verificar_email("usuario@examplecom") == False