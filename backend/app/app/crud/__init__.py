from .crud_user import user
from .crud_user_role import user_role
from .crud_project import project
from .crud_project_worker import project_worker
from .crud_user_feedback import user_feedback
from .crud_tool import tool
from .crud_user_tool import user_tool
from .crud_accounting_balance import accounting_balance
from .crud_accounting_hour import accounting_hour
from .crud_accounting_transaction import accounting_transaction
from .crud_accounting_transaction_type import accounting_transaction_type

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
