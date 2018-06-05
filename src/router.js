import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import About from "./views/About.vue";
import Place from "./views/Place.vue";
import Comments from "./views/Comments.vue";
import Style from './views/Style'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/about",
      name: "about",
      component: About
    },
    {
      path: "/place",
      name: "place",
      component: Place
    },
    {
      path: "/style",
      name: "style",
      component: Style
    },
    {
      path: "/comments",
      name: "commment",
      component: Comments,
      props: { default: true}
    }
  ]
});
