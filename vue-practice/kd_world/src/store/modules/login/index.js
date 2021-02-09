import getters from './getters';
import mutations from './mutations';
import actions from './actions';
import { getInitialState } from './state';

export default {
    namespaced: true,
    getters,
    mutations,
    actions,
    state: getInitialState
};
