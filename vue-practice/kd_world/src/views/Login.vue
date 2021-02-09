<template>
    <div>
        <LoginForm />
    </div>
</template>

<script>
// @ is an alias to /src
import LoginForm from '@/components/cores/form/LoginForm.vue';

export default {
    name: 'Login',
    components: {
        LoginForm
    }
};
</script>
