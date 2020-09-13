<template>
  <v-main>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <ValidationObserver v-slot="{ invalid }" ref="provider">
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>{{appName}} - Reset Password</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <p class="subheading">Enter your new password below</p>
                <v-form @keyup.enter="submit" ref="form">
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
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel">Cancel</v-btn>
                <v-btn @click="reset">Clear</v-btn>
                <v-btn @click="submit" :disabled="invalid">Save</v-btn>
              </v-card-actions>
            </v-card>
          </ValidationObserver>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfileUpdate } from '@/interfaces';
import { appName } from '@/env';
import { commitAddNotification } from '@/store/main/mutations';
import { dispatchResetPassword } from '@/store/main/actions';

@Component
export default class UserProfileEdit extends Vue {
  public appName = appName;
  public password1 = '';
  public password2 = '';

  public mounted() {
    this.checkToken();
  }

  public reset() {
    this.password1 = '';
    this.password2 = '';
  }

  public cancel() {
    this.$router.push('/');
  }

  public checkToken() {
    const token = (this.$router.currentRoute.query.token as string);
    if (!token) {
      commitAddNotification(this.$store, {
        content: 'No token provided in the URL, start a new password recovery',
        color: 'error',
      });
      this.$router.push('/recover-password');
    } else {
      return token;
    }
  }

  public async submit() {
    const token = this.checkToken();
    if (token) {
      await dispatchResetPassword(this.$store, { token, password: this.password1 });
      this.$router.push('/');
    }
  }
}
</script>
