import { IProjectWorker, IProjectWorkerProject } from './index'

export interface IProjectWorkerActiveProject {
  id: number;
  user_id: 8;
  created_dt: Date;
  project_worker: IProjectWorkerProject
}