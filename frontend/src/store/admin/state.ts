import {
  IProject, ITool,
  IUserInfo,
  IUserProfile,
  IUserRole, IUserTool,
  IWorkerProfileAdmin,
  IWorkerProfileProjectAdmin,
  IProjectWorkerAssociatedWithProject, IAccountingHour
} from '@/interfaces';

export interface AdminState {
  users: {
    users: IUserProfile[];
    clients: IUserProfile[];
    workers: IWorkerProfileProjectAdmin[];
    workersAvailable: IWorkerProfileAdmin[];
    userInfo: IUserInfo;
    userTools: IUserTool[];
    accountingHours: IAccountingHour[];
  },
  tools: ITool[];
  usersRoles: IUserRole[];
  projects: IProject[];
  projectWorkersAssociatedWithUser: IProjectWorkerAssociatedWithProject[];
  removedProjects: IProject[];
}
