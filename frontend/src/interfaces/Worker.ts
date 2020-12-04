export interface IWorkerProfile {
  id: number;
  first_name: string;
  is_active: boolean;
  role: string;
  available: boolean;
}

export interface IWorkerProfileUpdate {
  id: number;
  available: boolean;
}