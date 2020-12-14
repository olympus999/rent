import Vue from 'vue';
import { setInteractionMode, ValidationProvider, ValidationObserver } from 'vee-validate';

Vue.component('ValidationProvider', ValidationProvider);
Vue.component('ValidationObserver', ValidationObserver);
setInteractionMode('aggressive');

import '@/validation.js';
