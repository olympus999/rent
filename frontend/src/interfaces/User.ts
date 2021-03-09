import {IProjectWorkerActiveProject} from '@/interfaces/ProjectWorkerActive';
import {IUserFeedback} from '@/interfaces/UserFeedback';
import { IUserFeedbackInfo } from '@/interfaces'

export interface IUserProfile {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  is_active: boolean;
  role: string;
  available: boolean;
}

export interface IUserProfileUpdate {
  email?: string;
  first_name?: string;
  last_name?: string;
  password?: string;
  is_active?: boolean;
  role?: string;
  available?: boolean;
}

export interface IUserProfileCreate {
  email: string;
  first_name?: string;
  last_name?: string;
  password?: string;
  is_active?: boolean;
  available?: boolean;
  role?: string;
}

export interface IUserRole {
  id: number;
  name: string;
}

export interface IUserInfo {
  id: number;
  first_name: string;
  last_name: string;
  is_active: boolean;
  role: string;
  available: boolean;
  project_worker_active?: IProjectWorkerActiveProject;
  user_feedback?: IUserFeedbackInfo;
  show_available: boolean;
  average_rating: number;
}