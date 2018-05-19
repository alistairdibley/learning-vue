<template>
  <div class="place">
    <h1>This is the</h1>
    <!-- <ul v-if="posts && posts.length"> -->
     <input type="text" name="search" v-model="search" v-on:keyup="getblogs">
    <!-- <li v-for="post of posts" :key="post.id">
      <p>{{post.title}}</p>
      <p>{{post.body}}</p> -->
    <li style="list-style-type:none" v-for="blog of blogs" v-bind:key="blog.id">
      <div v-if="!blog.hide">
         <p>{{blog.title}} |||| {{blog.created}}</p> 
      </div>
    </li>
  </div>
</template>

<script>
import {getBlogs} from '../http_common';

export default {
  data() {
    return {
      blogs: [],
      filtered: [],
      errors: [],
      search: null,
    }
  },

  async created() {
        getBlogs()
      .then((response) => { 
        this.blogs = response.data;
        for (var key in this.blogs ) {
            this.blogs[key].hide = false;
        }
        })
      .catch((error) => {this.errors = error;})
  },
  methods: {
    getblogs: function () {
      console.log(this.search)
      for (var key in this.blogs ) {
        if  (this.blogs[key].title.includes(this.search)) {
          this.blogs[key].hide = false;
        } else {
          this.blogs[key].hide = true;
        }
      }
    }
  }
}
</script>