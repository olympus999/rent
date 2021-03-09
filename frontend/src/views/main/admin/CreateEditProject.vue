<template>
  <ValidationObserver v-slot="{ invalid }" ref="provider">
    <v-container fluid>
      <v-card class="ma-3 pa-3">
        <v-card-title primary-title>
          <div v-if="project" class="headline primary--text">Edit project</div>
          <div v-else class="headline primary--text">Create project</div>
        </v-card-title>
        <v-card-text>
          <template>
            <v-form ref="form" :disabled="isDisabled()" lazy-validation>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <v-text-field label="Name" v-model="name" :error-messages="errors" :success="valid"></v-text-field>
              </ValidationProvider>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <v-select label="Client" v-model="userId" :items="clients" item-value="id" :item-text="fullNameAndEmail"
                          :disabled="!!project"
                          :error-messages="errors" :success="valid">
                </v-select>
              </ValidationProvider>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <address-auto-complete label="Address" v-model="address" :success="valid" :error-messages="errors">
                </address-auto-complete>
              </ValidationProvider>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <v-text-field label="Description" v-model="description" :error-messages="errors"
                              :success="valid"></v-text-field>
              </ValidationProvider>
            </v-form>
            <project-add-workers v-on:handle-add-workers="handleAddWorkers"
                                 :projectWorker="projectWorker"
                                 :disabled="isDisabled()"></project-add-workers>
          </template>
        </v-card-text>
        <v-data-table :headers="headers" :items="projectWorker" :item-class="row_classes" class="elevation-1">
          <template v-slot:item.worker_accepted_dt="{ item }">
            <div v-if="item.worker_accepted_dt === true">
              Just now
            </div>
            <div v-else>
              {{ item.worker_accepted_dt }}
            </div>
          </template>
          <template v-slot:item.accept_worker="{ item }">
            <div v-if="!item.worker_accepted_dt && !item.removed_dt">
              <div v-if="isWorkerAvailable(item)">
                <v-btn @click="acceptWorker(item)" :disabled="isDisabled()">
                  Accept worker
                </v-btn>
              </div>
              <div v-else>
                <v-btn slot="activator" text :to="{name: 'main-admin-projects-edit',
                params: {id: item.worker.project_worker_active.project_worker.project.id}}">
                  Project
                  <v-icon small class="mr-2">
                    mdi-pencil
                  </v-icon>
                </v-btn>
              </div>
            </div>
          </template>
          <template v-slot:item.removed_dt="{ item }">
            <div v-if="item.removed_dt === true">
              Just now
            </div>
            <div v-else>
              {{ item.removed_dt }}
            </div>
          </template>
          <template v-slot:item.remove="{ item }">
            <div v-if="item.removed_dt">
              <v-btn @click="undoRemoveWorker(item)" :disabled="isDisabled()">
                Undo
              </v-btn>
            </div>
            <div v-else>
              <v-btn @click="removeWorker(item)" :disabled="isDisabled()">
                Remove
              </v-btn>
            </div>
          </template>
          <template v-slot:item.feedback="{ item }">
            <div v-if="item.user_feedback">
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs"
                       v-on="on">
                    <v-rating
                            v-model="item.user_feedback.rating"
                            color="yellow darken-3"
                            background-color="grey darken-1"
                            empty-icon="$ratingFull"
                            hover
                            large
                            readonly
                    ></v-rating>
                  </div>
                </template>
                <span>Comment: {{item.user_feedback.comment}}</span>
              </v-tooltip>
            </div>
            <div v-else>
              <project-add-user-feedback
                      v-on:refresh-data="reset"
                      :feedbackReceivedUserId="item.worker.id"
                      :projectWorkerId="item.id"
                      :userFirstName="item.worker.first_name"
                      :userLastName="item.worker.last_name"
              ></project-add-user-feedback>
            </div>
          </template>
        </v-data-table>
        <v-card-actions>
          <v-btn v-if="project" @click="removeProject" :disabled="isDisabled()">Remove</v-btn>
          <v-spacer></v-spacer>
          <v-btn @click="cancel" :disabled="isDisabled()">Cancel</v-btn>
          <v-btn @click="reset" :disabled="isDisabled()">Reset</v-btn>
          <v-btn @click="submit" :disabled="(invalid || isDisabled())">
            <div v-if="project">Update</div>
            <div v-else>Create</div>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </ValidationObserver>
</template>

<script lang="ts">
  import {Component, Vue, Watch} from 'vue-property-decorator';
  import {
    dispatchGetClients,
    dispatchGetProjects, dispatchGetRemovedProjects,
    dispatchRemoveProject,
    dispatchUpdateProject
  } from '@/store/admin/actions';
  import {readAdminClients, readAdminOneProject} from '@/store/admin/getters';
  import {
    IProject,
    IProjectAdminCreateUpdate, IProjectWorker,
    IProjectWorkerAdminCreateUpdate,
    IUserProfile,
    IWorkerProfile,
    IWorkerProfileAdminUpdate
  } from '@/interfaces';
  import ProjectAddWorkers from '@/views/main/admin/modals/ProjectAddWorkers.vue';
  import ProjectAddUserFeedback from '@/views/main/admin/modals/ProjectAddUserFeedback.vue'
  import AddressAutoComplete from '@/components/AddressAutoComplete.vue';
  import {dispatchCreateProject} from '@/store/admin/actions';

  const CreateEditProjectProps = Vue.extend({
    props: {
      create: Boolean
    }
  })

  @Component({
    components: {AddressAutoComplete, ProjectAddWorkers, ProjectAddUserFeedback}
  })
  export default class CreateEditProject extends CreateEditProjectProps {
    public projectId: number | null = null;
    public userId: number | null = null;
    public name: string = '';
    public address: string = '';
    public description: string = '';
    public projectWorker: IProjectWorkerAdminCreateUpdate[] = [];
    public removedDt: Date | null = null;

    public headers = [
      {
        text: 'First name',
        sortable: true,
        value: 'worker.first_name',
        align: 'left',
      },
      {
        text: 'Last name',
        sortable: true,
        value: 'worker.last_name',
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
      },
      {
        text: 'Feedback',
        sortable: true,
        value: 'feedback',
        align: 'left',
      },
    ];


    public async mounted() {
      await this.reset();
    }

    // Make sure component is reloaded when certain changes happen
    @Watch('$route.params.id', {immediate: true})
    async onChangeURLId(oldValue: any, newValue: any) {
      await this.reset()
    }

    // Make sure component is reloaded when certain changes happen
    @Watch('create', {immediate: true})
    async onChange(oldValue: any, newValue: any) {
      await this.reset()
    }

    public cancel() {
      this.$router.back();
    }

    public async removeProject() {
      await dispatchRemoveProject(this.$store,{ projectId: this.project!.id })
    }

    public async handleAddWorkers(workers: IWorkerProfileAdminUpdate[]) {
      workers.forEach((worker) => {
        const projectWorker: IProjectWorkerAdminCreateUpdate = {
          user_id: worker.id,
          removed_dt: null,
          worker_accepted_dt: null,
          worker,
        };
        this.projectWorker.push(projectWorker);
      });
    }

    public async acceptWorker(item: IProjectWorker) {
      item.worker_accepted_dt = true;
    }

    public async undoRemoveWorker(item: IProjectWorker) {
      item.removed_dt = null;
    }

    public async removeWorker(item: IProjectWorker) {
      item.removed_dt = true;
      item.worker_accepted_dt = null;
    }

    public isDisabled(){
      return !!this.removedDt
    }

    public isWorkerAvailable(item){
      return !item.worker.project_worker_active
    }

    public async reset() {
      await dispatchGetProjects(this.$store);
      await dispatchGetRemovedProjects(this.$store);
      await dispatchGetClients(this.$store);
      if (this.project) {
        this.name = this.project.name;
        this.projectId = this.project.id;
        this.userId = this.project.user_id;
        this.address = this.project.address;
        this.description = this.project.description;
        this.projectWorker = this.project.project_worker;
        this.removedDt = this.project.removed_dt;
      } else {
        this.name = ''
        this.projectId = null
        this.userId = null
        this.address = ''
        this.description = ''
        this.projectWorker = []
      }
    }

    public fullNameAndEmail(item: IUserProfile) {
      return item.first_name + ' ' + item.last_name + ' (' + item.email + ')'
    }

    get project() {
      return readAdminOneProject(this.$store)(+this.$router.currentRoute.params.id);
    }

    get clients() {
      return readAdminClients(this.$store)
    }

    row_classes(item: IProjectWorker) {
      if (item.removed_dt) {
        return 'background-red';
      } else if (item.worker_accepted_dt) {
        return 'background-green'
      }
    }

    public async submit() {
      const currentProject: IProjectAdminCreateUpdate = {};
      if (this.projectId) {
        currentProject.id = this.projectId;
      }
      if (this.userId) {
        currentProject.user_id = this.userId;
      }
      if (this.name) {
        currentProject.name = this.name;
      }
      if (this.address) {
        currentProject.address = this.address;
      }
      if (this.description) {
        currentProject.description = this.description;
      }
      if (this.projectWorker) {
        const projectWorkerCopy = JSON.parse(JSON.stringify(this.projectWorker))
        projectWorkerCopy.forEach((item, index) => {
          if(item.removed_dt === true) {
            item.removed_dt = Date.now();
          }
          if(item.worker_accepted_dt === true) {
            item.worker_accepted_dt = Date.now();
          }
          projectWorkerCopy[index] = item
        })
        currentProject.project_worker = projectWorkerCopy;
      }
      if (this.project) {
        const res = await dispatchUpdateProject(this.$store, {id: this.project!.id, project: currentProject});
        if (res) {
          await this.reset();
        }
      } else {
        await dispatchCreateProject(this.$store, {project: currentProject})
      }
      // await this.reset();
    }
  }
</script>

<style scoped>
</style>