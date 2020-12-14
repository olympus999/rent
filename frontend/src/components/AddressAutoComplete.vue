<template>
  <v-combobox :items="addressOptions"
              :error-messages="errorMessages"
              :success="success"
              :search-input.sync="addressTyping">

  </v-combobox>
</template>

<script lang="ts">
  import {Component, Vue, Watch} from 'vue-property-decorator';
  import { getAddressAutoComplete } from '@/store/main/actions';

  const AddressAutoCompleteProps = Vue.extend({
    props: {
      errorMessages: Array,
      success: Boolean,
      value: String
    }
  })

  @Component
  export default class AddressAutoComplete extends AddressAutoCompleteProps {
    public addressOptions: string[] = []
    public addressTyping: string = ''
    // public addressAutoCompleted: string = ''
    public timer: number = 0;

    async updated() {
      if(this.addressTyping !== this.value) {
        this.addressTyping = this.value
      }
    }

    @Watch('addressTyping')
    onAddressChange(value: string) {
      if(this.addressTyping) {
        this.$emit('input', this.addressTyping)
      }
      if(this.timer) {
        clearTimeout(this.timer)
      }
      this.timer = window.setTimeout(() => this.updateAddressOptions(this.addressTyping), 400)
    }

    public async updateAddressOptions(input: string) {
      if (input) {
        this.addressOptions = await getAddressAutoComplete(this.$store, input)
      }
    }
  }
</script>

<style scoped>

</style>