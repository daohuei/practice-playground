<template>
    <div>
        <v-data-table
            name="customerTable"
            @click:row="tableClick"
            :headers="headers"
            :items="customers"
            :items-per-page="5"
            class="elevation-1"
        ></v-data-table>
        <p>{{ bearer_token }}</p>
        <v-data-table
            name="cameraTable"
            :headers="cam_headers"
            :items="cams"
            :items-per-page="5"
            class="elevation-1"
        ></v-data-table>
    </div>
</template>
<script>
import axios from 'axios';
import { mapState } from 'vuex';
export default {
    name: 'DataTable',
    props: ['customers', 'headers'],
    data: () => ({
        cam_headers: [
            { text: 'Jumbo ID', value: 'jumboId' },
            { text: 'Name', value: 'name' },
            { text: 'Cloud Record Strategy', value: 'cloudRecordStrategy' },
            { text: 'CV Strategy', value: 'cvStrategy' },
            { text: 'Created Date', value: 'createdAt' }
        ],
        cams: []
    }),
    methods: {
        tableClick(value) {
            this.cams = [];
            axios({
                methods: 'get',
                url:
                    'http://localhost:8080/v1/customers/' +
                    value._id +
                    '/cameras',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: this.bearer_token
                }
            }).then(response => {
                response.data.forEach(x => {
                    this.cams.push({
                        jumboId: x.jumboId,
                        name: x.name,
                        cloudRecordStrategy: x.cloudRecordStrategy,
                        cvStrategy: x.cvStrategy,
                        createdAt: x.createdAt
                    });
                });
            });
        }
    },

    computed: {
        ...mapState({
            bearer_token: state => state.login.token,
            tokenAlias: 'token'
        })
    }
};
</script>
