<template>
  <p>{{this.formatDate(dt)}}</p>
</template>

<script lang="ts">
  import {Vue, Component} from 'vue-property-decorator';

  const DataTableDateColumnProps = Vue.extend({
    props: {
      dt: String,
    }
  });

  @Component
  export default class DataTableDateColumn extends DataTableDateColumnProps {
    formatDate(d: string) {
      return d.replace('T', ' ').replace(/\.(.*)/, ' ')
    }
  }
</script>

<style scoped>

</style>