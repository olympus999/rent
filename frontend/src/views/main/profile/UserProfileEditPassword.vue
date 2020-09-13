<template>
  <ValidationObserver v-slot="{ invalid }" ref="provider">
    <v-container fluid>
      <v-card class="ma-3 pa-3">
        <v-card-title primary-title>
          <div class="headline primary--text">Set Password</div>
        </v-card-title>
        <v-card-text>
          <template>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">User</div>
              <div class="title primary--text text--darken-2" v-if="userProfile.full_name">{{userProfile.full_name}}</div>
              <div class="title primary--text text--darken-2" v-else>{{userProfile.email}}</div>
            </div>
            <v-form ref="form" lazy-validation>
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
            </v-form>
          </template>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="cancel">Cancel</v-btn>
          <v-btn @click="reset">Reset</v-btn>
          <v-btn @click="submit" :disabled="invalid">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </ValidationObserver>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfileUpdate } from '@/interfaces';
import { readUserProfile } from '@/store/main/getters';
import { dispatchUpdateUserProfile } from '@/store/main/actions';

@Component
export default class UserProfileEdit extends Vue {
  // public valid = true;
  public password1 = '';
  public password2 = '';

  get userProfile() {
    return readUserProfile(this.$store);
  }

  public reset() {
    this.password1 = '';
    this.password2 = '';
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    const updatedProfile: IUserProfileUpdate = {};
    updatedProfile.password = this.password1;
    await dispatchUpdateUserProfile(this.$store, updatedProfile);
    this.$router.push('/main/profile');
  }
}
</script>
