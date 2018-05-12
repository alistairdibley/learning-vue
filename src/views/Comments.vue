<template>
  <div class="comment">
    <h1>This is the comments</h1>
    <input type="text" name="commentId" v-model="commentId" v-on:keyup.enter="getcomments">
      <p>{{comments.title}} </p>
       <p>{{comments.url}} </p>
  <!-- {{errors}} -->
  </div>
</template>
<script>
import {getComments, cube } from '../http_common';

export default {
  data() {
    return {
      comments: [],
      errors: [],
      commentId: 1
    }
  },
   async created() {
  //   // this.$router.push({ path: 'comment', query: { commentId: this.commentId }})

    getComments(1)
      .then((response) => { this.comments = response.data;})
      .catch((error) => {this.errors = error;})
  },
  methods: {
    getcomments:  function () {
      if (this.commentId) {
        getComments(this.commentId) 
        .then((response) => { this.comments = response.data;})
        .catch((error) => {this.errors = error;})
      }
  }
  }
}
</script>