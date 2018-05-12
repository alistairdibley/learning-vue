<template>
  <div class="place">
    <h1>This is the</h1>
    <!-- <ul v-if="posts && posts.length"> -->
    <li v-for="post of posts" :key="post.id">
      <p><strong>{{post.title}}</strong></p>
      <p>{{post.body}}</p>
    </li>
  <!-- </ul> -->
  </div>
</template>
<script>
import {HTTP} from '../http_common';

export default {
  data() {
    return {
      posts: [],
      errors: []
    }
  },

  async created() {
    HTTP.get(`posts`)
    .then(response => {
      this.posts = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}
</script>