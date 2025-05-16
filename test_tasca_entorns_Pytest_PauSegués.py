# T03-Bloc3-0487 | Entorns | Pau Segués Vitutia

import pytest
from Prova_escrita_05 import llibres_per_categoria, esta_disponible, usuari_te_prestecs, dies_prestec_total

@pytest.fixture
def biblioteca():
    return [
        {
            "llibre": "El Quixot",
            "autor": "Cervantes",
            "categoria": "novel·la",
            "prestecs": [
                {"usuari": "Joan", "dies": 15, "retornat": True},
                {"usuari": "Maria", "dies": 20, "retornat": False},
                {"usuari": "Pere", "dies": 12, "retornat": True}
            ]
        },
        {
            "llibre": "1984",
            "autor": "Orwell",
            "categoria": "ciència-ficció",
            "prestecs": [
                {"usuari": "Pere", "dies": 10, "retornat": True},
                {"usuari": "Anna", "dies": 25, "retornat": True},
                {"usuari": "Marta", "dies": 18, "retornat": False}
            ]
        },
        {
            "llibre": "El Senyor dels Anells",
            "autor": "Tolkien",
            "categoria": "fantasia",
            "prestecs": [
                {"usuari": "Maria", "dies": 30, "retornat": True},
                {"usuari": "Joan", "dies": 22, "retornat": True},
                {"usuari": "Pere", "dies": 15, "retornat": False}
            ]
        },
        {
            "llibre": "Crim i Càstig",
            "autor": "Dostoievski",
            "categoria": "novel·la",
            "prestecs": [
                {"usuari": "Anna", "dies": 28, "retornat": True},
                {"usuari": "Marta", "dies": 14, "retornat": True},
                {"usuari": "Joan", "dies": 21, "retornat": True}
            ]
        }
    ]

# 🔴 Errors intencionats als valors esperats

@pytest.mark.parametrize("categoria, res_esperat", [
    ("novel·la", ["1984"]),                      # Incorrecte expressament
    ("ciència-ficció", ["Crim i Càstig"]),       # Incorrecte
    ("fantasia", ["El Quixot"])                  # Incorrecte
])
def test_llibres_per_categoria(biblioteca, categoria, res_esperat):
    resultat = llibres_per_categoria(biblioteca, categoria)
    assert resultat == res_esperat

@pytest.mark.parametrize("llibre, res_esperat", [
    ("El Senyor dels Anells", True),   # Error: té préstec pendent
    ("1984", True),                    # Error
    ("El Quixot", True),              # Error
    ("Crim i Càstig", False)          # Error: està disponible
])
def test_esta_disponible(biblioteca, llibre, res_esperat):
    resultat = esta_disponible(biblioteca, llibre)
    assert resultat == res_esperat

@pytest.mark.parametrize("usuari, res_esperat", [
    ("Pere", False),    # Error: Pere té préstecs no retornats
    ("Joan", True),     # Error: Joan no té cap préstec pendent
    ("Maria", False),   # Error: Maria sí que té préstec pendent
    ("Anna", True)      # Error: Anna no en té cap pendent
])
def test_usuari_te_prestecs(biblioteca, usuari, res_esperat):
    resultat = usuari_te_prestecs(biblioteca, usuari)
    assert resultat == res_esperat

@pytest.mark.parametrize("llibre, res_esperat", [
    ("El Senyor dels Anells", 10),  # Error: hauria de ser 67
    ("1984", 5),                    # Error: hauria de ser 53
    ("El Quixot", 100),            # Error: hauria de ser 47
    ("Crim i Càstig", 0)           # Error: hauria de ser 63
])
def test_dies_prestec_total(biblioteca, llibre, res_esperat):
    resultat = dies_prestec_total(biblioteca, llibre)
    assert resultat == res_esperat

if __name__ == "__main__":
    pytest.main()
