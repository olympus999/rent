<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on" :disabled="disabled">
          Add workers
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Add workers</span>
        </v-card-title>
        <v-card-text>
          <v-data-table :headers="headers" :items="availableWorkers" show-select>
            <template v-slot:header.data-table-select>
              <!--                Removing a way to select all at once     -->
            </template>
            <template v-slot:item.data-table-select="{ item, isSelected, select }">
              <div v-if="item.available">
                <v-simple-checkbox
                        :value="isSelected"
                        @input="select($event)"
                        :disabled="!item.available"
                        @click="setWorkersForProject(item, !isSelected)">
                </v-simple-checkbox>
              </div>
            </template>
            <template v-slot:item.available="{ item }">
              <div v-if="item.available">
                <v-icon large color="green darken-2"> mdi-circle-medium</v-icon>
              </div>
              <div v-else>
                <v-icon large color="red darken-2"> mdi-circle-medium</v-icon>
              </div>
            </template>
          </v-data-table>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
            Close
          </v-btn>
          <v-btn color="blue darken-1" text @click="submit">
            Add selected workers
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script lang="ts">
  import { Component, Vue} from 'vue-property-decorator';
  import { IProjectWorkerAdminCreateUpdate, IUserProfile } from '@/interfaces';
  import { readAdminWorkersAvailable } from '@/store/admin/getters';
  import { dispatchGetWorkersAvailable } from '@/store/admin/actions';

  const ProjectAddWorkersProps = Vue.extend({
    props: {
      projectWorker: Array as () => IProjectWorkerAdminCreateUpdate[],
      disabled: {type: Boolean, default: false}
    }
  });

  @Component
  export default class ProjectAddWorkers extends ProjectAddWorkersProps {
    public bookedWorkers: IUserProfile[] = [];
    public dialog: boolean = false;
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
        value: 'available',
        width: '100'
      },
      {
        text: 'ID',
        value: 'id',
      },
    ];

    public async submit() {
      this.$emit('handle-add-workers', this.bookedWorkers);
      this.bookedWorkers = []
      this.dialog = false;
    }

    public async setWorkersForProject(item, newValue) {
      if (newValue) {
        this.bookedWorkers.push(item);
      } else {
        this.bookedWorkers = this._.remove(this.bookedWorkers, (t) => t.id !== item.id);
      }
    }

    get availableWorkers() {
      const existingUserIds = this.projectWorker.map((obj) => obj.worker.id);
      return readAdminWorkersAvailable(this.$store)(existingUserIds);
    }

    public async mounted() {
      await dispatchGetWorkersAvailable(this.$store);
    }
  }
</script>

<style scoped>

</style>