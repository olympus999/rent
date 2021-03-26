import {
  IProject, ITool,
  IUserInfo,
  IUserProfile,
  IUserRole, IUserTool,
  IWorkerProfileAdmin,
  IWorkerProfileProjectAdmin,
  IProjectWorkerAssociatedWithProject, IAccountingHour, IAccountingTransactionType, IAccountingBalance
} from '@/interfaces';
import {IAccountingTransaction} from '@/interfaces/AccountingTransaction';

export interface AdminState {
  users: {
    users: IUserProfile[];
    clients: IUserProfile[];
    workers: IWorkerProfileProjectAdmin[];
    workersAvailable: IWorkerProfileAdmin[];
    userInfo: IUserInfo;
    userTools: IUserTool[];
    accountingHours: IAccountingHour[];
    accountingTransactions: IAccountingTransaction[];
    accountingTransactionTypes: IAccountingTransactionType[];
    accountingBalance: IAccountingBalance;
  },
  tools: ITool[];
  usersRoles: IUserRole[];
  projects: IProject[];
  projectWorkersAssociatedWithUser: IProjectWorkerAssociatedWithProject[];
  removedProjects: IProject[];
}
