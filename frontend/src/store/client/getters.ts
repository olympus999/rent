import {ClientState} from '@/store/client/state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '@/store/state';

export const getters = {
  workers: (state: ClientState) => state.workers,
};

const { read } = getStoreAccessors<ClientState, State>('');

export const readWorkers = read(getters.workers);