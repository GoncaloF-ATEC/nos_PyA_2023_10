from pydantic import  BaseModel


class Contacto(BaseModel):
    nome: str
    telefone: int
    email: str

    def info(self):
        return f"email: {self.email}\ntelefone: {self.telefone}"
