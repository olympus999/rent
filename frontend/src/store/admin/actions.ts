import {api} from '@/api';
import {ActionContext} from 'vuex';
import {
  IProjectAdminCreateUpdate, IToolCreate, IToolUpdate,
  IUserFeedbackCreate,
  IUserProfileCreate,
  IUserProfileUpdate,
  IUserRole, IUserToolCreate, IUserToolUpdate
} from '@/interfaces';
import {State} from '../state';
import {AdminState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {
  commitSetUsers,
  commitSetUser,
  commitSetUsersRoles,
  commitSetWorkers,
  commitSetWorkersAvailable,
  commitSetRemovedProjects,
  commitSetUserInfo,
  commitSetTools,
  commitSetUserTools,
  commitSetProjectWorkersAssociatedWithUser, commitSetUserAccountingHours
} from './mutations';
import {dispatchCheckApiError} from '../main/actions';
import {commitAddNotification, commitRemoveNotification} from '../main/mutations';
import {commitSetProjects, commitSetClients} from '@/store/admin/mutations';
import router from '@/router';

type MainContext = ActionContext<AdminState, State>;

const manageError: (error, context, loadingNotification) => void = function async(error, context, loadingNotification) {
  commitRemoveNotification(context, loadingNotification);
  if (error && error.response) {
    commitAddNotification(context, {content: error.response.data.detail, color: 'error'});
  } else {
    commitAddNotification(context, {content: 'Something went wrong', color: 'error'});
  }
}

export const actions = {
  async actionGetUsers(context: MainContext) {
    try {
      const response = await api.getUsers(context.rootState.main.token);
      if (response) {
        commitSetUsers(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetClients(context: MainContext) {
    try {
      const response = await api.getClients(context.rootState.main.token);
      if (response) {
        commitSetClients(context, response.data);
      }
    } catch (error) {
      commitAddNotification(context, {content: 'Something went wrong', color: 'error'});
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetWorkers(context: MainContext) {
    try {
      const response = await api.getWorkers(context.rootState.main.token);
      if (response) {
        commitSetWorkers(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetWorkersAvailable(context: MainContext) {
    try {
      const response = await api.getWorkersAvailable(context.rootState.main.token);
      if (response) {
        commitSetWorkersAvailable(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateUser(context: MainContext, payload: { id: number, user: IUserProfileUpdate }) {
    try {
      const loadingNotification = {content: 'saving', showProgress: true};
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.updateUser(context.rootState.main.token, payload.id, payload.user),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitSetUser(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'User successfully updated', color: 'success'});
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionCreateUser(context: MainContext, payload: IUserProfileCreate) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.createUser(context.rootState.main.token, payload),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitSetUser(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'User successfully created', color: 'success'});
    } catch (error) {
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: error.response.data.detail, color: 'error'});
    }
  },
  async actionGetUsersRoles(context: MainContext) {
    try {
      const response = await api.getUsersRoles(context.rootState.main.token);
      if (response) {
        commitSetUsersRoles(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetProjects(context: MainContext) {
    try {
      const response = await api.getProjectsAdmin(context.rootState.main.token);
      if (response) {
        commitSetProjects(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateProject(context: MainContext, payload: { id: number, project: IProjectAdminCreateUpdate }) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.updateProjectAdmin(context.rootState.main.token, payload.id, payload.project),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Project successfully updated', color: 'success'});
      return true
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionCreateProject(context: MainContext, payload: {project: IProjectAdminCreateUpdate}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.createProjectAdmin(context.rootState.main.token, payload.project),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Project successfully created', color: 'success'});
      await router.push({ name: 'main-admin-projects-edit', params: { id: response.data.id }})
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionAddUserFeedback(context: MainContext, payload: {userFeedback: IUserFeedbackCreate}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.addUserFeedback(context.rootState.main.token, payload.userFeedback),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Feedback successfully given', color: 'success'});
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionRemoveProject(context: MainContext, payload: {projectId: number}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.removeProject(context.rootState.main.token, payload.projectId),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Project removed', color: 'success'});
      await router.push({ name: 'main-admin-projects' })
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionGetRemovedProjects(context: MainContext) {
    try {
      const response = await api.getRemovedProjectsAdmin(context.rootState.main.token);
      if (response) {
        commitSetRemovedProjects(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetUserInfo(context: MainContext, payload: {userId: number}) {
    try {
      const response = await api.getUserInfo(context.rootState.main.token, payload.userId);
      if (response) {
        commitSetUserInfo(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetTools(context: MainContext) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      const response = await api.getTools(context.rootState.main.token);
      if (response) {
        commitSetTools(context, response.data);
      }
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionCreateTool(context: MainContext, payload: {tool: IToolCreate}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      await api.createTool(context.rootState.main.token, payload.tool);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Tool added', color: 'success'});
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionDeleteTool(context: MainContext, payload: {toolId: number}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      await api.removeTool(context.rootState.main.token, payload.toolId);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Tool removed', color: 'success'});
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionUpdateTool(context: MainContext, payload: {tool: IToolUpdate}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      await api.updateTool(context.rootState.main.token, payload.tool);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Tool updated', color: 'success'});
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionGetUserTools(context: MainContext, payload: {userId: number}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      const response = await api.getUserTools(context.rootState.main.token, payload.userId);
      if (response) {
        commitSetUserTools(context, response.data);
      }
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionCreateUserTool(context: MainContext, payload: {userTool: IUserToolCreate}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      await api.createUserTool(context.rootState.main.token, payload.userTool);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'User tool created', color: 'success'});
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionUpdateUserTool(context: MainContext, payload: {userTool: IUserToolUpdate}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      await api.updateUserTool(context.rootState.main.token, payload.userTool);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'User tool updated', color: 'success'});
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionRemoveUserTool(context: MainContext, payload: {userToolId: number}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      await api.removeUserTool(context.rootState.main.token, payload.userToolId);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'User tool removed', color: 'success'});
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionGetProjectWorkersAssociatedWithUser(context: MainContext, payload: {userId: number}) {
    const loadingNotification = {content: 'saving', showProgress: true};
    try {
      const response = await api.getProjectWorkersAssociatedWithUser(context.rootState.main.token, payload.userId);
      if (response) {
        commitSetProjectWorkersAssociatedWithUser(context, response.data);
      }
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  },
  async actionGetUserAccountingHour(context: MainContext, payload: {userId: number, minDate: string, maxDate: string}) {
    const loadingNotification = {content: 'getting', showProgress: true};
    try {
      const response = await api.getAccountingHoursByUser(context.rootState.main.token,
        payload.userId,
        payload.minDate,
        payload.maxDate);
      if (response) {
        commitSetUserAccountingHours(context, response.data);
      }
    } catch (error) {
      await manageError(error, context, loadingNotification)
    }
  }
};

const {dispatch} = getStoreAccessors<AdminState, State>('');

export const dispatchCreateUser = dispatch(actions.actionCreateUser);
export const dispatchGetUsers = dispatch(actions.actionGetUsers);
export const dispatchGetClients = dispatch(actions.actionGetClients);
export const dispatchGetWorkers = dispatch(actions.actionGetWorkers);
export const dispatchGetWorkersAvailable = dispatch(actions.actionGetWorkersAvailable);
export const dispatchUpdateUser = dispatch(actions.actionUpdateUser);
export const dispatchGetUsersRoles = dispatch(actions.actionGetUsersRoles);
export const dispatchGetProjects = dispatch(actions.actionGetProjects);
export const dispatchUpdateProject = dispatch(actions.actionUpdateProject);
export const dispatchCreateProject = dispatch(actions.actionCreateProject);
export const dispatchAddUserFeedback = dispatch(actions.actionAddUserFeedback);
export const dispatchRemoveProject = dispatch(actions.actionRemoveProject)
export const dispatchGetRemovedProjects = dispatch(actions.actionGetRemovedProjects)
export const dispatchGetUserInfo = dispatch(actions.actionGetUserInfo)
export const dispatchGetTools = dispatch(actions.actionGetTools)
export const dispatchCreateTool = dispatch(actions.actionCreateTool)
export const dispatchDeleteTool = dispatch(actions.actionDeleteTool)
export const dispatchUpdateTool = dispatch(actions.actionUpdateTool)
export const dispatchGetUserTools = dispatch(actions.actionGetUserTools)
export const dispatchCreateUserTool = dispatch(actions.actionCreateUserTool)
export const dispatchUpdateUserTool = dispatch(actions.actionUpdateUserTool)
export const dispatchRemoveUserTool = dispatch(actions.actionRemoveUserTool)
export const dispatchGetProjectWorkersAssociatedWithUser = dispatch(actions.actionGetProjectWorkersAssociatedWithUser)
export const dispatchGetUserAccountingHour = dispatch(actions.actionGetUserAccountingHour)
