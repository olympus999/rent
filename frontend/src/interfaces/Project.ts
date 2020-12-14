import {IWorkerProfile, IProjectWorker, IProjectWorkerUpdate} from './index';

export interface IProject {
  id: number;
  name: string;
  user_id: number;
  address: string;
  description: string;
  created_dt: Date;
  modified_dt: Date;
  project_worker_details: IProjectWorker[]
}

export interface IProjectUpdate {
  name?: string;
  address?: string;
  description?: string;
  project_worker_details?: IProjectWorkerUpdate[]
}

export interface IProjectCreate {
  user_id: number;
  name: string;
  address: string;
  description?: string;
  workers: IWorkerProfile[];
}