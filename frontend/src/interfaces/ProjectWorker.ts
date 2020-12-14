import { IWorkerProfileAdmin, IWorkerProfileAdminUpdate } from '@/interfaces';

export interface IProjectWorker {
  id: number;
  project_id: number;
  user_id: number;
  created_dt: Date;
  modified_dt: Date;
  removed_dt: Date | null;
  worker_accepted_dt: Date | null;
  worker_rejected_dt: Date | null;
  show_project_to_worker: boolean;
  worker: IWorkerProfileAdmin
}

export interface IProjectWorkerUpdate {
  project_id: number;
  user_id: number;
  created_dt?: Date;
  modified_dt?: Date;
  removed_dt: Date | null;
  worker_accepted_dt?: Date | null;
  worker_rejected_dt?: Date | null;
  show_project_to_worker?: boolean;
  worker: IWorkerProfileAdminUpdate
}