<template>
  <v-data-table :headers="headers" :items="tools" class="elevation-1">
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Tools</v-toolbar-title>
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
              New Item
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
                    <v-text-field
                            v-model="editedItem.name"
                            label="Name"
                    ></v-text-field>
                    <v-text-field
                            v-model="editedItem.description"
                            label="Description"
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
</template>

<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import {dispatchCreateTool, dispatchDeleteTool, dispatchGetTools, dispatchUpdateTool} from '@/store/admin/actions';
  import {readAdminTools} from '@/store/admin/getters';
  import {ITool, IToolUpdate} from '@/interfaces';

  @Component
  export default class Tools extends Vue {

    public dialog = false;
    public dialogDelete = false;
    public headers = [
      {
        text: 'ID',
        sortable: true,
        value: 'id',
        align: 'left',
        width: '100'
      },
      {
        text: 'Name',
        sortable: true,
        value: 'name',
        align: 'left',
        width: '100'
      },
      {
        text: 'Description',
        sortable: true,
        value: 'description',
        align: 'left',
        width: '300'
      },
      {
        text: 'Actions',
        value: 'actions',
      }
    ];

    public defaultItem: ITool = {
      id: -1,
      name: '',
      description: '',
    };

    public editedItem: IToolUpdate = {
      id: -1,
      name: '',
      description: '',
    };

    public async mounted() {
      await this.reset();
    }

    public async reset() {
      await dispatchGetTools(this.$store);
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
        await dispatchUpdateTool(this.$store, {tool: this.editedItem})
      } else {
        await dispatchCreateTool(this.$store, {tool: this.editedItem})
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
      await dispatchDeleteTool(this.$store, {toolId: this.editedItem.id})
      this.closeDelete()
      await this.reset()
    };

    get tools() {
      return readAdminTools(this.$store)
    };

    get formTitle () {
      return this.editedItem.id > -1 ? 'Edit Item' : 'New Item'
    };

  }
</script>

<style scoped>

</style>