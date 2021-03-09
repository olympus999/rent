import {
  IAccountingHour,
  IProject, IProjectWorkerAssociatedWithProject, ITool,
  IUserInfo,
  IUserProfile,
  IUserRole, IUserTool,
  IWorkerProfileAdmin,
  IWorkerProfileProjectAdmin
} from '@/interfaces';
import {AdminState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';
import {ClientState} from '@/store/client/state';

export const mutations = {
  setClients(state: AdminState, payload: IUserProfile[]) {
    state.users.clients = payload;
  },
  setUsers(state: AdminState, payload: IUserProfile[]) {
    state.users.users = payload;
  },
  setUser(state: AdminState, payload: IUserProfile) {
    const users = state.users.users.filter((user: IUserProfile) => user.id !== payload.id);
    users.push(payload);
    state.users.users = users;
  },
  setUsersRoles(state: AdminState, payload: IUserRole[]) {
    state.usersRoles = payload;
  },
  setProjects(state: AdminState, payload: IProject[]) {
    state.projects = payload;
  },
  setRemovedProjects(state: AdminState, payload: IProject[]) {
    state.removedProjects = payload
  },
  setWorkers(state: AdminState, payload: IWorkerProfileProjectAdmin[]) {
    state.users.workers = payload;
  },
  setWorkersAvailable(state: AdminState, payload: IWorkerProfileAdmin[]) {
    state.users.workersAvailable = payload;
  },
  setUserInfo(state: AdminState, payload: IUserInfo) {
    state.users.userInfo = payload;
  },
  setTools(state: AdminState, payload: ITool[]) {
    state.tools = payload
  },
  setUserTools(state: AdminState, payload: IUserTool[]) {
    state.users.userTools = payload
  },
  setProjectWorkerAssociatedWithUser(state: AdminState, payload: IProjectWorkerAssociatedWithProject[]) {
    state.projectWorkersAssociatedWithUser = payload
  },
  setUserAccountingHours(state: AdminState, payload: IAccountingHour[]) {
    state.users.accountingHours = payload
  }
};

const {commit} = getStoreAccessors<AdminState, State>('');

export const commitSetClients = commit(mutations.setClients);
export const commitSetUser = commit(mutations.setUser);
export const commitSetUsers = commit(mutations.setUsers);
export const commitSetUsersRoles = commit(mutations.setUsersRoles);
export const commitSetProjects = commit(mutations.setProjects);
export const commitSetWorkers = commit(mutations.setWorkers);
export const commitSetWorkersAvailable = commit(mutations.setWorkersAvailable);
export const commitSetRemovedProjects = commit(mutations.setRemovedProjects);
export const commitSetUserInfo = commit(mutations.setUserInfo)
export const commitSetTools = commit(mutations.setTools)
export const commitSetUserTools = commit(mutations.setUserTools)
export const commitSetProjectWorkersAssociatedWithUser = commit(mutations.setProjectWorkerAssociatedWithUser)
export const commitSetUserAccountingHours = commit(mutations.setUserAccountingHours)