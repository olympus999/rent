<template>
    <div>
        <span>Test</span>
    </div>
</template>

<script lang="ts">
    import {Component, Vue} from 'vue-property-decorator';
    // import { dispatchGetProjects } from '@/store/client/actions'
    @Component
    export default class Projects extends Vue {
        public async mounted() {
          // await dispatchGetProjects(this.$store)
        }
    }
</script>

<style scoped>

</style>