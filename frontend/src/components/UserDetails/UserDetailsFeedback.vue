<template>
  <v-card class="ma-3 pa-3">
    <v-data-table :headers="headers" :items="user.user_feedback" :sort-by="['created_dt']" :sort-desc="[true]">>
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Feedback</v-toolbar-title>
        </v-toolbar>
      </template>
      <template v-slot:item.rating="{ item }">
        <v-rating
                v-model="item.rating"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                hover
                large
                readonly
        ></v-rating>
      </template>
      <template v-slot:item.project_worker="{ item }">
        <v-btn slot="activator" text :to="{name: 'main-admin-projects-edit', params: {id: item.project_worker.project.id}}">
          <div> {{item.project_worker.project.name }} </div>
          <v-icon small class="mr-2">
            mdi-pencil
          </v-icon>
        </v-btn>
      </template>
      <template v-slot:item.feedback_given_user_id="{ item }">
        <v-btn slot="activator" text :to="{name: 'main-admin-users-edit', params: {id: item.feedback_given_user_id}}">
          <v-icon small class="mr-2">
            mdi-pencil
          </v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">

  import {Component, Vue} from 'vue-property-decorator';
  import {dispatchGetUserInfo} from '@/store/admin/actions';
  import {readAdminUserInfo} from '@/store/admin/getters';

  const UserDetailsFeedbackProps = Vue.extend({
    props: {
      userId: {type: Number}
    }
  });

  @Component
  export default class UserDetailsFeedback extends UserDetailsFeedbackProps {
    public headers = [
      {
        text: 'Comment',
        sortable: true,
        value: 'comment',
        align: 'left',
        width: '100'
      },
      {
        text: 'Rating',
        sortable: true,
        value: 'rating',
        align: 'left',
        width: '100'
      },
      {
        text: 'Created',
        sortable: true,
        value: 'created_dt',
        width: '100'
      },
      {
        text: 'Edit project',
        sortable: true,
        value: 'project_worker',
        width: '100'
      },
      {
        text: 'Feedback given by',
        sortable: true,
        value: 'feedback_given_user_id',
        width: '100'
      },
    ];

    public async mounted() {
      await dispatchGetUserInfo(this.$store, {userId: this.userId});
    }

    get user() {
      return readAdminUserInfo(this.$store)
    }
  }
</script>
<style scoped>

</style>