from Agenda import *
#a = Agenda("Agenda")

#import Agenda
#a = Agenda.Agenda("Agenda")

import Agenda as ag

a = ag.Agenda("Agenda")

a.info()

a.nome = "Novo nome"

a.info()

#a.adicionar_contacto("Joao")

a.info()

print(a)


ct = ag.Contacto("Gonçalo", 23232434, "email@nos.pt")

print(ct)

a.adicionar_contacto(ct)

a.info()

print(ct.__eq__("Gonçalo"))

print("---------------")
a.info("Gonçalo")

print("---------------")
print("---------------")
a.adicionar_contacto(ct)
print("---------------")
print("---------------")
print("---------------")
a.remover_contacto("Gonçalo")
a.info("Gonçalo")