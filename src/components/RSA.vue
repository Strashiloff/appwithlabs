<template>
  <div class="container-component rsa-component" v-show="showComponent">
    <div class="row">
      <div class="upload-file">
        <label for="test">Загрузите файл: </label>
        <input type="file" name="test" ref="file" accept=".txt" @change="handler">
      </div>
      <div class="upload-button">
        <input type="button" value="Отправить на шифрование/дешифрование" :disabled="dis" @click="upload">
      </div>
    </div>
    <div v-if="getEncrypt != null">
      <h2>Приватный ключ: {{ getEncrypt.private }}</h2>
      <h2>Публичный ключ: {{ getEncrypt.public }}</h2>
      <h2>N: {{ getEncrypt.n }}</h2>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'rsa-encrypt',
  data () {
    return {
      file: '',
      dis: true
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    ...mapGetters('rsa', ['getEncrypt']),
    showComponent () {
      return this.getView === 'rsa'
    },
  },
  watch: {
    file (value) {
      if (value != '' && value != undefined) {
        this.dis = false
      } else {
        this.dis = true
      }
    }
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
          font-family: Georgia, 'Times New Roman', Times, serif;
          font-size: 0.5em;
          margin: auto auto auto 20px;
        }
      }

      .upload-button {
        padding: 5px 10px;
        
        input[type=button] {
          font-family: Georgia, 'Times New Roman', Times, serif;
          font-size: 1em;
        }
      }

    }
  }
</style>