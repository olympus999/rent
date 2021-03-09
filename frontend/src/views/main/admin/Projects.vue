<template>
    <div>
        <v-data-table :headers="headers" :items="projects" :sort-by="['created_dt']" :sort-desc="[true]">
            <template v-slot:item.edit="{ item }">
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
    import {dispatchGetProjects, dispatchGetRemovedProjects} from '@/store/admin/actions';
    import { readAdminProjects, readAdminRemovedProjects } from '@/store/admin/getters';

    const ProjectProps = Vue.extend({
      props: {
        showRemovedProjects: {type: Boolean, default: false}
      }
    })

    @Component
    export default class Projects extends ProjectProps {
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
          text: 'Edit',
          sortable: false,
          value: 'edit',
          align: 'left',
        }
      ];

        get projects() {
          if (this.showRemovedProjects) {
            return readAdminRemovedProjects(this.$store)
          }
            return readAdminProjects(this.$store);
        }
        public async mounted() {
          if (this.showRemovedProjects) {
            await dispatchGetRemovedProjects(this.$store)
          } else {
            await dispatchGetProjects(this.$store)
          }
        }
    }
</script>

<style scoped>

</style>