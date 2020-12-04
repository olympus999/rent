import {api} from '@/api';
import { IProjectCreate } from '@/interfaces';
import {commitSetWorkers} from '@/store/client/mutations';
import {dispatchCheckApiError} from '@/store/main/actions';
import {ActionContext} from 'vuex';
import {ClientState} from '@/store/client/state';
import {State} from '@/store/state';
import {getStoreAccessors} from 'typesafe-vuex';

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
  async actionCreateProject(context: MainContext, payload: IProjectCreate) {
    console.log('test')
    try {
      const response = await api.createProject(context.rootState.main.token, payload)
      console.log('after api')
      if (response) {
        return true
        // DO something
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  }
}

const { dispatch } = getStoreAccessors<ClientState, State>('');

export const dispatchGetWorkers = dispatch(actions.actionGetWorkers);
export const dispatchCreateProject = dispatch(actions.actionCreateProject);