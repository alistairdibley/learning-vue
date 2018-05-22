<template>
  <div class="place">
    <h1>Blog Stuff</h1>
    <div v-if="loading">
      loading....
    </div>
     <input type="text" name="search" v-model="search" v-on:keyup="getblogs">
    <li style="list-style-type:none" v-for="blog of blogs" v-bind:key="blog.id">
      <div v-if="!blog.hide">
         <p>{{blog.title}} |||| {{blog.created}}</p> 
      </div>
    </li>
  </div>
</template>

<script>
import {getBlogs} from '../http_common';
import Vuex from "vuex";

export default {
  data() {
    return {
      filtered: [],
      errors: [],
      search: null,
    }
  },

  created() {
      this.$store.dispatch('loadData')
  },
  methods: {
    getblogs: function () {
      for (var key in this.blogs ) {
        if  (this.blogs[key].title.includes(this.search)) {
          this.blogs[key].hide = false;
        } else {
          this.blogs[key].hide = true;
        }
      }
    }
  },
  computed: {
    blogs() {
        return this.$store.state.blogs
    },
    loading() {
      return this.$store.state.loading
    }
  }
}
</script>