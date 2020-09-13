<template>
  <ValidationObserver v-slot="{ invalid }" ref="provider">
    <v-container fluid>
      <v-card class="ma-3 pa-3">
        <v-card-title primary-title>
          <div class="headline primary--text">Create User</div>
        </v-card-title>
        <v-card-text>
          <template>
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
                  <ValidationObserver>
                    <ValidationProvider name="password1" rules="required" v-slot="{ errors, valid }">
                      <v-text-field type="password" label="Set Password" v-model="password1"  :error-messages="errors"
                                    :success="valid"></v-text-field>
                    </ValidationProvider>
                    <ValidationProvider name="password2" rules="required|duplicate:@password1" v-slot="{ errors, valid }">
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
import {
  IUserProfile,
  IUserProfileUpdate,
  IUserProfileCreate,
} from '@/interfaces';
import {dispatchGetUsers, dispatchCreateUser, dispatchGetUsersRoles} from '@/store/admin/actions';
import {readUsersRolesNames} from '@/store/admin/getters';

@Component
export default class CreateUser extends Vue {
  public usersRolesNames: string[] = [];
  public firstName: string = '';
  public lastName: string = '';
  public email: string = '';
  public isActive: boolean = true;
  public userRole: string = '';
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
    this.firstName = '';
    this.lastName = '';
    this.email = '';
    this.isActive = true;
    this.userRole = 'isWorker';
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    const updatedProfile: IUserProfileCreate = {
      email: this.email,
    };
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
    updatedProfile.role = this.userRole;
    updatedProfile.password = this.password1;
    await dispatchCreateUser(this.$store, updatedProfile);
    this.$router.push('/main/admin/users');
  }
}
</script>
