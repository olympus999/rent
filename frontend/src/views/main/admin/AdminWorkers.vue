<template>
    <div>
        <v-toolbar light>
            <v-toolbar-title>
                Book
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <create-project :workers="this.bookedWorkers" v-if="bookedWorkers.length > 0"></create-project>
<!--            <v-btn v-if="bookedWorkers.length > 0" color="primary">Book selected workers</v-btn>-->
        </v-toolbar>
        <v-data-table :headers="headers" :items="workers">
            <template v-slot:header.data-table-select>
<!--                Removing a way to select all at once     -->
            </template>
            <template v-slot:item.data-table-select="{ item, isSelected, select }">
                <div v-if="item.available">
                    <v-simple-checkbox
                                       :value="isSelected"
                                       @input="select($event)"
                                       :disabled="!item.available"
                                       @click="updateBookedWorkers(item, !isSelected)">
                    </v-simple-checkbox>
                </div>
            </template>
          <template  v-slot:item.show_available="{ item }">
            <div v-if="item.show_available">
              <v-icon large color="green darken-2"> mdi-circle-medium </v-icon>
            </div>
            <div v-else>
              <v-icon large color="red darken-2"> mdi-circle-medium </v-icon>
            </div>
          </template>
          <template v-slot:item.user_info="{ item }">
            <v-btn slot="activator" text :to="{name: 'main-admin-user-details', params: {id: item.id}}">
              <v-icon small class="mr-2">
                mdi-pencil
              </v-icon>
            </v-btn>
          </template>
          <template v-slot:item.edit_user="{ item }">
            <v-btn slot="activator" text :to="{name: 'main-admin-users-edit', params: {id: item.id}}">
              <v-icon small class="mr-2">
                mdi-pencil
              </v-icon>
            </v-btn>
          </template>
          <template v-slot:item.edit_project="{ item }">
            <div v-if="item.project_worker_active">
              <v-btn slot="activator" text :to="{name: 'main-admin-projects-edit', params: {id: item.project_worker_active.project_worker.project.id}}">
                <v-icon small class="mr-2">
                  mdi-pencil
                </v-icon>
              </v-btn>
            </div>
          </template>
        </v-data-table>
    </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import { Store } from 'vuex';
  import { IUserProfile, IUserFeedback } from '@/interfaces';
  import { readAdminWorkers } from '@/store/admin/getters';
  import { dispatchGetWorkers } from '@/store/admin/actions';
  // import CreateProject from '@/views/main/client/modals/CreateProject.vue';
  @Component({
    // components: {CreateProject}
  })
  export default class Workers extends Vue {
    public bookedWorkers: IUserProfile[] = [];
    public headers = [
      {
        text: 'First Name',
        sortable: true,
        value: 'first_name',
        align: 'left',
        width: '100'
      },
      {
        text: 'Role',
        sortable: true,
        value: 'role',
        align: 'left',
        width: '100'
      },
      {
        text: 'Available',
        sortable: true,
        value: 'show_available',
        width: '100'
      },
      {
        text: 'Available',
        sortable: true,
        value: 'available',
        width: '100'
      },
      {
        text: 'User Info',
        sortable: true,
        value: 'user_info',
        width: 100,
      },
      {
        text: 'Edit user',
        sortable: true,
        value: 'edit_user',
        width: 100,
      },
      {
        text: 'Edit project',
        sortable: true,
        value: 'edit_project',
        width: 100,
      },
      {
        text: 'Rating',
        sortable: true,
        value: 'average_rating',
        width: 100,
      },
      {
        text: 'ID',
        value: 'id',
      },
    ];

    public async mounted() {
      await dispatchGetWorkers(this.$store);
    }

    get workers() {
      return readAdminWorkers(this.$store);
    }

    public async updateBookedWorkers(item, newValue) {
      if (newValue) {
        this.bookedWorkers.push(item)
      } else {
        this.bookedWorkers = this._.remove(this.bookedWorkers, (t) => t.id !== item.id)
      }
    }
  }
</script>
