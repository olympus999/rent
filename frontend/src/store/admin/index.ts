import {mutations} from './mutations';
import {getters} from './getters';
import {actions} from './actions';
import {AdminState} from './state';
import {IAccountingBalance, IUserInfo} from '@/interfaces';

const defaultState: AdminState = {
  users: {
    users: [],
    clients: [],
    workers: [],
    workersAvailable: [],
    userInfo: {} as IUserInfo,
    userTools: [],
    accountingHours: [],
    accountingTransactions: [],
    accountingTransactionTypes: [],
    accountingBalance: {} as IAccountingBalance
  },
  tools: [],
  usersRoles: [],
  projects: [],
  projectWorkersAssociatedWithUser: [],
  removedProjects: [],
};

export const adminModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
