import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { ClientState } from './state';

const defaultState: ClientState = {
  workers: [],
};

export const clientModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
