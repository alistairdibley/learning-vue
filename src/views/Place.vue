<template>
  <div class="place">
    <h1>Blog Stuff</h1>
    <div v-if="loading">
      loading....
    </div>
    <b-form-group horizontal label="Filter" class="mb-0">
          <b-input-group>
            <b-form-input v-model="filter" placeholder="Type to Search" />
            <b-input-group-append>
              <b-btn :disabled="!filter" @click="filter = ''">Clear</b-btn>
            </b-input-group-append>
          </b-input-group>
    </b-form-group>
    <b-table striped hover :items="blogs" :filter="filter">
    </b-table>
  </div>
</template>

<script>
import {getBlogs} from '../http_common';
import Vuex from "vuex";

export default {
  data() {
    return {
      filter: null,
    }
  },

  created() {
      this.$store.dispatch('getAllBlogs')
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