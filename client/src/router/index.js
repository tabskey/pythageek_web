import Vue from "vue";
import Router from "vue-router";
import AppMain from "../views/AppMain.vue";
import Theory from "../components/Theory";
import AppAbout from "../components/AppAbout";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "AppMain",
      component: AppMain,
    },
    {
      path: "/theory",
      name: "Theory",
      component: Theory,
    },
    {
      path: "/about",
      name: "AppAbout",
      component: AppAbout,
    },
  ],
});
