<template>
  <div class="place">
    <h1>This is the</h1>
    <!-- <ul v-if="posts && posts.length"> -->
     <input type="text" name="search" v-model="search" v-on:keyup="getposts">
    <!-- <li v-for="post of posts" :key="post.id">
      <p>{{post.title}}</p>
      <p>{{post.body}}</p> -->
    <li style="list-style-type:none" v-for="post of posts" :key="post.id">
      <div v-if="!post.hide">
         <p>{{post.title}} |||| {{post.url}}</p> 
      </div>
    </li>
  </div>
</template>

<script>
import {getComments} from '../http_common';

export default {
  data() {
    return {
      posts: [],
      filtered: [],
      errors: [],
      search: null,
    }
  },

  async created() {
        getComments()
      .then((response) => { 
        this.posts = response.data;
        for (var key in this.posts ) {
            this.posts[key].hide = false;
        }
        })
      .catch((error) => {this.errors = error;})
  },
  methods: {
    getposts: function () {
      var filter = []
      for (var key in this.posts ) {
        if  (this.posts[key].title.includes(this.search)) {
          this.posts[key].hide = false;
          //  filter.push(this.posts[key])
        } else {
          this.posts[key].hide = true;
        }
       
      // console.log(filter);
      // this.filtered = filter
      }
    }
  }
}
</script>