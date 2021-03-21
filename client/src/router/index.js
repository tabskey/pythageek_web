import Vue from "vue";
import Router from "vue-router";
//import Home from "../views/Home.vue";
import Theory from "../components/Theory.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/theory",
      name: "Theory",
      component: Theory,
    },
  ],
});
