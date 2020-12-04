import { IUserProfile, IUserRole, IWorkerProfile } from '@/interfaces';
import { ClientState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setWorkers(state: ClientState, payload: IWorkerProfile[]) {
      state.workers = payload;
    }
}

const { commit } = getStoreAccessors<ClientState, State>('');

export const commitSetWorkers = commit(mutations.setWorkers);