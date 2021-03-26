import {IProjectLimited} from '@/interfaces/Project';

export interface IAccountingHour {
  id: number;
  user_id: number;
  project_id: number;
  day: string;
  hour_count: number;
  per_hour_cost: number;
  comment?: string;
  created_dt?: Date;
  modified_dt?: Date;
  project: IProjectLimited;
}

export interface IAccountingHourCreateUpdate {
  id?: number;
  user_id: number;
  project_id: number;
  day: string;
  hour_count: number;
  per_hour_cost: number;
  comment?: string;
  created_dt?: Date;
  modified_dt?: Date;
}