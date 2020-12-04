<template>
    <div>
<!--        <v-toolbar light>-->
<!--            <v-toolbar-title>-->
<!--                Manage Users-->
<!--            </v-toolbar-title>-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn color="primary" to="/main/admin/users/create">Create User</v-btn>-->
<!--        </v-toolbar>-->
        <v-data-table :headers="headers" :items="workers">
            <template v-slot:item.is_active="{ item }">
                <v-icon v-if="item.is_active">checkmark</v-icon>
            </template>
<!--            <template v-slot:item.actions="{ item }">-->
<!--                <v-btn slot="activator" text :to="{name: 'main-client-workers-edit', params: {id: item.id}}">-->
<!--                    <v-icon small class="mr-2">-->
<!--                        mdi-pencil-->
<!--                    </v-icon>-->
<!--                </v-btn>-->
<!--            </template>-->
        </v-data-table>
    </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import { Store } from 'vuex';
  import { IUserProfile } from '@/interfaces';
  import { readWorkers } from '@/store/client/getters';
  import {dispatchGetWorkers} from '@/store/client/actions';

  @Component
  export default class Workers extends Vue {
    public headers = [
      {
        text: 'First Name',
        sortable: true,
        value: 'first_name',
        align: 'left',
      },
      {
        text: 'Is Active',
        sortable: true,
        value: 'is_active',
        align: 'left',
      },
      {
        text: 'Role',
        sortable: true,
        value: 'role',
        align: 'left',
      },
      {
        text: 'ID',
        value: 'id',
      },
      // {
      //   text: 'Actions',
      //   sortable: false,
      //   value: 'actions',
      //   align: 'left',
      // },
    ];
    get workers() {
      return readWorkers(this.$store);
    }

    public async mounted() {
      await dispatchGetWorkers(this.$store);
    }
  }
</script>
