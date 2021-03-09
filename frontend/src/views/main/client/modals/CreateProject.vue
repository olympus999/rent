<template>
    <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark v-bind="attrs" v-on="on">
                    Book selected workers
                </v-btn>
            </template>
            <v-card>
                <v-card-title>
                    <span class="headline">Project details</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12" sm="6" md="4">
                                <v-text-field label="Project Name" v-model="projectName" required></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4" >
                                <v-text-field label="Project Address" v-model="address" required
                                ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4" >
                                <v-text-field
                                        label="Description"
                                        v-model="description"
                                        hint="Description relevant to the project"
                                        persistent-hint
                                ></v-text-field>
                            </v-col>
                        </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="dialog = false">
                        Close
                    </v-btn>
                    <v-btn color="blue darken-1" text @click="submit">
                        Save
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import {IProjectCreate, IWorkerProfile} from '@/interfaces';
// import {dispatchCreateProject, dispatchGetWorkers} from '@/store/client/actions';

const CreateProjectProps = Vue.extend({
  props: {
    workers: Array  as () => IWorkerProfile[]
  }
})

@Component
export default class CreateProject extends CreateProjectProps {
    public dialog: boolean = false;
    public projectName: string = '';
    public address: string = '';
    public description: string = '';

  public async submit() {
    const projectObject: IProjectCreate = {
      name: this.projectName,
      address: this.address,
      description: this.description,
      user_id: this.$store.state.main.userProfile.id,
      workers: this.workers
    };

    // await dispatchCreateProject(this.$store, projectObject);
    // this.dialog = false;
    // await dispatchGetWorkers(this.$store);
  }
}

</script>
