import Vue from 'vue';
import { setInteractionMode, ValidationProvider, ValidationObserver, extend } from 'vee-validate';

Vue.component('ValidationProvider', ValidationProvider);
Vue.component('ValidationObserver', ValidationObserver);
setInteractionMode('aggressive');

import '@/validation.js';
import {double} from 'vee-validate/dist/rules';

extend('double', double);