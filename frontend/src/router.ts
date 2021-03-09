import Vue from 'vue';
import Router from 'vue-router';

import RouterComponent from './components/RouterComponent.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import(/* webpackChunkName: "start" */ './views/main/Start.vue'),
      children: [
        {
          path: 'login',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "login" */ './views/Login.vue'),
        },
        {
          path: 'recover-password',
          component: () => import(/* webpackChunkName: "recover-password" */ './views/PasswordRecovery.vue'),
        },
        {
          path: 'reset-password',
          component: () => import(/* webpackChunkName: "reset-password" */ './views/ResetPassword.vue'),
        },
        {
          path: 'main',
          component: () => import(/* webpackChunkName: "main" */ './views/main/Main.vue'),
          children: [
            {
              path: 'dashboard',
              component: () => import(/* webpackChunkName: "main-dashboard" */ './views/main/Dashboard.vue'),
            },
            {
              path: 'profile',
              component: RouterComponent,
              redirect: 'profile/view',
              children: [
                {
                  path: 'view',
                  component: () => import(
                    /* webpackChunkName: "main-profile" */ './views/main/profile/UserProfile.vue'),
                },
                // {
                //   path: 'edit',
                //   component: () => import(
                //     /* webpackChunkName: "main-profile-edit" */ './views/main/profile/UserProfileEdit.vue'),
                // },
                {
                  path: 'password',
                  component: () => import(
                    /* webpackChunkName: "main-profile-password" */ './views/main/profile/UserProfileEditPassword.vue'),
                },
              ],
            },
            {
              path: 'client',
              component: () => import(/* webpackChunkName: "main-admin" */ './views/main/client/Client.vue'),
              redirect: 'client/projects/all',
              children: [
                {
                  path: 'projects/all',
                  name: 'main-client-projects',
                  component: () => import(
                    /* webpackChunkName: "main-client-projects" */ './views/main/client/Projects.vue'),
                }
              ]
            },
            {
              path: 'admin',
              component: () => import(/* webpackChunkName: "main-admin" */ './views/main/admin/Admin.vue'),
              redirect: 'admin/users/all',
              children: [
                {
                  path: 'users',
                  component: RouterComponent,
                  redirect: 'admin/users/all',
                  children: [
                    {
                      path: '/',
                      redirect: 'all',
                    },
                    {
                      path: 'all',
                      component: () => import(
                        /* webpackChunkName: "main-admin-users" */ './views/main/admin/AdminUsers.vue'),
                    },
                    {
                      path: 'edit/:id',
                      name: 'main-admin-users-edit',
                      component: () => import(
                        /* webpackChunkName: "main-admin-users-edit" */ './views/main/admin/EditUser.vue'),
                    },
                    {
                      path: 'create',
                      name: 'main-admin-users-create',
                      component: () => import(
                        /* webpackChunkName: "main-admin-users-create" */ './views/main/admin/CreateUser.vue'),
                    },
                    {
                      path: 'details/:id',
                      name: 'main-admin-user-details',
                      component: () => import(
                        /* webpackChunkName: "main-admin-users-details" */ './views/main/admin/DetailsUser.vue'),
                    },
                  ]
                },
                {
                  path: 'workers',
                  component: RouterComponent,
                  redirect: 'workers/all',
                  children: [
/*                    {
                      path: 'info/:id',
                      name: 'main-admin-workers-info',
                      component: () => import(
                        /!* webpackChunkName: "main-admin-workers-info" *!/ './views/main/admin/UserDetails.vue'),
                    },*/
                    {
                      path: 'all',
                      name: 'main-admin-workers-all',
                      component: () => import(
                        /* webpackChunkName: "main-admin-workers" */ './views/main/admin/AdminWorkers.vue'),
                    },
                  ]
                },
                {
                  path: 'projects',
                  component: RouterComponent,
                  redirect: 'projects/all',
                  children: [
                    {
                      path: 'all',
                      name: 'main-admin-projects',
                      component: () => import(
                        /* webpackChunkName: "main-admin-projects" */ './views/main/admin/Projects.vue'),
                    },
                    {
                      path: 'removed',
                      name: 'main-admin-removed-projects',
                      component: () => import(
                        /* webpackChunkName: "main-admin-removed-projects" */ './views/main/admin/Projects.vue'),
                      props: {
                        showRemovedProjects: true
                      }
                    },
                    {
                      path: 'create',
                      name: 'main-admin-projects-create',
                      component: () => import(
                        /* webpackChunkName: "main-admin-projects-create" */ './views/main/admin/CreateEditProject.vue'),
                      props: {
                        create: true
                      }
                    },
                    {
                      path: 'edit/:id',
                      name: 'main-admin-projects-edit',
                      component: () => import(
                        /* webpackChunkName: "main-admin-projects-edit" */ './views/main/admin/CreateEditProject.vue'),
                      props: {
                        create: true
                      }
                    }
                  ]
                },
                {
                  path: 'tools',
                  component: RouterComponent,
                  redirect: 'tools/all',
                  children: [
                    {
                      path: 'all',
                      name: 'main-admin-tools',
                      component: () => import(
                        /* webpackChunkName: "main-admin-tools" */ './views/main/admin/Tools.vue'),
                    },
                  ]
                }
              ],
            },
          ],
        },
      ],
    },
    {
      path: '/*', redirect: '/',
    },
  ],
});
