<template>
  <v-card class="ma-3 pa-3">
    <v-data-table :headers="headers" :items="userTools" :sort-by="['created_dt']" :sort-desc="[true]">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>User Tools</v-toolbar-title>
          <v-divider
                  class="mx-4"
                  inset
                  vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
                  v-model="dialog"
                  max-width="500px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                      color="primary"
                      dark
                      class="mb-2"
                      v-bind="attrs"
                      v-on="on"
              >
                Add tool
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                            cols="12"
                            sm="6"
                            md="10"
                    >
                      <v-select
                              v-model="editedItem.tool_id"
                              item-value="id"
                              item-text="name"
                              :items="tools"
                              label="Tool name"
                      ></v-select>
                      <v-text-field
                              v-model="editedItem.details"
                              label="Details"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                        color="blue darken-1"
                        text
                        @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                        color="blue darken-1"
                        text
                        @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="600px">
            <v-card>
              <v-card-title class="headline">Are you sure you want to delete tool named <br>"{{editedItem.name}}"?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon
                small
                class="mr-2"
                @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
                small
                @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import {
    dispatchCreateTool,
    dispatchCreateUserTool, dispatchDeleteTool,
    dispatchGetTools,
    dispatchGetUserInfo, dispatchRemoveUserTool,
    dispatchUpdateTool,
    dispatchUpdateUserTool,
    dispatchGetUserTools
  } from '@/store/admin/actions';
  import {readAdminTools, readAdminUserInfo, readAdminUserTools} from '@/store/admin/getters';
  import {IUserTool} from '@/interfaces';

  const UserDetailsToolsProps = Vue.extend({
    props: {
      userId: {type: Number}
    }
  });

  @Component
  export default class UserDetailsTools extends UserDetailsToolsProps {

    public dialog = false;
    public dialogDelete = false;
    public headers = [
      {
        text: 'Tool name',
        sortable: true,
        value: 'tool.name',
        align: 'left',
        width: '100'
      },
      {
        text: 'Details',
        sortable: true,
        value: 'details',
        align: 'left',
        width: '100'
      },
      {
        text: 'Actions',
        value: 'actions',
      }
    ]

    public defaultItem: IUserTool = {
      id: -1,
      user_id: this.userId,
      tool_id: -1,
      details: '',
    };

    public editedItem: IUserTool = {
      id: -1,
      user_id: this.userId,
      tool_id: -1,
      details: '',
    };

    public async mounted() {
      await this.reset();
    }

    public async reset() {
      await dispatchGetTools(this.$store);
      await dispatchGetUserTools(this.$store, {userId: this.userId});
    }

    public async editItem (item) {
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    };

    public close () {
      this.editedItem = Object.assign({}, this.defaultItem)
      this.dialog = false
    };

    public async save () {
      if (this.editedItem.id > -1) {
        await dispatchUpdateUserTool(this.$store, {userTool: this.editedItem})
      } else {
        await dispatchCreateUserTool(this.$store, {userTool: this.editedItem})
      }
      this.close()
      await this.reset()
    };

    public closeDelete () {
      this.editedItem = Object.assign({}, this.defaultItem)
      this.dialogDelete = false
    };

    public async deleteItem (item) {
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    };

    public async deleteItemConfirm () {
      await dispatchRemoveUserTool(this.$store, {userToolId: this.editedItem.id})
      this.closeDelete()
      await this.reset()
    };

    get userTools() {
      return readAdminUserTools(this.$store)
    }

    get tools() {
      return readAdminTools(this.$store)
    }

    get formTitle () {
      return this.editedItem.id > -1 ? 'Edit user tool' : 'Add user tool'
    };

  }
</script>

<style scoped>

</style>