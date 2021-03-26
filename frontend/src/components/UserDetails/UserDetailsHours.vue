<template>
  <v-card class="ma-3 pa-3">
    <v-data-table :headers="headers" :items="accountingHours" :items-per-page=30 :custom-sort="customSortDay" :sort-desc="[true]">
      <template v-slot:top>
          <v-container>
            <v-row class="mb-6">
              <v-toolbar-title>Accounting hours</v-toolbar-title>
            </v-row>
            <v-row align="center">
              <p class="mr-4">Start Date</p>
              <v-menu
                      ref="menuMin"
                      v-model="menuMinDate"
                      :close-on-content-click="false"
                      :return-value.sync="minDateStr"
                      transition="scale-transition"
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
              <p class="mr-4 ml-6">End Date</p>
              <v-menu
                      ref="menuMax"
                      v-model="menuMaxDate"
                      :close-on-content-click="false"
                      :return-value.sync="maxDateStr"
                      transition="scale-transition"
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
              <v-btn @click="fillWorkdays" class="ml-10">Fill workdays</v-btn>
            </v-row>
            <v-row align="center">
              <p class="mr-4">Project: </p>
              <v-select :items="projectWorkersAssociatedWithUser"
                        item-text="project.name"
                        item-value="project.id"
                        v-model="globalSelectedProjectId"
                        class="shrink"
              ></v-select>
              <v-btn @click="setProject" class="ml-10">Set Project</v-btn>
            </v-row>
            <v-row>
              <p class="mr-4">Per hour cost: </p>
              <v-text-field
                      v-model.number="globalPerHourCost"
                      name="Hour"
                      type="number"
                      class="shrink"
              ></v-text-field>
              <v-btn @click="setPerHourCost" class="ml-10">Set per hour</v-btn>
            </v-row>
            <v-row>
              <v-btn @click="saveAccountingHours" class="ml-10">Save changes</v-btn>
            </v-row>
          </v-container>
      </template>
      <template v-slot:item.project.name="props">
        <v-select :items="projectWorkersAssociatedWithUser"
                  item-text="project.name"
                  item-value="project.id"
                  v-model="props.item.project_id"
        ></v-select>
      </template>
      <template v-slot:item.day="props">
        <span>{{props.item.day}} {{getDayStringFromDate(props.item.day)}}</span>
      </template>
      <template v-slot:item.hour_count="props">
        <v-text-field
                v-model.number="props.item.hour_count"
                name="hour count"
                type="number"
        ></v-text-field>
      </template>
      <template v-slot:item.per_hour_cost="props">
        <v-text-field
                v-model.number="props.item.per_hour_cost"
                name="per hour cost"
                type="number"
        ></v-text-field>
      </template>
      <template v-slot:item.comment="props">
        <v-text-field
                v-model.text="props.item.comment"
                name="per hour cost"
                type="text"
        ></v-text-field>
      </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">
  import {Component, Vue, Watch} from 'vue-property-decorator';
  import {
    dispatchCreateUpdateAccountingHours,
    dispatchGetProjectWorkersAssociatedWithUser,
    dispatchGetUserAccountingHour
  } from '@/store/admin/actions';
  import {readAdminProjectWorkersAssociatedWithUser, readAdminUserAccountingHours} from '@/store/admin/getters';
  import {IAccountingHourCreateUpdate} from '@/interfaces/AccountingHour';
  import {commitAddNotification} from '@/store/main/mutations';

  const UserDetailsHoursProps = Vue.extend({
    props: {
      userId: {type: Number}
    }
  });

  @Component
  export default class UserDetailsHours extends UserDetailsHoursProps {

    public minDateStr: string = '';
    public maxDateStr: string = '';
    public overlay: boolean = false;
    public menuMinDate: boolean = false;
    public menuMaxDate: boolean = false;
    public accountingHours: IAccountingHourCreateUpdate[] = [];
    public globalSelectedProjectId: number = -1;
    public globalPerHourCost: number = 0
    public headers = [
      {
        text: 'ID',
        sortable: true,
        value: 'id',
        align: 'left',
        width: '30'
      },
      {
        text: 'Project Name',
        sortable: true,
        value: 'project.name',
        align: 'left',
        width: '180'
      },
      {
        text: 'Day',
        sortable: true,
        value: 'day',
        align: 'left',
        width: '130'
      },
      {
        text: 'Hours',
        sortable: true,
        value: 'hour_count',
        align: 'left',
        width: '90'
      },
      {
        text: 'Per hour cost',
        sortable: true,
        value: 'per_hour_cost',
        align: 'left',
        width: '90'
      },
      {
        text: 'Comment',
        sortable: true,
        value: 'comment',
        align: 'left',
        // width: '100'
      },
    ]

    async mounted() {
      const maxDate = new Date();
      const minDate = new Date();
      minDate.setTime(minDate.getTime() - 7*24*60*60*1000);
      // console.log('diff', maxDate.getTime()-minDate.getTime())

      this.minDateStr = this.formatDateForDay(minDate)
      this.maxDateStr = this.formatDateForDay(maxDate)

      await dispatchGetProjectWorkersAssociatedWithUser(this.$store, {userId: this.userId})
      await this.refreshHours()
    }

    get projectWorkersAssociatedWithUser() {
      return readAdminProjectWorkersAssociatedWithUser(this.$store)
    }

    get minMaxDateStr() {
      return `${this.minDateStr}|${this.maxDateStr}`;
    }

    @Watch('minMaxDateStr')
    async refreshHours() {
      await dispatchGetUserAccountingHour(this.$store, {userId: this.userId, minDate: this.minDateStr, maxDate: this.maxDateStr });
      await this.setAccountingHours()
    }

    async setAccountingHours() {
      this.accountingHours = readAdminUserAccountingHours(this.$store)
    }

    async fillWorkdays(){
      const existingDates: string[] = [];
      const filledWorkdays: IAccountingHourCreateUpdate[] = [];
      this.accountingHours.forEach((obj: IAccountingHourCreateUpdate) => {
        existingDates.push(obj.day)
      })
      const dates = await this.getDatesBetweenDates(
        new Date(this.minDateStr),
        new Date(this.maxDateStr)
      )
      if (dates.length > 30) {
        const loadingNotification = {content: 'Date range too wide! Must be below 30 days.', color: 'error'};
        commitAddNotification(this.$store, loadingNotification);
      } else {
        // console.log('existingDates', existingDates)
        // console.log('dates', dates)
        dates.forEach((dateStr) => {
          if (!existingDates.includes(dateStr)) {
            const accountingHour: IAccountingHourCreateUpdate = {
              user_id: this.userId,
              project_id: this.globalSelectedProjectId,
              day: dateStr,
              hour_count: 0,
              per_hour_cost: 0,
            }
            this.accountingHours.push(accountingHour)
          }
        })
      }
    }

    async checkIfValidAccountingHours(){
      try {
        this.accountingHours.forEach((obj: IAccountingHourCreateUpdate) => {
          if (obj.project_id < 0) throw Error()
          if (obj.user_id < 0) throw Error()
        });
      } catch (e) {
        return false
      }
      return true
    }

    async saveAccountingHours() {
      if (await this.checkIfValidAccountingHours()) {
        await dispatchCreateUpdateAccountingHours(this.$store, {accountingHours: this.accountingHours})
        await this.refreshHours()
      } else {
        const loadingNotification = {content: 'There is an issue with accounting hours, cannot save', color: 'error'};
        commitAddNotification(this.$store, loadingNotification);
      }
      // await dispatchCreateUpdateAccountingHours(this.$store, {accountingHours: this.accountingHours})
      // await this.refreshHours()
    }

    async setProject() {
      this.accountingHours.forEach((item: IAccountingHourCreateUpdate, idx: number) => {
        this.accountingHours[idx].project_id = this.globalSelectedProjectId
      })
    }

    async setPerHourCost() {
      this.accountingHours.forEach((item: IAccountingHourCreateUpdate, idx: number) => {
        this.accountingHours[idx].per_hour_cost = this.globalPerHourCost
      })
    }

    async getDatesBetweenDates(startDate: Date, endDate: Date, workdaysOnly: boolean = true): Promise<string[]> {
      let dates: string[] = []
      // to avoid modifying the original date
      const theDate = new Date(startDate)
      while (theDate <= endDate) {

        let addToDates: boolean = true
        if (workdaysOnly) {
          const day = theDate.getDay()
          if(day === 0 || day === 6) {
            addToDates = false
          }
        }

        if (addToDates) {
          const date = this.formatDateForDay(theDate)
          dates = [...dates, date]
        }

        theDate.setDate(theDate.getDate() + 1)
      }
      return dates
    }

    customSortDay(items: IAccountingHourCreateUpdate[], index, isDesc) {
      items.sort((a, b) => {
        if (!isDesc) {
          return new Date(a.day) < new Date(b.day) ? -1 : 1;
        } else {
          return new Date(b.day) < new Date(a.day) ? -1 : 1;
        }
        // if (index === "date") {
        //   if (!isDesc) {
        //     return dateHelp.compare(a.date, b.date);
        //   } else {
        //     return dateHelp.compare(b.date, a.date);
        //   }
        // } else {
        //   if (!isDesc) {
        //     return a[index] < b[index] ? -1 : 1;
        //   } else {
        //     return b[index] < a[index] ? -1 : 1;
        //   }
        // }
      });
      return items;
    }

    getDayStringFromDate(dateStr: string) {
      const date: Date = new Date(Date.parse(dateStr))
      const weekDay = new Array(7);
      weekDay[0] = 'Su'
      weekDay[1] = 'Mo'
      weekDay[2] = 'Tu'
      weekDay[3] = 'We'
      weekDay[4] = 'Th'
      weekDay[5] = 'Fr'
      weekDay[6] = 'Sa'
      return weekDay[date.getDay()]
    }

    formatDateForDay(date: Date) {
      return `${date.getFullYear()}-${('0'+(date.getMonth()+1)).slice(-2)}-${('0'+date.getDate()).slice(-2)}`
    }

  }
</script>

<style scoped>

</style>
