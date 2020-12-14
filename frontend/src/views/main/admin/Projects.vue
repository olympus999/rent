<template>
    <div>
        <v-data-table :headers="headers" :items="projects">
            <template v-slot:item.actions="{ item }">
                <v-btn slot="activator" text :to="{name: 'main-admin-projects-edit', params: {id: item.id}}">
                    <v-icon small class="mr-2">
                        mdi-pencil
                    </v-icon>
                </v-btn>
            </template>
        </v-data-table>
    </div>
</template>

<script lang="ts">
    import {Component, Vue} from 'vue-property-decorator';
    import { dispatchGetProjects } from '@/store/admin/actions'
    import { readAdminProjects } from '@/store/admin/getters';
    @Component
    export default class Projects extends Vue {
      public headers = [
        {
          text: 'Project name',
          sortable: true,
          value: 'name',
          align: 'left',
        },
        {
          text: 'Address',
          sortable: true,
          value: 'address',
          align: 'left',
        },
        {
          text: 'Created',
          sortable: true,
          value: 'created_dt',
          align: 'left',
        },
        {
          text: 'Actions',
          sortable: false,
          value: 'actions',
          align: 'left',
        }
      ];

        get projects() {
            return readAdminProjects(this.$store);
        }
        public async mounted() {
          await dispatchGetProjects(this.$store)
        }
    }
</script>

<style scoped>

</style>