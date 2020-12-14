import { api } from '@/api';
import { ActionContext } from 'vuex';
import {IProjectUpdate, IUserProfileCreate, IUserProfileUpdate, IUserRole} from '@/interfaces';
import { State } from '../state';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { commitSetUsers, commitSetUser, commitSetUsersRoles, commitSetWorkers, commitSetWorkersAvailable } from './mutations';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';
import { commitSetProjects } from '@/store/admin/mutations';

type MainContext = ActionContext<AdminState, State>;

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
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateUser(context.rootState.main.token, payload.id, payload.user),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateUser(context: MainContext, payload: IUserProfileCreate) {
        const loadingNotification = { content: 'saving', showProgress: true };
        try {
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createUser(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully created', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: error.response.data.detail, color: 'error' });
        }
    },
    async actionGetUsersRoles(context: MainContext) {
        try {
            const response = await api.getUsersRoles(context.rootState.main.token);
            if (response) {
                commitSetUsersRoles(context, response.data)
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionGetProjects(context: MainContext) {
        try {
            const response = await api.getProjectsAdmin(context.rootState.main.token)
            if (response) {
                commitSetProjects(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateProject(context: MainContext, payload: { id: number, project: IProjectUpdate}) {
        const loadingNotification = { content: 'saving', showProgress: true };
        try {
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateProjectAdmin(context.rootState.main.token, payload.id, payload.project),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Project successfully updated', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            if(error && error.response) {
                commitAddNotification(context, { content: error.response.data.detail, color: 'error' });
            } else {
                commitAddNotification(context, { content: 'Something went wrong', color: 'error' });
            }
        }
    }
};

const { dispatch } = getStoreAccessors<AdminState, State>('');

export const dispatchCreateUser = dispatch(actions.actionCreateUser);
export const dispatchGetUsers = dispatch(actions.actionGetUsers);
// export const dispatchGetWorkers = dispatch(actions.actionGetWorkers);
export const dispatchGetWorkersAvailable = dispatch(actions.actionGetWorkersAvailable);
export const dispatchUpdateUser = dispatch(actions.actionUpdateUser);
export const dispatchGetUsersRoles = dispatch(actions.actionGetUsersRoles);
export const dispatchGetProjects = dispatch(actions.actionGetProjects);
export const dispatchUpdateProject = dispatch(actions.actionUpdateProject);
