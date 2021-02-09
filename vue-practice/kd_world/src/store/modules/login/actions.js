export default {
    AUTH_REQUEST({ commit }, submit_token) {
        return new Promise(resolve => {
            // The Promise used for router redirect in login
            commit('AUTH_REQUEST');
            localStorage.setItem('user-token', submit_token); // store the token in localstorage
            commit('AUTH_SUCCESS', submit_token);
            resolve();
        });
    }
};
