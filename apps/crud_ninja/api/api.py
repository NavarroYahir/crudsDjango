from ninja import Router
from apps.crud_ninja.models import Cosa
from .schemas import CosaIn, CosaOut
from typing import List

router = Router()

@router.get("/cosas", response=List[CosaOut])
def listar_cosas(request):
    return Cosa.objects.all()

@router.get("/cosas/{cosa_id}", response=CosaOut)
def obtener_cosa(request, cosa_id: int):
    return Cosa.objects.get(id=cosa_id)

@router.post("/cosas", response=CosaOut)
def crear_cosa(request, data: CosaIn):
    cosa = Cosa.objects.create(**data.dict())
    return cosa

@router.put("/cosas/{cosa_id}", response=CosaOut)
def actualizar_cosa(request, cosa_id: int, data: CosaIn):
    cosa = Cosa.objects.get(id=cosa_id)
    for attr, value in data.dict().items():
        setattr(cosa, attr, value)
    cosa.save()
    return cosa

@router.delete("/cosas/{cosa_id}")
def eliminar_cosa(request, cosa_id: int):
    cosa = Cosa.objects.get(id=cosa_id)
    cosa.delete()
    return {"success": True}
