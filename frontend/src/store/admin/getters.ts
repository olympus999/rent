import {AdminState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';

export const getters = {
  adminClients: (state: AdminState) => state.users.clients,
  adminUsers: (state: AdminState) => state.users.users,
  adminOneUser: (state: AdminState) => (userId: number) => {
    const filteredUsers = state.users.users.filter((user) => user.id === userId);
    if (filteredUsers.length > 0) {
      return {...filteredUsers[0]};
    }
  },
  adminProjects: (state: AdminState) => state.projects,
  adminRemovedProjects: (state: AdminState) => state.removedProjects,
  adminOneProject: (state: AdminState) => (projectId: number) => {
    let filteredProjects = state.projects.filter((project) => project.id === projectId);
    if (filteredProjects.length > 0) {
      return {...filteredProjects[0]};
    } else {
      // Check for removed projects
      filteredProjects = state.removedProjects.filter((project) => project.id === projectId);
      if (filteredProjects.length > 0) {
        return {...filteredProjects[0]};
      }
    }
  },
  adminWorkers: (state: AdminState) => state.users.workers,
  adminWorkersAvailable: (state: AdminState) => (dontIncludeIds: number[]) => {
    return state.users.workersAvailable.filter((worker) => !dontIncludeIds.includes(worker.id));
  },
  usersRoles: (state: AdminState) => state.usersRoles.map(userRole => userRole.name),
  adminUserInfo: (state: AdminState) => state.users.userInfo,
  adminTools: (state: AdminState) => state.tools,
  adminUserTools: (state: AdminState) => state.users.userTools,
  adminProjectWorkersAssociatedWithUser: (state: AdminState) => state.projectWorkersAssociatedWithUser,
  adminUserAccountingHours: (state: AdminState) => state.users.accountingHours,
};

const {read} = getStoreAccessors<AdminState, State>('');

export const readAdminClients = read(getters.adminClients);
export const readAdminOneUser = read(getters.adminOneUser);
export const readAdminUsers = read(getters.adminUsers);
export const readAdminWorkers = read(getters.adminWorkers);
export const readAdminWorkersAvailable = read(getters.adminWorkersAvailable);
export const readUsersRolesNames = read(getters.usersRoles);
export const readAdminProjects = read(getters.adminProjects);
export const readAdminRemovedProjects = read(getters.adminRemovedProjects);
export const readAdminOneProject = read(getters.adminOneProject);
export const readAdminUserInfo = read(getters.adminUserInfo);
export const readAdminTools = read(getters.adminTools);
export const readAdminUserTools = read(getters.adminUserTools);
export const readAdminProjectWorkersAssociatedWithUser = read(getters.adminProjectWorkersAssociatedWithUser);
export const readAdminUserAccountingHours = read(getters.adminUserAccountingHours)
