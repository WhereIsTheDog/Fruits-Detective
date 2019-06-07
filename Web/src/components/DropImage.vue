<template>
  <div class="hello">
    <img-inputer
      v-model="file"
      theme="light"
      size="large"
      class="img-container"
    />
    <h1>{{ loading ? '...' : what || 'nothong' }}</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      file: null,
      dataUrl: null,
      what: '',
      loading: false
    }
  },
  watch: {
    file(file) {
      if (!file || !window.FileReader) return
      if (/^image/.test(file.type)) {
        let reader = new FileReader()
        reader.readAsDataURL(file)
        const vm = this
        reader.onloadend = function() {
          vm.dataUrl = this.result
        }
      }
    },
    async dataUrl(value) {
      this.loading = true
      try {
        this.what = await this.parseImage(value)
      } catch (error) {
        this.what = 'ops!'
      }
      this.loading = false
    }
  },
  methods: {
    async parseImage(dataUrl) {
      try {
        const time = +new Date() + ''
        const picture = dataUrl.slice(23)
        await axios('http://www.nbutlab.com:5000/todo/api/v1/image', {
          method: 'post',
          params: { picture, time }
        })
        const {
          data: { imageinfo }
        } = await axios.get('http://www.nbutlab.com:5000/todo/api/v1/image', {
          params: { time }
        })
        return imageinfo
      } catch (error) {
        // eslint-disable-next-line
        console.error(error)
        throw error
      }
    }
  }
}
</script>

<style lang="stylus">
.img-container
  .img-inputer__preview-img
    width auto
    max-width 100%
    max-height 100%
</style>
