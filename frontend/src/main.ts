import '@babel/polyfill';
// Import Component hooks before component definitions
import './component-hooks';
import Vue from 'vue';
import './plugins/vuetify';
import './plugins/vee-validate';
import './plugins/lodash';
import App from './App.vue';
import router from './router';
import store from '@/store';
import './registerServiceWorker';
import 'vuetify/dist/vuetify.min.css';
import Vuetify from 'vuetify';

Vue.config.productionTip = false;
const vuetifyOptions = { };
new Vue({
  router,
  store,
  render: (h) => h(App),
  vuetify: new Vuetify(vuetifyOptions),
}).$mount('#app');
