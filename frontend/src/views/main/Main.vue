<template>
  <div>
    <v-navigation-drawer persistent :mini-variant="miniDrawer" v-model="showDrawer" fixed app>
      <v-layout column fill-height>
        <v-list>
          <v-subheader>Main menu</v-subheader>
          <v-list-item to="/main/dashboard">
            <v-list-item-action>
              <v-icon>web</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item to="/main/profile/view">
            <v-list-item-action>
              <v-icon>person</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Profile</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
<!--          <v-list-item to="/main/profile/edit">-->
<!--            <v-list-item-action>-->
<!--              <v-icon>edit</v-icon>-->
<!--            </v-list-item-action>-->
<!--            <v-list-item-content>-->
<!--              <v-list-item-title>Edit Profile</v-list-item-title>-->
<!--            </v-list-item-content>-->
<!--          </v-list-item>-->
          <v-list-item to="/main/profile/password">
            <v-list-item-action>
              <v-icon>vpn_key</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Change Password</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-list subheader v-show="hasClientAccess">
          <v-subheader>Platform</v-subheader>
<!--          <v-list-item to="/main/client/projects/all">-->
<!--            <v-list-item-action>-->
<!--              <v-icon>group</v-icon>-->
<!--            </v-list-item-action>-->
<!--            <v-list-item-content>-->
<!--              <v-list-item-title>Projects</v-list-item-title>-->
<!--            </v-list-item-content>-->
<!--          </v-list-item>-->
        </v-list>
        <v-divider></v-divider>
        <v-list subheader v-show="hasAdminAccess">
          <v-subheader>Admin</v-subheader>
          <v-list-group
                  :value="false"
                  prepend-icon="mdi-account-circle"
                  sub-group
          >
            <template v-slot:activator>
              <v-list-item-title>Users</v-list-item-title>
            </template>
            <v-list-item to="/main/admin/users/all">
              <v-list-item-action>
                <v-icon>group</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Manage Users</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item to="/main/admin/users/create">
              <v-list-item-action>
                <v-icon>person_add</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Create User</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
          <v-list-group
                  :value="false"
                  prepend-icon="accessibility_new"
                  sub-group
          >
            <template v-slot:activator>
              <v-list-item-title>Workers</v-list-item-title>
            </template>
            <v-list-item to="/main/admin/workers/all">
              <v-list-item-action>
                <v-icon>accessibility_new</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Manage Workers</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
          <v-list-group
                  :value="false"
                  prepend-icon="work"
                  sub-group
          >
            <template v-slot:activator>
              <v-list-item-title>Projects</v-list-item-title>
            </template>
            <v-list-item to="/main/admin/projects/create">
              <v-list-item-action>
                <v-icon>work_outline</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Create Project</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item to="/main/admin/projects/all">
              <v-list-item-action>
                <v-icon>work</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Manage Projects</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item to="/main/admin/projects/removed">
              <v-list-item-action>
                <v-icon>work_off</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Removed Projects</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
          <v-list-group
                  :value="false"
                  prepend-icon="mdi-hammer-wrench"
                  sub-group
          >
            <template v-slot:activator>
              <v-list-item-title>Tools</v-list-item-title>
            </template>
            <v-list-item to="/main/admin/tools/all">
              <v-list-item-action>
                <v-icon>mdi-hammer-wrench</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Manage Tools</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
        </v-list>
        <v-spacer></v-spacer>
        <v-list>
          <v-list-item @click="logout">
            <v-list-item-action>
              <v-icon>close</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item @click="switchMiniDrawer">
            <v-list-item-action>
              <v-icon v-html="miniDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Collapse</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-layout>
    </v-navigation-drawer>
    <v-app-bar dark color="primary" app>
      <v-app-bar-nav-icon @click.stop="switchShowDrawer"></v-app-bar-nav-icon>
      <v-toolbar-title v-text="appName"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu bottom left offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>more_vert</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item to="/main/profile">
            <v-list-item-content>
              <v-list-item-title>Profile</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>person</v-icon>
            </v-list-item-action>
          </v-list-item>
          <v-list-item @click="logout">
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>close</v-icon>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
    <v-footer class="pa-3" fixed app>
      <v-spacer></v-spacer>
      <span>&copy; {{appName}}</span>
    </v-footer>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

import { appName } from '@/env';
import { readDashboardMiniDrawer, readDashboardShowDrawer, readHasAdminAccess, readHasClientAccess } from '@/store/main/getters';
import { commitSetDashboardShowDrawer, commitSetDashboardMiniDrawer } from '@/store/main/mutations';
import { dispatchUserLogOut } from '@/store/main/actions';

const routeGuardMain = async (to, from, next) => {
  if (to.path === '/main') {
    next('/main/dashboard');
  } else {
    next();
  }
};

@Component
export default class Main extends Vue {
  public appName = appName;

  public beforeRouteEnter(to, from, next) {
    routeGuardMain(to, from, next);
  }

  public beforeRouteUpdate(to, from, next) {
    routeGuardMain(to, from, next);
  }

  get miniDrawer() {
    return readDashboardMiniDrawer(this.$store);
  }

  get showDrawer() {
    return readDashboardShowDrawer(this.$store);
  }

  set showDrawer(value) {
    commitSetDashboardShowDrawer(this.$store, value);
  }

  public switchShowDrawer() {
    commitSetDashboardShowDrawer(
      this.$store,
      !readDashboardShowDrawer(this.$store),
    );
  }

  public switchMiniDrawer() {
    commitSetDashboardMiniDrawer(
      this.$store,
      !readDashboardMiniDrawer(this.$store),
    );
  }

  public get hasAdminAccess() {
    return readHasAdminAccess(this.$store);
  }
  public get hasClientAccess() {
    return readHasClientAccess(this.$store);
  }

  public async logout() {
    await dispatchUserLogOut(this.$store);
  }
}
</script>
