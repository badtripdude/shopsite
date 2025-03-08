<template>
  <div>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
    };
  },
  async created() {
    const response = await this.$http.get('/hello/');
    this.message = response.data.message;
  },
};
</script>