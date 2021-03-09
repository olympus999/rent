<template>
  <ValidationObserver v-slot="{ invalid }" ref="provider">
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" :disabled="typeof projectWorkerId === 'undefined'">
            Add feedback
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">Add feedback</span>
          </v-card-title>
          <v-card-text>
            <template>
              <div class="my-3">
                <div class="subheading secondary--text text--lighten-2">Receivers name</div>
                <div class="title primary--text text--darken-2"
                >{{userFirstName + " " + userLastName}}</div>
              </div>
              <v-form ref="form" lazy-validation>
                <ValidationProvider v-slot="{ errors, valid }">
                  <v-textarea label="Comment" v-model="comment" :error-messages="errors" :success="valid" auto-grow></v-textarea>
                </ValidationProvider>
                <ValidationProvider  rules="required" v-slot="{ errors, valid }">
                  <v-rating
                    v-model="rating"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    hover
                    large
                  ></v-rating>
                  <span id="error">{{ errors[0] }}</span>
                </ValidationProvider>
              </v-form>
            </template>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Close
            </v-btn>
            <v-btn @click="submit" :disabled="invalid">Submit</v-btn>
<!--            <v-btn color="blue darken-1" text @click="submit">-->
<!--              Add selected workers-->
<!--            </v-btn>-->
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </ValidationObserver>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import { IUserFeedbackCreate } from '@/interfaces';
  import {dispatchAddUserFeedback} from '@/store/admin/actions';

  const ProjectAddUserFeedbackProps = Vue.extend({
    props: {
      feedbackReceivedUserId: {
        type: Number,
        required: true
      },
      projectWorkerId: {
        type: Number,
      },
      userFirstName: {
        type: String,
        required: true
      },
      userLastName: {
        type: String,
        required: true
      },
    }
  })

  @Component
  export default class ProjectAddUserFeedback extends ProjectAddUserFeedbackProps {
    public rating: number = 0;
    public comment: string = '';
    public dialog: boolean = false;

    public async submit() {
      const userFeedbackCreate: IUserFeedbackCreate = {
        feedback_received_user_id: this.feedbackReceivedUserId,
        project_worker_id: this.projectWorkerId,
        rating: this.rating,
        comment: this.comment
      }
      await dispatchAddUserFeedback(this.$store,  { userFeedback: userFeedbackCreate })
      this.$emit('refresh-data', 'asd');
      this.dialog = false;
    }
  }
</script>

<style scoped>

</style>