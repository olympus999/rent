<template>
    <router-view></router-view>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import { store } from '@/store';
  import { readHasClientAccess } from '@/store/main/getters';

  const routeGuardClient = async (to, from, next) => {
    if (!readHasClientAccess(store)) {
      next('/main');
    } else {
      next();
    }
  };

  @Component
  export default class Client extends Vue {
    public beforeRouteEnter(to, from, next) {
      routeGuardClient(to, from, next);
    }

    public beforeRouteUpdate(to, from, next) {
      routeGuardClient(to, from, next);
    }
  }
</script>
