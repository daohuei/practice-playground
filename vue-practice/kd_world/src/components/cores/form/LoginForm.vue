<template>
    <div>
        <v-row>
            <v-col cols="12" md="10">
                <v-text-field
                    v-model="token"
                    label="Please Input Bearer Token"
                    required
                ></v-text-field>
            </v-col>

            <v-col cols="12" md="2">
                <v-btn @click="login">SUBMIT</v-btn>
            </v-col>
        </v-row>

        <ValidationProvider name="count" rules="positive" v-slot="{ errors }">
            <v-row>
                <v-col cols="12" md="10">
                    <v-text-field
                        v-model="count"
                        label="Please Input Postive Number"
                        :error-messages="
                            errors != ''
                                ? 'Invalid: It\'s a non-positive number or not a number'
                                : ''
                        "
                        required
                    ></v-text-field>
                </v-col>

                <v-col cols="12" md="2">
                    <v-btn @click="checkPositive">SUBMIT</v-btn>
                </v-col>
            </v-row>
        </ValidationProvider>
    </div>
</template>
<script>
import { ValidationProvider } from 'vee-validate';

export default {
    name: 'LoginForm',
    data: () => ({
        token: '',
        count: 0
    }),
    methods: {
        login: function() {
            console.log(this.token);
            if (this.token != '') {
                this.$store
                    .dispatch('login/AUTH_REQUEST', this.token)
                    .then(() => {
                        this.$router.push('/');
                    });
                console.log(this.$store.state.login.token);
                console.log(this.$store.state.login.status);
            }
        },
        checkPositive: function() {
            if (this.count > 0) {
                console.log("It's positive");
            } else {
                console.log('Nah');
            }
        }
    },
    components: {
        ValidationProvider
    }
};
</script>
