from fastapi import APIRouter
from typing import Optional
from lib.geometries import Geometry
from typing import List
from datetime import date

router = APIRouter()
geometry = Geometry()

#Get wkb geometries for earch postal code
@router.get("/geometries/total",)
async def get_total():

    return geometry.get_wkb_geometry()