<template>
    <div>

                                <!--
                                <div class="btn-wrapper">
                                    <base-button tag="a"
                                                 href="https://demos.creative-tim.com/argon-design-system/docs/components/alerts.html"
                                                 class="mb-3 mb-sm-0"
                                                 type="info"
                                                 icon="fa fa-code">
                                        Components
                                    </base-button>
                                    <base-button tag="a"
                                                 href="https://www.creative-tim.com/product/argon-design-system"
                                                 class="mb-3 mb-sm-0"
                                                 type="white"
                                                 icon="ni ni-cloud-download-95">
                                        Download HTML
                                    </base-button>
                                </div>
                            -->
        
        

        

        


        <section class="section section-shaped my-0 overflow-hidden">
            <div class="shape shape-style-3 bg-gradient-default shape-skew">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
            <div class="container pt-lg pb-300"/>
            <div class="container">
                <div class="row justify-content-center mt--300">
                    <div class="col-lg-8" id="api_result">
                        <card gradient="secondary" shadow body-classes="p-lg-5">
                            <h4 class="mb-1">Please input HTTP API URL</h4>
                            <a href="http://apidoc.umbocv.com/AdminGrasshopper/" target="_blank">API Documentation</a>
                            <p></p>
                            <div class="row">
                              <div class="col-9">
                                <base-input 
                                        alternative
                                        placeholder="Bearer Token"
                                        addon-left-icon="ni ni-user-run" v-model="bearer_token">
                                </base-input>
                              </div>
                              <div class="col-3">
                                <base-button tag="a" type="primary" href="https://ag-staging.umbocv-inc.com" target="_blank">Get Token</base-button>
                              </div>
                            </div>
                            
                            <base-input class="mb-4">
                                    <textarea class="form-control form-control-alternative" name="name" rows="4"
                                              cols="80" placeholder="Type URL here..." v-model="api_url"></textarea>
                            </base-input>
                            <base-button type="default" round block size="lg" @click="get_api_response">
                                Test API
                            </base-button>
                            <pre>{{ api_responses }}</pre>
                            <!--
                              <div v-for="api_response in api_responses">
                                <p>Customer Name: {{api_response.name}}</p>
                                <p>Status: {{api_response.status}}</p>
                                <br/>
                              </div>
                            -->
                        </card>
                    </div>
                </div>
            </div>
        </section>
       

    </div>
</template>

<script>
// import axios from 'axios'
export default {
  name: "home",
  components: {},
  data() {
    return {
      api_responses: "",
      api_url: "http://localhost:8080/v1/customers",
      bearer_token: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imtlbi50aW5nQHVtYm9jdi5jb20iLCJzZXJ2aWNlX2RvbWFpbiI6IiIsImV4cCI6MTU5NzM5Nzg3Nn0.ABb7thA7p_3K87FKwdJ0FSLAxBGbXZ3nL7EqCGWIZio",
      json_obj: { "_id": "569616936295f9d4853b81f6", "name": "Woodies Lumbermill", "status": "active", "createdAt": "2016-01-13T09:19:15.304Z", "isSupport": false },
    };
  },
  methods:{
    get_api_response(){
      // Need to set up the Access-Control-Allow-Origin: "*" in the server side.
      // means every origin source can access the server to prevent rejection from CORS policy
      fetch(
        this.api_url,
        {
          headers: { 
              'Content-Type': 'application/json',
              'Authorization': this.bearer_token,
              },
          method: 'GET', // *GET, POST, PUT, DELETE, etc.
          //mode: 'no-cors', // no-cors, cors, *same-origin
        }
      ).then(res => res.json())
        .then(data => this.api_responses = JSON.stringify(data, null, 4));
        /*
        axios({
        methods: 'get',
        url: this.api_url,
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': this.bearer_token
        },
        }).then(res => res.json())
        .then(data => this.api_responses = JSON.stringify(data, null, 4));
      */
    }
  }
};
</script>
