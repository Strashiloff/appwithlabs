<template>
  <div class="container-component dh-component" v-show="showComponent">
    <div class="row">
      <div class="buttons-block">
        <input type="button" value="Сгенирировать ключи" @click="setParam">
        <input type="button" value="Шифровать" @click="setText" :disabled="getParam == null">
      </div>
    </div>
    <div class="row">
      <div class="column">
        <p class="columnp">Сторона 1</p>
        <div class="param" v-if="getParam">
          <p>{{ 'a = ' + getParam.a + '  g = ' + getParam.g + '  p = ' + getParam.p }}</p>
          <p>{{ 'A = ' + getParam.A }}</p>
          <p>{{ 'K = ' + getParam.K1 }}</p>
        </div>
      </div>
      <div style="height: 100%; margin: auto;">
        <img style="margin: auto;" src="../assets/dh.png">
      </div>
      <div class="column">
        <p class="columnp">Сторона 2</p>
        <div class="param" v-if="getParam">
          <p>{{ 'b = ' + getParam.b }}</p>
          <p>{{ 'B = ' + getParam.B }}</p>
          <p>{{ 'K = ' + getParam.K2 }}</p>
        </div>
      </div>
    </div>
    <div class="row" height="300px">
      <div class="input-text">
        <textarea name="text" placeholder="Сообщение" v-model="text"></textarea>
      </div>
    </div>
    <div class="row" height="300px">
      <div class="column no-border">
        <textarea name="text" v-model="getEncrypt" placeholder="Зашифрованное сообщение" readonly></textarea>
      </div>
      <div class="column no-border">
        <textarea name="text" v-model="getDecrypt" placeholder="Расшифрованное сообщение" readonly></textarea>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'DH',
  data () {
    return {
      text: ''
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    ...mapGetters('dh', ['getParam', 'getEncrypt', 'getDecrypt']),
    showComponent () {
      return this.getView === 'dh'
    },
  },
  methods: {
    ...mapActions('dh', ['setParam', 'setEncrypt']),
    setText() {
      this.setEncrypt(this.text)
    }
  }
}
</script>

<style lang="scss" scoped>
  .dh-component {
    padding: 20px 50px;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;

    .row {
      height: fit-content;
      margin-bottom: 10px;
      display: flex;
      flex-direction: row;
      box-sizing: border-box;

      .input-text {
        width: 100%;
        margin: 0 30px;
        display: flex;
        align-items: center;

        textarea {
          height: 100px;
          width: 100%;
          font-size: 1em;
          padding: 5px;
          resize: none;
          box-sizing: border-box;
        }
      }

      .column {
        width: 50%;
        height: fit-content;
        box-sizing: border-box;
        margin: 0 30px;
        border: solid black 1px;
        box-sizing: border-box;

        p {
          width: 100%;
          text-align: center
        }

        .param {
          padding: 0 20px
        }

        &.no-border {
          border: 0;
          height: 200px;
        }

        textarea {
          height: 200px;
          width: 100%;
          font-size: 1em;
          padding: 5px;
          resize: none;
          box-sizing: border-box;
        }
      }

      .buttons-block {
        height: fit-content;
        width: 100%;
        padding: 10px;
        display: flex;
        justify-content: center;

        input[type=button] {
          height: 50px;
          width: 240px;
          margin: 0 20px;
          font-size: 1em
        }
      }
    }
  }
</style>