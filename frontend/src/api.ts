import axios from 'axios';
import { apiUrl } from '@/env';
import {
  IUserProfile, IUserProfileUpdate, IUserProfileCreate,
  IUserRole, IWorkerProfile, IProjectCreate, IProject,
  IProjectAdminCreateUpdate, IWorkerProfileAdmin, IWorkerProfileProjectAdmin, IUserFeedbackCreate,
  IUserInfo, ITool, IToolCreate, IToolUpdate, IUserToolCreate, IUserTool, IUserToolUpdate,
  IAccountingHour, IAccountingHourCreateUpdate
} from './interfaces';
import {IAccountingTransactionCreate} from '@/interfaces/AccountingTransaction';

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
  async getClients(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/clients/`, authHeaders(token));
  },
  // async createProject(token: string, data: IProjectCreate) {
  //   return axios.post<IProjectCreate>(`${apiUrl}/api/v1/projects/`, data, authHeaders(token));
  // },
  async getWorkers(token: string) {
    return axios.get<IWorkerProfileProjectAdmin[]>(`${apiUrl}/api/v1/workers/`, authHeaders(token));
  },
  async getWorkersAvailable(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/workers/available`, authHeaders(token));
  },
  // async getProjectsClient(token: string) {
  //   return axios.get<IProject[]>(`${apiUrl}/api/v1/projects/client`, authHeaders(token));
  // },
  async removeProject(token: string, projectId: number) {
    return axios.delete(`${apiUrl}/api/v1/projects/admin/${projectId}`, authHeaders(token));
  },
  async getProjectsAdmin(token: string) {
    return axios.get<IProject[]>(`${apiUrl}/api/v1/projects/admin`, authHeaders(token));
  },
  async getRemovedProjectsAdmin(token: string) {
    return axios.get<IProject[]>(`${apiUrl}/api/v1/projects/admin/removed`, authHeaders(token));
  },
  async createProjectAdmin(token: string, data: IProjectAdminCreateUpdate) {
    return axios.post(`${apiUrl}/api/v1/projects/admin/`, data, authHeaders(token))
  },
  async updateProjectAdmin(token: string, projectId: number, data: IProjectAdminCreateUpdate) {
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
  },
  async addUserFeedback(token: string, data: IUserFeedbackCreate) {
    return axios.post(`${apiUrl}/api/v1/user_feedback/`, data, authHeaders(token))
  },
  async getUserInfo(token: string, userId: number) {
    return axios.get<IUserInfo>(`${apiUrl}/api/v1/users/info/${userId}`, authHeaders(token))
  },
  async getTools(token: string) {
    return axios.get<ITool[]>(`${apiUrl}/api/v1/tools`, authHeaders(token))
  },
  async createTool(token: string, data: IToolCreate) {
    return axios.post<ITool>(`${apiUrl}/api/v1/tools`, data, authHeaders(token))
  },
  async updateTool(token: string, data: IToolUpdate) {
    return axios.put<ITool>(`${apiUrl}/api/v1/tools/${data.id}`, data, authHeaders(token))
  },
  async removeTool(token: string, toolId: number) {
    return axios.delete(`${apiUrl}/api/v1/tools/${toolId}`, authHeaders(token))
  },
  async getUserTools(token: string, userId: number) {
    return axios.get<IUserTool[]>(`${apiUrl}/api/v1/user_tools/user/${userId}`, authHeaders(token))
  },
  async createUserTool(token: string, data: IUserToolCreate) {
    return axios.post<IUserTool>(`${apiUrl}/api/v1/user_tools/`, data, authHeaders(token))
  },
  async updateUserTool(token: string, data: IUserToolUpdate) {
    return axios.put<IUserTool>(`${apiUrl}/api/v1/user_tools/${data.id}`, data, authHeaders(token))
  },
  async removeUserTool(token: string, userToolId: number) {
    return axios.delete(`${apiUrl}/api/v1/user_tools/${userToolId}`, authHeaders(token))
  },
  async getProjectWorkersAssociatedWithUser(token: string, userId: number) {
    return axios.get(`${apiUrl}/api/v1/project_worker/user/${userId}/projects`, authHeaders(token))
  },
  async getAccountingHoursByUser(token: string, userId: number, minDate: string, maxDate: string) {
    return axios.get<IAccountingHour[]>(`${apiUrl}/api/v1/accounting_hour/user/${userId}/${minDate}/${maxDate}`, authHeaders(token))
  },
  async createUpdateAccountingHours(token: string, data: IAccountingHourCreateUpdate[]) {
    return axios.post<IAccountingHour[]>(`${apiUrl}/api/v1/accounting_hour`, data, authHeaders(token))
  },
  async getAccountingTransactions(token: string, userId: number) {
    return axios.get(`${apiUrl}/api/v1/accounting_transaction/user/${userId}`, authHeaders(token))
  },
  async createAccountingTransaction(token: string, data: IAccountingTransactionCreate) {
    return axios.post(`${apiUrl}/api/v1/accounting_transaction/`, data, authHeaders(token))
  },
  async getAccountingTransactionTypes(token: string) {
    return axios.get(`${apiUrl}/api/v1/accounting_transaction_type/`, authHeaders(token))
  },
  async getAccountingBalanceByUser(token: string, userId: number) {
    return axios.get(`${apiUrl}/api/v1/accounting_balance/${userId}`, authHeaders(token))
  }
};