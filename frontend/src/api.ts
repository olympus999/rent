import axios from 'axios';
import { apiUrl } from '@/env';
import {
  IUserProfile, IUserProfileUpdate, IUserProfileCreate,
  IUserRole, IWorkerProfile, IProjectCreate, IProject, IProjectUpdate, IWorkerProfileAdmin
} from './interfaces';

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(`${apiUrl}/api/v1/users/me`, data, authHeaders(token));
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async createProject(token: string, data: IProjectCreate) {
    return axios.post<IProjectCreate>(`${apiUrl}/api/v1/projects/`, data, authHeaders(token));
  },
  async getWorkers(token: string) {
    return axios.get<IWorkerProfileAdmin[]>(`${apiUrl}/api/v1/workers/`, authHeaders(token));
  },
  async getWorkersAvailable(token: string) {
    return axios.get<IWorkerProfileAdmin[]>(`${apiUrl}/api/v1/workers/available`, authHeaders(token));
  },
  // async getProjectsClient(token: string) {
  //   return axios.get<IProject[]>(`${apiUrl}/api/v1/projects/client`, authHeaders(token));
  // },
  async getProjectsAdmin(token: string) {
    return axios.get<IProject[]>(`${apiUrl}/api/v1/projects/admin`, authHeaders(token));
  },
  async updateProjectAdmin(token: string, projectId: number, data: IProjectUpdate) {
    return axios.put(`${apiUrl}/api/v1/projects/admin/${projectId}`, data, authHeaders(token))
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async getUsersRoles(token: string) {
    return axios.get<IUserRole[]>(`${apiUrl}/api/v1/user_roles/`, authHeaders(token));
  },
  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/v1/reset-password/`, {
      new_password: password,
      token,
    });
  },
  async addressAutoComplete(token: string, address: string) {
    return axios.get(`${apiUrl}/api/v1/google_maps/address_auto_complete/`,
      {...authHeaders(token), params:{ address }})
  }
};