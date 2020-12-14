// import Vue from 'vue'
// import _Vue from 'vue';
//
// import {Client} from '@googlemaps/google-maps-services-js';
// import { PlaceAutocompleteRequest } from '@googlemaps/google-maps-services-js/dist';
// //
// const GoogleApiClient = new Client({});
// const googleLocation = async (input: string) => {
//   const AutoComplete: PlaceAutocompleteRequest = {
//     params: { input, key: 'XXX'}
//   };
//   return await GoogleApiClient.placeAutocomplete(AutoComplete)
// }
//
//
// const googleLocationPlugin = {
//   install: (Vue: typeof _Vue, options?: any) => {
//     Vue.prototype.$googleLocation = googleLocation;
//   }
// }
//
// Vue.use(googleLocationPlugin)
//
// interface IGoogleLocation {
//   (input: string): string
// }
//
// declare module 'vue/types/vue' {
//   interface Vue {
//     $googleLocation: IGoogleLocation;
//   }
// }
//
