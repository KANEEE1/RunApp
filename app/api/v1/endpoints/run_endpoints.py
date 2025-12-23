# """Run endpoints - Rotas da API para operações de corridas (criar, listar, atualizar, deletar)."""
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List

# from app.core.database import get_db
# from app.schemas.run import RunCreate, RunResponse
# from app.services.run_service import RunService

# router = APIRouter()


# @router.post("/", response_model=RunResponse, status_code=201)
# def create_run(
#     run_data: RunCreate,
#     db: Session = Depends(get_db)
# ):
#     """Cria uma nova corrida."""
#     service = RunService(db)
#     return service.create_run(run_data)


# @router.get("/{run_id}", response_model=RunResponse)
# def get_run(
#     run_id: int,
#     db: Session = Depends(get_db)
# ):
#     """Busca uma corrida por ID."""
#     service = RunService(db)
#     run = service.get_run(run_id)
#     if not run:
#         raise HTTPException(status_code=404, detail="Corrida não encontrada")
#     return run


# @router.get("/", response_model=List[RunResponse])
# def list_runs(
#     skip: int = 0,
#     limit: int = 100,
#     db: Session = Depends(get_db)
# ):
#     """Lista todas as corridas."""
#     service = RunService(db)
#     return service.list_runs(skip=skip, limit=limit)


# @router.delete("/{run_id}", status_code=204)
# def delete_run(
#     run_id: int,
#     db: Session = Depends(get_db)
# ):
#     """Deleta uma corrida."""
#     service = RunService(db)
#     if not service.delete_run(run_id):
#         raise HTTPException(status_code=404, detail="Corrida não encontrada")
