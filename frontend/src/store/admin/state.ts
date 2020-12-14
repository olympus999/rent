import {IProject, IUserProfile, IUserRole, IWorkerProfileAdmin} from '@/interfaces';

export interface AdminState {
  // users: {
  //
  // },
  users: IUserProfile[];
  usersRoles: IUserRole[];
  projects: IProject[];
  workers: IWorkerProfileAdmin[];
  workersAvailable: IWorkerProfileAdmin[];
}
