import '@babel/polyfill';
// Import Component hooks before component definitions
import './component-hooks';
import Vue from 'vue';
import './plugins/vuetify';
import './plugins/vee-validate';
import './plugins/lodash';
// import './plugins/google-autocomplete';
import App from './App.vue';
import router from './router';
import store from '@/store';
import './registerServiceWorker';
import 'vuetify/dist/vuetify.min.css';
import Vuetify from 'vuetify';
import './assets/style.css'


Vue.config.productionTip = false;
const vuetifyOptions = { };
// Vue.use(GoogleLocationAutofillPlugin)
new Vue({
  router,
  store,
  render: (h) => h(App),
  vuetify: new Vuetify(vuetifyOptions),
}).$mount('#app');
