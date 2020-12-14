<template>
  <ValidationObserver v-slot="{ invalid }" ref="provider">
    <v-container fluid>
      <v-card class="ma-3 pa-3" max-width="900">
        <v-card-title primary-title>
          <div class="headline primary--text">Edit project</div>
        </v-card-title>
        <v-card-text>
          <template>
            <v-form ref="form" lazy-validation>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <v-text-field label="Name" v-model="name" :error-messages="errors" :success="valid"></v-text-field>
              </ValidationProvider>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <address-auto-complete v-model="address" :success="valid" :error-messages="errors">
                </address-auto-complete>
              </ValidationProvider>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <v-text-field label="Description" v-model="description" :error-messages="errors"
                              :success="valid"></v-text-field>
              </ValidationProvider>
            </v-form>
            <project-add-workers v-on:handle-add-workers="handleAddWorkers"
                                 :projectWorkerDetails="projectWorkerDetails"></project-add-workers>
          </template>
        </v-card-text>
        <v-data-table :headers="headers" :items="projectWorkerDetails" :item-class="row_classes" class="elevation-1">
          <template v-slot:item.accept_worker="{ item }">
            <div v-if="!item.worker_accepted_dt && !item.removed_dt">
              <v-btn @click="acceptWorker(item)">
                Accept worker
              </v-btn>
            </div>
          </template>
          <template v-slot:item.remove="{ item }">
            <div v-if="item.removed_dt">
              <v-btn @click="undoRemoveWorker(item)">
                Undo
              </v-btn>
            </div>
            <div v-else>
              <v-btn @click="removeWorker(item)">
                Remove
              </v-btn>
            </div>
          </template>
        </v-data-table>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="cancel">Cancel</v-btn>
          <v-btn @click="reset">Reset</v-btn>
          <v-btn @click="submit" :disabled="invalid"> Update</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </ValidationObserver>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import {dispatchGetProjects, dispatchUpdateProject} from '@/store/admin/actions';
  import {readAdminOneProject} from '@/store/admin/getters';
  import {IProjectUpdate, IProjectWorkerUpdate, IWorkerProfile, IWorkerProfileAdminUpdate} from '@/interfaces';
  import ProjectAddWorkers from '@/views/main/admin/modals/ProjectAddWorkers.vue';
  import AddressAutoComplete from '@/components/AddressAutoComplete.vue';

  @Component({
    components: {AddressAutoComplete, ProjectAddWorkers}
  })
  export default class EditProject extends Vue {
    public project_id: number = -1;
    public user_id: number = -1;
    public name: string = '';
    public address: string = '';
    public description: string = '';
    public projectWorkerDetails: IProjectWorkerUpdate[] = [];
    // public test: string = '';

    public headers = [
      {
        text: 'First name',
        sortable: true,
        value: 'worker.first_name',
        align: 'left',
      },
      {
        text: 'Added',
        sortable: true,
        value: 'created_dt',
        align: 'left',
      },
      {
        text: 'Accepted',
        sortable: true,
        value: 'worker_accepted_dt',
        align: 'left',
      },
      {
        text: 'Accept worker',
        sortable: true,
        value: 'accept_worker',
        align: 'left',
      },
      {
        text: 'Removed',
        sortable: true,
        value: 'removed_dt',
        align: 'left',
      },
      {
        text: 'Remove',
        sortable: true,
        value: 'remove',
        align: 'left',
      }
    ];


    public async mounted() {
      await dispatchGetProjects(this.$store);
      this.reset();
    }

    public cancel() {
      this.$router.back();
    }

    public async handleAddWorkers(workers: IWorkerProfileAdminUpdate[]) {
      workers.forEach((worker) => {
        const projectWorker: IProjectWorkerUpdate = {
          project_id: this.project!.id,
          user_id: worker.id,
          removed_dt: null,
          worker,
        };
        this.projectWorkerDetails.push(projectWorker);
      });
    }

    public async acceptWorker(item) {
      item.worker_accepted_dt = Date.now();
    }

    public async undoRemoveWorker(item) {
      item.removed_dt = null;
    }

    public async removeWorker(item) {
      item.removed_dt = Date.now();
    }

    public reset() {
      if (this.project) {
        this.name = this.project.name;
        this.address = this.project.address;
        this.description = this.project.description;
        this.projectWorkerDetails = this.project.project_worker_details;
      }
    }

    get project() {
      return readAdminOneProject(this.$store)(+this.$router.currentRoute.params.id);
    }

    row_classes(item) {
      if (item.removed_dt) {
        return 'background-red';
      }
    }

    public async submit() {
      const updatedProject: IProjectUpdate = {};
      if (this.name) {
        updatedProject.name = this.name;
      }
      if (this.address) {
        updatedProject.address = this.address;
      }
      if (this.description) {
        updatedProject.description = this.description;
      }
      if (this.projectWorkerDetails) {
        updatedProject.project_worker_details = this.projectWorkerDetails;
      }
      await dispatchUpdateProject(this.$store, {id: this.project!.id, project: updatedProject});
    }
  }
</script>

<style scoped>
</style>