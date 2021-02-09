export const getInitialState = () => ({
    token: localStorage.getItem('user-token') || '',
    status: ''
});
