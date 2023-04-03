import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import List from "../views/ListView.vue";
import Form from "../views/CadastroView.vue";
Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "home",
    component: List,
  },
  {
    path: "/Cadastro",
    name: "/cadastro",
    component: Form,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
