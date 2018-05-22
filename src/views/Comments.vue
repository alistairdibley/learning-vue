<template>
  <div class="comment">
    <h1>This is the comments</h1>
    <input type="text" name="Id" v-model="Id" v-on:keyup.enter="getblog">
      <p>{{blog.title}} </p>
       <p>{{blog.body}} </p>
  <!-- {{errors}} -->
  </div>
</template>
<script>
// import {getbogs, cube } from '../http_common';
import Vuex from "vuex";

export default {
  data() {
    return {
      comments: [],
      errors: [],
      Id: 1,
      blog: []
    }
  },
   created() {
    this.$store.dispatch('getBlogById', {Id: this.Id})
  },
 methods: {
   getblog: function() {
     this.$store.dispatch('getBlogById', {Id: this.Id})
    //  console.log(this.Id)
    //  this.blog = this.blogs[this.Id-1]
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