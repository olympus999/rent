import { IProjectWorkerActiveProject, IUserFeedback } from './index';

export interface IWorkerProfile {
  id: number;
  first_name: string;
  is_active: boolean;
  role: string;
  available: boolean;
}

export interface IWorkerProfileUpdate {
  id: number;
  available?: boolean;
}

export interface IWorkerProfileAdmin {
  id: number;
  first_name: string;
  last_name: string;
  is_active: boolean;
  role: string;
  available: boolean;
}

export interface IWorkerProfileProjectAdmin {
  id: number;
  first_name: string;
  last_name: string;
  is_active: boolean;
  role: string;
  available: boolean;
  project_worker_active?: IProjectWorkerActiveProject
  user_feedback?: IUserFeedback
  show_available: boolean
}

export interface IWorkerProfileAdminUpdate {
  id: number;
}