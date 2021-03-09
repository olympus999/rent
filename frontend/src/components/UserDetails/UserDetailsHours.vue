<template>
  <v-card class="ma-3 pa-3">
    <v-data-table :headers="headers" :items="accountingHours">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Accounting hours</v-toolbar-title>
          <v-divider
                  class="mx-4"
                  inset
                  vertical
          ></v-divider>
          <span class="mr-4">Start Date</span>
          <v-menu
                  ref="menuMin"
                  v-model="menuMinDate"
                  :close-on-content-click="false"
                  :return-value.sync="minDateStr"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                      v-model="minDateStr"
                      label="Start date"
                      prepend-icon="mdi-calendar"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      class="shrink"
              ></v-text-field>
            </template>
            <v-date-picker
                    v-model="minDateStr"
                    no-title
                    scrollable
            >
              <v-spacer></v-spacer>
              <v-btn
                      text
                      color="primary"
                      @click="menuMinDate = false"
              >
                Cancel
              </v-btn>
              <v-btn
                      text
                      color="primary"
                      @click="$refs.menuMin.save(minDateStr)"
              >
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>
          <span class="mr-4 ml-6">End Date</span>
          <v-menu
                  ref="menuMax"
                  v-model="menuMaxDate"
                  :close-on-content-click="false"
                  :return-value.sync="maxDateStr"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                      v-model="maxDateStr"
                      label="End date"
                      prepend-icon="mdi-calendar"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      class="shrink"
              ></v-text-field>
            </template>
            <v-date-picker
                    v-model="maxDateStr"
                    no-title
                    scrollable
            >
              <v-spacer></v-spacer>
              <v-btn
                      text
                      color="primary"
                      @click="menuMaxDate = false"
              >
                Cancel
              </v-btn>
              <v-btn
                      text
                      color="primary"
                      @click="$refs.menuMax.save(maxDateStr)"
              >
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>
        </v-toolbar>
      </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">
  import {Component, Vue, Watch} from 'vue-property-decorator';
  import {dispatchGetProjectWorkersAssociatedWithUser, dispatchGetUserAccountingHour} from '@/store/admin/actions';
  import {readAdminProjectWorkersAssociatedWithUser, readAdminUserAccountingHours} from '@/store/admin/getters';

  const UserDetailsHoursProps = Vue.extend({
    props: {
      userId: {type: Number}
    }
  });

  @Component
  export default class UserDetailsHours extends UserDetailsHoursProps {

    public minDateStr = '';
    public maxDateStr = '';
    public overlay = false;
    public menuMinDate = false;
    public menuMaxDate = false;
    public headers = [
      {
        text: 'ID',
        sortable: true,
        value: 'id',
        align: 'left',
        width: '100'
      },
      {
        text: 'Project Name',
        sortable: true,
        value: 'project.name',
        align: 'left',
        width: '100'
      },
      {
        text: 'Day',
        sortable: true,
        value: 'day',
        align: 'left',
        width: '100'
      },
      {
        text: 'Hours',
        sortable: true,
        value: 'hour_count',
        align: 'left',
        width: '100'
      },
      {
        text: 'Per hour cost',
        sortable: true,
        value: 'per_hour_cost',
        align: 'left',
        width: '100'
      },
      {
        text: 'Comment',
        sortable: true,
        value: 'comment',
        align: 'left',
        width: '100'
      },
    ]

    async mounted() {
      const maxDate = new Date();
      const minDate = new Date();
      minDate.setMonth(minDate.getMonth() - 1);
      console.log('diff', maxDate.getTime()-minDate.getTime())

      this.minDateStr = `${minDate.getFullYear()}-${minDate.getMonth()+1}-${minDate.getDate()}`
      this.maxDateStr = `${maxDate.getFullYear()}-${maxDate.getMonth()+1}-${maxDate.getDate()}`

      await dispatchGetProjectWorkersAssociatedWithUser(this.$store, {userId: this.userId})
      await this.refreshHours()
    }

    @Watch('minDateStr')
    async refreshHours() {
      console.log('trigger watcher')
      await dispatchGetUserAccountingHour(this.$store, {userId: this.userId, minDate: this.minDateStr, maxDate: this.maxDateStr });
    }

    get projectWorkersAssociatedWithUser() {
      return readAdminProjectWorkersAssociatedWithUser(this.$store)
    }

    get accountingHours() {
      return readAdminUserAccountingHours(this.$store)
    }

  }
</script>

<style scoped>

</style>
