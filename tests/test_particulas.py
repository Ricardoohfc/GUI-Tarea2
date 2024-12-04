#Importar la clase Particula
from Modelo_Estandar.particulas import Particula

def test_crear_particula():
    #Crear una partícula de prueba
    electron = Particula("Electrón", "lepton", -1, 0.51099895000)

    #Verificar los atributos de la partícula
    assert electron.nombre == "Electrón"
    assert electron.tipo == "lepton"
    assert electron.carga == -1
    assert electron.masa == 0.51099895000

def test_mostrar_info():
    #Crear una partícula de prueba
    gluon = Particula("Gluón", "boson", 0, 0, "red/anti-red", None)

    #Verificar el formato de la información
    info = gluon.mostrar_info()
    assert "Partícula: Gluón" in info
    assert "Tipo: boson" in info
    assert "Carga: 0 e" in info
    assert "Masa: 0 MeV/c^2" in info
    assert "Carga de color: red/anti-red" in info
