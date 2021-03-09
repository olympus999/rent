from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils, user_roles, workers, \
    projects, google_maps, clients, user_feedback, tools, user_tool, \
    accounting_transaction, accounting_hour, accounting_balance, \
    project_worker

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(workers.router, prefix="/workers", tags=["workers"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(user_roles.router, prefix="/user_roles", tags=["user_roles"])
api_router.include_router(google_maps.router, prefix="/google_maps", tags=["google_maps"])
api_router.include_router(user_feedback.router, prefix="/user_feedback", tags=["user_feedback"])
api_router.include_router(tools.router, prefix="/tools", tags=["tools"])
api_router.include_router(user_tool.router, prefix="/user_tools", tags=["user_tools"])
api_router.include_router(accounting_transaction.router, prefix="/accounting_transaction", tags=["accounting_transaction"])
api_router.include_router(accounting_hour.router, prefix="/accounting_hour", tags=["accounting_hour"])
api_router.include_router(accounting_balance.router, prefix="/accounting_balance", tags=["accounting_balance"])
api_router.include_router(project_worker.router, prefix="/project_worker", tags=["project_worker"])
