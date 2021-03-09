import {IWorkerProfile, IWorkerProfileAdmin, IProjectWorker, IProjectWorkerAdminCreateUpdate} from './index';

export interface IProject {
  id: number;
  name: string;
  user_id: number;
  address: string;
  description: string;
  created_dt: Date;
  modified_dt: Date;
  removed_dt: Date | null;
  project_worker: IProjectWorker[]
}

export interface IProjectAdminCreateUpdate {
  id?: number;
  user_id?: number;
  name?: string;
  address?: string;
  description?: string;
  project_worker?: IProjectWorkerAdminCreateUpdate[]
}

export interface IProjectCreate {
  user_id: number;
  name: string;
  address: string;
  description?: string;
  workers: IWorkerProfile[];
}

export interface IProjectForProjectWorker {
  user_id: number;
  name: string;
  address: string;
  description?: string;
  workers: IWorkerProfileAdmin[];
}

export interface IProjectLimited {
  id: number;
  user_id: number;
  name: string;
  address: string;
  description?: string;
}