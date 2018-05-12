<template>
  <div class="comments">
    <h1>This is the comments</h1>
    <!-- <ul v-if="posts && posts.length"> -->
    <li v-for="comment of comments" :key="comment.id">
      <p><strong>{{comment.email}}</strong></p>
      <p>{{comment.body}}</p>
    </li>
  {{errors}}
  </div>
</template>
<script>
import {getComments, cube } from '../http_common';

export default {
  data() {
    console.log(this.$router.query.id)
    return {
      comments: [],
      errors: []
    }
  },
   created() {
    getComments(1)
      .then((response) => { this.comments = response.data;})
      .catch((error) => {this.errors = error;})

  }
}
</script>