import Vue from 'vue';
import Vuex from 'vuex';

// Store functionality
import modules from './modules';

Vue.use(Vuex);

export default new Vuex.Store({
    modules
});
