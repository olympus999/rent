<template>
  <v-card class="ma-3 pa-3" max-width="700">
    <v-card-title primary-title>
      <div class="headline primary--text">User Info</div>
    </v-card-title>
    <v-card-text>
      <template>
        <div class="my-3">
          <div class="subheading secondary--text text--lighten-2">Role</div>
          <div
                  class="title primary--text text--darken-2"
          >{{user.role}}</div>
          <div class="subheading secondary--text text--lighten-2">First Name</div>
          <div
                  class="title primary--text text--darken-2"
          >{{user.first_name}}</div>
          <div class="subheading secondary--text text--lighten-2">Last Name</div>
          <div
                  class="title primary--text text--darken-2"
          >{{user.last_name}}</div>
          <div class="subheading secondary--text text--lighten-2">Balance</div>
          <div
                  class="title primary--text text--darken-2"
          >{{balance}}</div>
        </div>
      </template>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import {dispatchGetUserAccountingBalanceByUser, dispatchGetUserInfo} from '@/store/admin/actions';
  import {readAdminUserAccountingBalance, readAdminUserInfo} from '@/store/admin/getters';

  const UserDetailsGeneralProps = Vue.extend({
    props: {
      userId: {type: Number}
    }
  });

  @Component
  export default class UsersDetailsGeneral extends UserDetailsGeneralProps {

    public async mounted() {
      await dispatchGetUserInfo(this.$store, {userId: this.userId});
      await dispatchGetUserAccountingBalanceByUser(this.$store, {userId: this.userId})
    }

    get user() {
      return readAdminUserInfo(this.$store)
    }

    get balance() {
      return readAdminUserAccountingBalance(this.$store).balance
    }

  }
</script>

<style scoped>

</style>