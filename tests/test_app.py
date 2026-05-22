import pytest
from src.app import somar, dividir

def test_somar():
    assert somar(2, 3) == 5

#def test_dividir():
   # assert dividir(10, 2) == 5.0
    # Propositalmente sem testar divisão por zero

def test_dividir_por_zero():
    with pytest.raises(ValueError): # type: ignore
        dividir(10, 0)