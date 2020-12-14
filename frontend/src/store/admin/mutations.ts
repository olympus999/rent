import {IProject, IUserProfile, IUserRole, IWorkerProfileAdmin} from '@/interfaces';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';
import {ClientState} from '@/store/client/state';

export const mutations = {
    setUsers(state: AdminState, payload: IUserProfile[]) {
        state.users = payload;
    },
    setUser(state: AdminState, payload: IUserProfile) {
        const users = state.users.filter((user: IUserProfile) => user.id !== payload.id);
        users.push(payload);
        state.users = users;
    },
    setUsersRoles(state: AdminState, payload: IUserRole[]) {
        state.usersRoles = payload;
    },
    setProjects(state: AdminState, payload: IProject[]) {
        state.projects = payload;
    },
    setWorkers(state: AdminState, payload: IWorkerProfileAdmin[]) {
        state.workers = payload;
    },
    setWorkersAvailable(state: AdminState, payload: IWorkerProfileAdmin[]) {
      state.workersAvailable = payload;
    }
};

const { commit } = getStoreAccessors<AdminState, State>('');

export const commitSetUser = commit(mutations.setUser);
export const commitSetUsers = commit(mutations.setUsers);
export const commitSetUsersRoles = commit(mutations.setUsersRoles);
export const commitSetProjects = commit(mutations.setProjects);
export const commitSetWorkers = commit(mutations.setWorkers);
export const commitSetWorkersAvailable = commit(mutations.setWorkersAvailable);