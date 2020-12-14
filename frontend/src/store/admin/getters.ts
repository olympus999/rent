import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    adminUsers: (state: AdminState) => state.users,
    adminOneUser: (state: AdminState) => (userId: number) => {
        const filteredUsers = state.users.filter((user) => user.id === userId);
        if (filteredUsers.length > 0) {
            return { ...filteredUsers[0] };
        }
    },
    adminProjects: (state: AdminState) => state.projects,
    adminOneProject: (state: AdminState) => (projectId: number) => {
        const filteredProjects = state.projects.filter((project) => project.id === projectId);
        if (filteredProjects.length > 0) {
            return { ...filteredProjects[0] }
        }
    },
    adminWorkers: (state: AdminState) => (dontIncludeIds: number[]) => {
        return state.workers.filter((worker) => !dontIncludeIds.includes(worker.id))
    },
    adminWorkersAvailable: (state: AdminState) => (dontIncludeIds: number[]) => {
      return state.workersAvailable.filter((worker) => !dontIncludeIds.includes(worker.id))
    },
    usersRoles: (state: AdminState) => state.usersRoles.map(userRole => userRole.name),
};

const { read } = getStoreAccessors<AdminState, State>('');

export const readAdminOneUser = read(getters.adminOneUser);
export const readAdminUsers = read(getters.adminUsers);
export const readAdminWorkers = read(getters.adminWorkers);
export const readAdminWorkersAvailable = read(getters.adminWorkersAvailable);
export const readUsersRolesNames = read(getters.usersRoles);
export const readAdminProjects = read(getters.adminProjects)
export const readAdminOneProject = read(getters.adminOneProject)