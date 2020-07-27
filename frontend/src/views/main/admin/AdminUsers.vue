<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Users
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/users/create">Create User</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="users">
      <template v-slot:item.is_active="{ item }">
        <v-icon v-if="item.is_active">checkmark</v-icon>
      </template>
      <template v-slot:item.is_superuser="{ item }">
        <v-icon v-if="item.is_superuser">checkmark</v-icon>
      </template>
      <template v-slot:item.is_client="{ item }">
        <v-icon v-if="item.is_client">checkmark</v-icon>
      </template>
      <template v-slot:item.is_worker="{ item }">
        <v-icon v-if="item.is_worker">checkmark</v-icon>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-btn slot="activator" text :to="{name: 'main-admin-users-edit', params: {id: item.id}}">
          <v-icon small class="mr-2">
            mdi-pencil
          </v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfile } from '@/interfaces';
import { readAdminUsers } from '@/store/admin/getters';
import { dispatchGetUsers } from '@/store/admin/actions';

@Component
export default class AdminUsers extends Vue {
  public headers = [
    {
      text: 'Email',
      sortable: true,
      value: 'email',
      align: 'left',
    },
    {
      text: 'First Name',
      sortable: true,
      value: 'first_name',
      align: 'left',
    },
    {
      text: 'Last Name',
      sortable: true,
      value: 'last_name',
      align: 'left',
    },
    {
      text: 'Is Active',
      sortable: true,
      value: 'is_active',
      align: 'left',
    },
    {
      text: 'Is Superuser',
      sortable: true,
      value: 'is_superuser',
      align: 'left',
    },
    {
      text: 'Is Client',
      sortable: true,
      value: 'is_client',
      align: 'left',
    },
    {
      text: 'Is Worker',
      sortable: true,
      value: 'is_worker',
      align: 'left',
    },
    {
      text: 'ID',
      value: 'id',
    },
    {
      text: 'Actions',
      sortable: false,
      value: 'actions',
      align: 'left',
    },
  ];
  get users() {
    return readAdminUsers(this.$store);
  }

  public async mounted() {
    await dispatchGetUsers(this.$store);
  }
}
</script>
