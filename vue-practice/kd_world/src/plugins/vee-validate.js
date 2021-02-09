import Vue from 'vue';
import VeeValidate, { Validator } from 'vee-validate';

Validator.extend('positive', {
    validate: value => {
        return value > 0;
    }
});

Vue.use(VeeValidate);
