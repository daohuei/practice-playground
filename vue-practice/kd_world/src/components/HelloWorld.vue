<template>
    <div>
        <v-form v-model="valid">
            <v-container>
                <v-row>
                    <v-col cols="12" md="5">
                        <v-text-field
                            v-model="api_url"
                            label="Please Input API URL"
                            required
                        ></v-text-field>
                    </v-col>

                    <v-col cols="12" md="5">
                        <v-text-field
                            v-model="bearer_token"
                            label="Please Input Bearer Token"
                            required
                        ></v-text-field>
                    </v-col>

                    <v-col cols="12" md="2">
                        <v-btn @click="get_api_response">SUBMIT</v-btn>
                    </v-col>
                </v-row>
            </v-container>
        </v-form>
        <!--
        <div>
            <pre class="text-left">{{ api_responses }}</pre>
        </div>
        -->
        <DataTable :customers="customers" :headers="headers" />
    </div>
</template>

<script>
import axios from 'axios';
import DataTable from '@/components/cores/tables/DataTable.vue';
import { mapState } from 'vuex';
export default {
    data: () => ({
        name: 'HelloWorld',
        valid: false,
        api_responses: '',
        raw_responses: '',
        api_url: 'http://localhost:8080/v1/customers',
        headers: [
            { text: 'ID', value: '_id' },
            { text: 'Name', value: 'name' },
            { text: 'Status', value: 'status' },
            { text: 'Created Date', value: 'createdAt' },
            { text: 'Support Mode', value: 'isSupport' }
        ],
        customers: []
    }),
    methods: {
        get_api_response() {
            // Need to set up the Access-Control-Allow-Origin: "*" in the server side.
            // means every origin source can access the server to prevent rejection from CORS policy
            axios({
                methods: 'get',
                url: this.api_url,
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: this.bearer_token
                }
            }).then(response => {
                response.data.forEach(x => {
                    this.customers.push({
                        _id: x._id,
                        name: x.name,
                        status: x.status,
                        createdAt: x.createdAt,
                        isSupport: x.isSupport
                    });
                });
                // this.api_responses = JSON.stringify(response.data, null, 4);
            });
        }
    },
    components: {
        DataTable
    },

    computed: {
        ...mapState({
            bearer_token: state => state.login.token,
            tokenAlias: 'token'
        })
    }
};
</script>
