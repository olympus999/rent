import {api} from '@/api';
import { IProjectCreate } from '@/interfaces';
import {commitSetProjects, commitSetWorkers} from '@/store/client/mutations';
import {dispatchCheckApiError} from '@/store/main/actions';
import {ActionContext} from 'vuex';
import {ClientState} from '@/store/client/state';
import {State} from '@/store/state';
import {getStoreAccessors} from 'typesafe-vuex';
import {commitAddNotification, commitRemoveNotification} from '@/store/main/mutations';

type MainContext = ActionContext<ClientState, State>;

export const actions = {
  async actionGetWorkers(context: MainContext) {
    try {
      const response = await api.getWorkers(context.rootState.main.token)
      if (response) {
        commitSetWorkers(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  // async actionGetProjects(context: MainContext) {
  //   try {
  //     const response = await api.getProjectsClient(context.rootState.main.token)
  //     if (response) {
  //       commitSetProjects(context, response.data);
  //     }
  //   } catch (error) {
  //     await dispatchCheckApiError(context, error);
  //   }
  // },
  async actionCreateProject(context: MainContext, payload: IProjectCreate) {
    try {
      const response = await api.createProject(context.rootState.main.token, payload)
      if (response) {
        commitAddNotification(context, { content: 'Project successfully created', color: 'success' });
      }
    } catch (error) {
      commitAddNotification(context, { content: error.response.data.detail, color: 'error' });
    }
  }
}

const { dispatch } = getStoreAccessors<ClientState, State>('');

export const dispatchGetWorkers = dispatch(actions.actionGetWorkers);
export const dispatchCreateProject = dispatch(actions.actionCreateProject);
// export const dispatchGetProjects = dispatch(actions.actionGetProjects)