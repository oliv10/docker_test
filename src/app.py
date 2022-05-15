class app:
    def __init__(self, name: str, age: int, alive: bool = True):
        self.name = name
        self.age = age
        self.alive = alive
    
    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getAlive(self) -> bool:
        return self.alive