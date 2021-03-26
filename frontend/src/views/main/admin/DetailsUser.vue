<template>
  <v-container fluid>
    <user-details-general :userId="userId"></user-details-general>
    <user-details-feedback :userId="userId"></user-details-feedback>
    <user-details-tools :userId="userId"></user-details-tools>
    <user-details-hours :userId="userId"> </user-details-hours>
    <user-details-transaction :userId="userId"></user-details-transaction>
  </v-container>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import UserDetailsFeedback from '@/components/UserDetails/UserDetailsFeedback.vue';
  import UserDetailsGeneral from '@/components/UserDetails/UserDetailsGeneral.vue';
  import UserDetailsTools from '@/components/UserDetails/UserDetailsTools.vue';
  import UserDetailsHours from '@/components/UserDetails/UserDetailsHours.vue';
  import UserDetailsTransaction from '@/components/UserDetails/UserDetailsTransaction.vue';

  @Component({
    components: {UserDetailsFeedback, UserDetailsGeneral, UserDetailsTools, UserDetailsHours, UserDetailsTransaction}
  })
  export default class DetailsUser extends Vue {

    get userId() {
      return parseInt(this.$router.currentRoute.params.id, 10)
    }
  }
</script>

<style scoped>

</style>