import { shallowMount } from '@vue/test-utils';
import Vue from 'vue';
import Vuex from 'vuex';
import LoginForm from '../../src/components/cores/form/LoginForm.vue';
import Vuetify from 'vuetify';

Vue.use(Vuex, Vuetify);
describe('LoginForm.vue', () => {
    let actions;
    let store;
    let veutify;

    beforeEach(() => {
        actions = {
            AUTH_REQUEST: jest.fn()
        };
        store = new Vuex.Store({
            actions
        });
        veutify = new Vuetify();
    });

    it('dispatches "AUTH_REQUEST" when input event value is "input"', async () => {
        const wrapper = shallowMount(LoginForm, { store, veutify });
        await wrapper.setData({
            token: 'input'
        });

        wrapper.find('v-btn').trigger('click');

        expect(actions.AUTH_REQUEST).toHaveBeenCalled();
    });

    it('does not dispatch "AUTH_REQUEST" when event value is not "input"', () => {
        const wrapper = shallowMount(LoginForm, { store, veutify });
        wrapper.find('v-btn').trigger('click');
        expect(actions.AUTH_REQUEST).not.toHaveBeenCalled();
    });
});
