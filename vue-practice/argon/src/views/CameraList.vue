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
                          <v-data-table
                            :headers="headers"
                            :items="desserts"
                            :items-per-page="5"
                            class="elevation-1"
                          ></v-data-table>
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
      headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: '1%',
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: '1%',
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: '7%',
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: '8%',
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: '16%',
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: '0%',
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: '2%',
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: '45%',
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: '22%',
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: '6%',
          },
        ],
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
          'Access-Control-Allow-Origin': '*',
          'Authorization': this.bearer_token
        },
        }).then(response => {
        this.api_response = response.json()
      })
      */
    }
  }
};
</script>
