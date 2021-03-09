<template>
  <ValidationObserver v-slot="{ invalid }" ref="provider">
    <v-container fluid>
      <v-card class="ma-3 pa-3" max-width="700">
        <v-card-title primary-title>
          <div class="headline primary--text">Edit User</div>
        </v-card-title>
        <v-card-text>
          <template>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">Username</div>
              <div
                class="title primary--text text--darken-2"
                v-if="user"
              >{{user.email}}</div>
              <div
                class="title primary--text text--darken-2"
                v-else
              >-----</div>
            </div>
            <v-form ref="form" lazy-validation>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <v-text-field label="First Name" v-model="firstName" :error-messages="errors" :success="valid"></v-text-field>
              </ValidationProvider>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <v-text-field label="Last Name" v-model="lastName" :error-messages="errors" :success="valid"></v-text-field>
              </ValidationProvider>
              <ValidationProvider rules="required|email" v-slot="{ errors, valid }">
                <v-text-field label="E-mail" type="email" v-model="email" :error-messages="errors" :success="valid"></v-text-field>
              </ValidationProvider>
              <ValidationProvider rules="required" v-slot="{ errors, valid }">
                <v-select :items="usersRolesNames" item-text="name" v-model="role" label="User Role"
                          :error-messages="errors" :success="valid" outlined>
                </v-select>
              </ValidationProvider>
              <v-layout align-center>
                <v-flex>
                  <ValidationObserver v-slot="{ dirty }">
                    <ValidationProvider name="password1" :rules="{'required':dirty, min: { length: 6 }}" v-slot="{ errors, valid }">
                      <v-text-field type="password" label="Set Password" v-model="password1"  :error-messages="errors"
                                    :success="valid"></v-text-field>
                    </ValidationProvider>
                    <ValidationProvider name="password2" :rules="{'required':dirty, min: { length: 6 }, 'duplicate': password1}" v-slot="{ errors, valid }">
                      <v-text-field type="password" label="Confirm Password" data-vv-as="password" v-model="password2"
                                    :error-messages="errors" :success="valid"></v-text-field>
                    </ValidationProvider>
                  </ValidationObserver>
                </v-flex>
              </v-layout>
              <v-checkbox
                      label="Is Active"
                      v-model="isActive"
              ></v-checkbox>
              <v-checkbox
                      label="Is Available"
                      v-model="available"
              ></v-checkbox>
            </v-form>
          </template>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="cancel">Cancel</v-btn>
          <v-btn @click="reset">Reset</v-btn>
          <v-btn @click="submit" :disabled="invalid"> Save </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </ValidationObserver>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { IUserProfile, IUserProfileUpdate, IUserRole } from '@/interfaces';
import { dispatchGetUsers, dispatchUpdateUser, dispatchGetUsersRoles } from '@/store/admin/actions';
import { readAdminOneUser, readUsersRolesNames } from '@/store/admin/getters';

@Component
export default class EditUser extends Vue {
  public usersRolesNames: string[] = [];
  public firstName: string = '';
  public lastName: string = '';
  public email: string = '';
  public isActive: boolean = true;
  public role: string = '';
  public available: boolean = true;
  public password1: string = '';
  public password2: string = '';

  public async mounted() {
    await dispatchGetUsers(this.$store);
    await dispatchGetUsersRoles(this.$store)
    this.usersRolesNames = await readUsersRolesNames(this.$store)
    this.reset();
  }

  public reset() {
    this.password1 = '';
    this.password2 = '';
    if (this.user) {
      this.firstName = this.user.first_name;
      this.lastName = this.user.last_name;
      this.email = this.user.email;
      this.isActive = this.user.is_active;
      this.role = this.user.role;
      this.available = this.user.available
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    const updatedProfile: IUserProfileUpdate = {};
    if (this.firstName) {
      updatedProfile.first_name = this.firstName;
    }
    if (this.lastName) {
      updatedProfile.last_name = this.lastName;
    }
    if (this.email) {
      updatedProfile.email = this.email;
    }
    updatedProfile.is_active = this.isActive;
    updatedProfile.available = this.available;
    updatedProfile.role = this.role;
    if (this.password1) {
      updatedProfile.password = this.password1;
    }
    await dispatchUpdateUser(this.$store, { id: this.user!.id, user: updatedProfile });
    this.$router.push('/main/admin/users');
  }

  get user() {
    return readAdminOneUser(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
