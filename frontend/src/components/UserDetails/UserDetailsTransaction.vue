<template>
  <ValidationObserver v-slot="{ invalid }" ref="provider">
    <v-card class="ma-3 pa-3">
      <v-data-table :headers="headers" :items="accountingTransactions" :sort-by="['created_dt']" :sort-desc="[true]">
        <template v-slot:top>
          <v-container>
            <v-row class="mb-6">
              <v-toolbar-title>Accounting transactions</v-toolbar-title>
            </v-row>
            <v-row align="center">
              <v-dialog v-model="dialog" persistent max-width="600px">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn color="primary" dark v-bind="attrs" v-on="on">Add</v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="headline">Add transaction</span>
                  </v-card-title>
                  <v-card-text>
                    <ValidationProvider rules="required" v-slot="{ errors, valid }">
                      <v-text-field label="Amount" v-model.number="createTransaction.amount" :success="valid" :error-messages="errors">
                      </v-text-field>
                    </ValidationProvider>
                    <v-text-field label="Comment" v-model.number="createTransaction.comment">
                    </v-text-field>
                    <ValidationProvider rules="required" v-slot="{ errors, valid }">
                      <v-select  label="Transaction type"
                                 :items="accountingTransactionTypes"
                                 v-model="createTransaction.type_id"
                                 item-text="name"
                                 item-value="id"
                                 shrink
                      >
                      </v-select>
                    </ValidationProvider>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                    <v-btn color="blue darken-1" text @click="submit" :disabled="invalid">OK</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-row>
          </v-container>
        </template>
        <template v-slot:item.created_dt="{ item }">
          <data-table-date-column :dt="item.created_dt"></data-table-date-column>
        </template>
      </v-data-table>
    </v-card>
  </ValidationObserver>
</template>

<script lang="ts">
  import {Vue, Component} from 'vue-property-decorator';
  import {
    dispatchCreateAccountingTransaction,
    dispatchGetUserAccountingTransaction,
    dispatchGetUserAccountingTransactionTypes
  } from '@/store/admin/actions';
  import {readAdminUserAccountingTransactions, readAdminUserAccountingTransactionTypes} from '@/store/admin/getters';
  import {IAccountingTransactionCreate} from '@/interfaces/AccountingTransaction';
  import DataTableDateColumn from '@/components/DataTableDateColumn.vue';

  const UserDetailsTransactionProps = Vue.extend({
    props: {
      userId: {type: Number}
    }
  });

  @Component({
    components: {DataTableDateColumn}
  })
  export default class UserDetailsTransaction extends UserDetailsTransactionProps {
    public headers = [
      {
        text: 'ID',
        sortable: true,
        value: 'id',
        align: 'left',
        width: '30'
      },
      {
        text: 'Amount',
        sortable: true,
        value: 'amount',
        align: 'left',
        width: '100'
      },
      {
        text: 'Created',
        sortable: true,
        value: 'created_dt',
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

    public dialog = false;
    public createTransaction: IAccountingTransactionCreate = {} as IAccountingTransactionCreate

    async mounted() {
      await this.refresh()
    }

    async submit() {
      if (await dispatchCreateAccountingTransaction(this.$store, {accountingTransaction: this.createTransaction})){
        await this.refresh()
        this.close()
      }
    }

    close () {
      this.dialog = false;
      this.createTransaction = {} as IAccountingTransactionCreate
    }

    async refresh() {
      await dispatchGetUserAccountingTransaction(this.$store, {userId: this.userId})
      await dispatchGetUserAccountingTransactionTypes(this.$store)
      this.createTransaction = {} as IAccountingTransactionCreate
      this.createTransaction.user_id = this.userId
    }

    get accountingTransactionTypes() {
      return readAdminUserAccountingTransactionTypes(this.$store)
    }

    get accountingTransactions() {
      return readAdminUserAccountingTransactions(this.$store)
    }
  }
</script>

<style scoped>

</style>