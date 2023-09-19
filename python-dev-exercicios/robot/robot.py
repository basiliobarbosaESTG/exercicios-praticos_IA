class Robot:
    # inicializa o atributo nome e define o atributo state como "inactive"
    def __init__(self, nome):
        self.nome = nome
        self.state = "inactive"

    # define o estado como ativo
    def activate(self):
        self.state = "active"

    # define o estado como inativo
    def deactivate(self):
        self.state = "inactive"

    # retorna True se o atributo estado for "ativo" e False caso contrário.
    def Is_active(self):
        return self.state == "active"


# Instancia objeto Robot
r2d2 = Robot("R2D2")
r2d2.activate()
print(r2d2.Is_active())  # True
r2d2.deactivate()
print(r2d2.Is_active())  # False


class SuperRobot(Robot):
    def __init__(self, nome):
        super().__init__(nome)
        self.speed = 0  # atributo speed

    # aumenta a velocidade do robo em determinada quantidade
    def increase_speed(self, quantity):
        self.speed += quantity


# Instancia objeto SuperRobot
sr = SuperRobot("SuperR2D2")
sr.activate()
print(sr.Is_active())  # True
sr.increase_speed(10)
print(sr.speed)  # 10
sr.deactivate()
print(sr.Is_active())  # False

print(r2d2.nome, r2d2.state)
print(sr.nome, sr.state)
sr.increase_speed(1)  # speed = 11
print(sr.nome, sr.state, sr.speed)
