import { IProjectWorkerUserInfo } from '@/interfaces'

export interface IUserFeedback {
  rating: number;
  comment: string;
}

export interface IUserFeedbackCreate {
  feedback_received_user_id: number;
  project_worker_id: number;
  rating: number;
  comment: string;
}

export interface IUserFeedbackInfo {
  feedback_received_user_id: number;
  rating: number;
  comment: string;
  project_worker: IProjectWorkerUserInfo
  created_dt: Date;
}