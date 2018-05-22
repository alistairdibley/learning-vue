import Vue from "vue";
import Vuex from "vuex";
import {getBlogs} from './http_common';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    blogs:[],
    loading:[]
  },
  mutations: {
    updateBlogs(state, blogs) {
      state.blogs = blogs
    },
    changeLoadingState(state, loading) {
      state.loading = loading
    }
  },
  actions: {
    loadData({
      commit
    }) {
      getBlogs().then((response) => {
        console.log(response.data, this)
        commit('updateBlogs', response.data)
        commit('changeLoadingState', false)
      })
    }
  },
});
