import {MainState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';

export const getters = {
  hasAdminAccess: (state: MainState) => {
    return (
      state.userProfile &&
      state.userProfile.role === 'superuser' && state.userProfile.is_active);
  },
  hasClientAccess: (state: MainState) => {
    return (
      (state.userProfile &&
        state.userProfile.role === 'client' && state.userProfile.is_active) ||
      (state.userProfile && state.userProfile.role === 'superuser')
    );
  },
  loginError: (state: MainState) => state.logInError,
  dashboardShowDrawer: (state: MainState) => state.dashboardShowDrawer,
  dashboardMiniDrawer: (state: MainState) => state.dashboardMiniDrawer,
  userProfile: (state: MainState) => state.userProfile,
  token: (state: MainState) => state.token,
  isLoggedIn: (state: MainState) => state.isLoggedIn,
  firstNotification: (state: MainState) => state.notifications.length > 0 && state.notifications[0],
};

const {read} = getStoreAccessors<MainState, State>('');

export const readDashboardMiniDrawer = read(getters.dashboardMiniDrawer);
export const readDashboardShowDrawer = read(getters.dashboardShowDrawer);
export const readHasAdminAccess = read(getters.hasAdminAccess);
export const readHasClientAccess = read(getters.hasClientAccess);
export const readIsLoggedIn = read(getters.isLoggedIn);
export const readLoginError = read(getters.loginError);
export const readToken = read(getters.token);
export const readUserProfile = read(getters.userProfile);
export const readFirstNotification = read(getters.firstNotification);
