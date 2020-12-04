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
}

export interface IUserProfileCreate {
  email: string;
  first_name?: string;
  last_name?: string;
  password?: string;
  is_active?: boolean;
  role?: string;
}

export interface IUserRole {
  id: number;
  name: string;
}