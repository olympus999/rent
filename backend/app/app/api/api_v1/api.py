from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, user_roles, workers, projects

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(workers.router, prefix="/workers", tags=["workers"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(user_roles.router, prefix="/user_roles", tags=["user_roles"])
