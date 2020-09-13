<template>
  <v-main>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <ValidationObserver v-slot="{ invalid }" ref="provider">
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>{{appName}} - Password Recovery</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <p class="subheading">A password recovery email will be sent to the registered account</p>
                <v-form @keyup.enter="submit" ref="form" @submit.prevent="" lazy-validation>
                  <ValidationProvider rules="required|email" v-slot="{ errors, valid }">
                    <v-text-field @keyup.enter="submit" label="E-Mail" type="text" prepend-icon="person" v-model="username"
                                  data-vv-name="username" :error-messages="errors" :success="valid"></v-text-field>
                  </ValidationProvider>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel">Cancel</v-btn>
                <v-btn @click.prevent="submit" :disabled="invalid">
                  Recover Password
                </v-btn>
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
import { appName } from '@/env';
import { dispatchPasswordRecovery } from '@/store/main/actions';

@Component
export default class Login extends Vue {
  public username: string = '';
  public appName = appName;

  public cancel() {
    this.$router.back();
  }

  public submit() {
    dispatchPasswordRecovery(this.$store, { username: this.username });
  }
}
</script>

<style>
</style>
