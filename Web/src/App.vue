<template>
  <div id="app">
    <h1>Show me the fruits</h1>
    <DropImage />
  </div>
</template>

<script>
import DropImage from './components/DropImage.vue'

export default {
  name: 'app',
  components: {
    DropImage
  }
}
</script>

<style lang="stylus">
#app
  font-family 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50
  margin-top 60px
</style>
