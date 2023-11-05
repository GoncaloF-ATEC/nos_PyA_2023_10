from dataclasses import dataclass
import utils as utl

@dataclass
class Contacto:
    nome: str
    telefone: int
    email: str

    def info(self):
        return f"email: {self.email}\ntelefone: {self.telefone}"


    def __str__(self):
        return f"nome: {self.nome}\ntelefone: {self.telefone}"

    def __eq__(self, other):
        return  self.nome == other

class Agenda:

    def __init__(self, nome_agenda: str):
        self.nome = nome_agenda
        self.lista = []

    def info(self, contacto: str = None):

        print(f"{self.nome}")
        if contacto == None:
            utl.showList(self.lista)
        else:
            try:
                ct_index = self.lista.index(contacto)
                ct = self.lista[ct_index]

                print("-" * 10, ct.nome , "-" * 10 )
                print(ct.info())

            except NameError:
                print("a key não existe")
            except ValueError:
                print("o Conacto não esta na lista")
            except:
                print("Erro desconhecido")

    def adicionar_contacto(self, ct: Contacto):

        # if not (contacto is Contacto):
        #    raise TypeError("o parm tem de ser do tipo Contacto")

        if not self.lista.__contains__(ct.nome):
            self.lista.append(ct)
            print("contacto adicionado")
        else:
            print("contacto ja existente")

    def remover_contacto(self, ct: str):
        try:
            #ct_index = self.lista.index(ct)
            #self.lista.pop(ct_index)

            self.lista.remove(ct)
            print("Contacto removido")

        except:
            print("o contacto não existe")

    def editar_contacto(self):
        pass



