from src import app

def test_getName():
    name = app("Name", 56)
    assert name.getName() == "Name"

def test_getAge():
    age = app("Name", 56)
    assert age.getAge() == 56

def test_getAliveTrue():
    alive = app("Name", 24)
    assert alive.getAlive() == True

def test_getAliveFalse():
    alive = app("Name", 24, alive=False)
    assert alive.getAlive() == False