import { IWorkerProfileAdmin, IWorkerProfileAdminUpdate, IProjectForProjectWorker } from '@/interfaces';
import { IUserFeedback, IProjectLimited } from '@/interfaces'

export interface IProjectWorker {
  id: number;
  project_id: number;
  user_id: number;
  created_dt: Date;
  modified_dt: Date;
  removed_dt: Date | boolean | null;
  worker_accepted_dt: Date | boolean | null;
  worker_rejected_dt: Date | boolean | null;
  show_project_to_worker: boolean;
  worker: IWorkerProfileAdmin
  user_feedback: IUserFeedback
}

export interface IProjectWorkerAdminCreateUpdate {
  id?: number;
  project_id?: number;
  user_id?: number;
  removed_dt: Date | boolean | null
  worker_accepted_dt: Date | boolean | null;
  show_project_to_worker?: boolean;
  worker: IWorkerProfileAdminUpdate
}

export interface IProjectWorkerProject {
  id: number;
  created_dt: Date;
  modified_dt: Date;
  removed_dt: Date | boolean | null;
  worker_accepted_dt: Date | boolean | null;
  worker_rejected_dt: Date | boolean | null;
  show_project_to_worker: boolean;
  project: IProjectForProjectWorker
}

export interface IProjectWorkerUserInfo {
  project: IProjectLimited;
}

export interface IProjectWorkerAssociatedWithProject {
  id: number;
  project: IProjectLimited
}