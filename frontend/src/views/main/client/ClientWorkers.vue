<template>
    <div>
        <v-toolbar light>
            <v-toolbar-title>
                Book
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <create-project :workers="this.bookedWorkers" v-if="bookedWorkers.length > 0"></create-project>
<!--            <v-btn v-if="bookedWorkers.length > 0" color="primary">Book selected workers</v-btn>-->
        </v-toolbar>
        <v-data-table :headers="headers" :items="workers" show-select>
            <template v-slot:header.data-table-select>
<!--                Removing a way to select all at once     -->
            </template>
            <template v-slot:item.data-table-select="{ item, isSelected, select }">
                <div v-if="item.available">
                    <v-simple-checkbox
                                       :value="isSelected"
                                       @input="select($event)"
                                       :disabled="!item.available"
                                       @click="updateBookedWorkers(item, !isSelected)">
                    </v-simple-checkbox>
                </div>
            </template>
            <template v-slot:item.available="{ item }">
                <div v-if="item.available">
                    <v-icon large color="green darken-2"> mdi-circle-medium </v-icon>
                </div>
                <div v-else>
                    <v-icon large color="red darken-2"> mdi-circle-medium </v-icon>
                </div>
            </template>
        </v-data-table>
    </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import { Store } from 'vuex';
  import { IUserProfile } from '@/interfaces';
  import { readWorkers } from '@/store/client/getters';
  import {dispatchGetWorkers} from '@/store/client/actions';
  import CreateProject from '@/views/main/client/modals/CreateProject.vue';
  @Component({
    components: {CreateProject}
  })
  export default class Workers extends Vue {
    public bookedWorkers: IUserProfile[] = [];
    public headers = [
      {
        text: 'First Name',
        sortable: true,
        value: 'first_name',
        align: 'left',
        width: '100'
      },
      {
        text: 'Role',
        sortable: true,
        value: 'role',
        align: 'left',
        width: '100'
      },
      {
        text: 'Available',
        sortable: true,
        value: 'available',
        width: '100'
      },
      {
        text: 'ID',
        value: 'id',
        // width: '5'
      },
      // {
      //   text: 'Actions',
      //   sortable: false,
      //   value: 'actions',
      //   align: 'left',
      // },
    ];
    // set bookedWorkers() {
    //
    // }
    get workers() {
      return readWorkers(this.$store);
    }

    public async updateBookedWorkers(item, newValue) {
      if (newValue) {
        this.bookedWorkers.push(item)
      } else {
        this.bookedWorkers = this._.remove(this.bookedWorkers, (t) => t.id !== item.id)
      }
    }

    public async mounted() {
      await dispatchGetWorkers(this.$store);
    }
  }
</script>
