<template>
   <div class="container">
    <div class="columns">
      <div class="column is-narrow" style="width: 400px">
      <div style="width: 200px"><section>
        <br>
        <b-field label="Number A">
          <b-input></b-input>
        </b-field>
        <b-field label="Number B">
          <b-input></b-input>
        </b-field>
         <b-button type="is-success">Calculate</b-button>
      </section>
      </div>
      </div>
      <div class="column is-narrow"> <br>
        <div class="box" style="width: 400px"><h1 class="title">Result!</h1></div>
      </div>
      </div>
    </div>
  
</template>
<script>
import axios from 'axios'
export default {
  name: "Theory",
  data() {
   return {
     result: '',
      CalcForm: {
      numA: '',
      numB: '',
     
   },
    };
  },
  methods:{
    getResult() {
      const path = 'http://localhost:8000/last_result'
      axios.get(path)
      .then((res) =>{
        this.result = res.data.result
      })
      .catch((error) =>{
        // eslint-disable-next-line
          console.error(error);
      }
      )
    },
    addOperation(payload) {
      const path = 'http://localhost:8000/theory'
       axios.post(path, payload)
        .then(() => {
          this.getResult();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getResult();
        });
    },
    initOperation() {
      this.addOperation.numA = '';
      this.addOperation.numB = ''
    },
    SubmitOperation() {
      const payload = {
        numA: this.addOperation.numA,
        numB: this.addOperation.numB
      };
      this.addOperation(payload);
      this.initOperation();
    }
  }
  
}    
</script>