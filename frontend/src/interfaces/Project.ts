import { IWorkerProfile } from './index'

export interface IProject {
  id: number;
  user_id: number;
  name: string;
  address: boolean;
  description: string;
}

export interface IProjectCreate {
  user_id: number;
  name: string;
  address: string;
  description?: string;
  workers: IWorkerProfile[];
}