from ninja import Schema

class CosaIn(Schema):
    nombre: str
    descripcion: str

class CosaOut(Schema):
    id: int
    nombre: str
    descripcion: str
