<template>
  <div class="container-component rsa-component" v-show="showComponent">
    <div class="row">
      <div class="upload-file">
        <label for="test">Загрузите файл: </label>
        <input type="file" name="test" ref="file" accept=".txt" @change="handler">
      </div>
      <div class="upload-button">
        <input type="button" value="Загрузить" @click="upload">
      </div>
    </div>
    <div>

    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'rsa-encrypt',
  data () {
    return {
      file: ''
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    showComponent () {
      return this.getView === 'rsa'
    },
  },
  methods: {
    ...mapActions('rsa', ['setFile']),
    upload () {
      this.setFile(this.file)
    },
    handler () {
      this.file = this.$refs.file.files[0];
    }
  }
}
</script>

<style lang="scss" scoped>
  .rsa-component {
    padding: 20px 50px;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;

    .row {
      height: fit-content;
      margin-bottom: 10px;
      display: flex;
      flex-direction: column;

      .upload-file {
        display: flex;
        flex-direction: row;
        padding: 5px 10px;
        font-size: 2em;

        input[type=file] {
          font-size: 0.5em;
          margin: auto auto auto 20px;
        }
      }

      .upload-button {
        padding: 5px 10px;
      }

    }
  }
</style>