<template>
  <div class="container-component gamm-component" v-show="showComponent">
    <div class="row">
      <div class="buttons-block">
        <input type="button" value="Зашифровать" @click="setParam" :disabled="text == ''">
      </div>
    </div>
    <div class="row" height="300px">
      <div class="input-text">
        <div class="label-input">
          <label for="textarea-1">Сообщение</label>
          <textarea name="text" placeholder="Текст ообщения" v-model="text"></textarea>
        </div>
      </div>
    </div>
    <div v-if="getGamma !== null">
      <div class="row">
        <div class="input-text">
          <div class="label-input">
            <label for="textarea-1">Зашифрованное сообщение</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="getEncrypt"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text">
          <div class="label-input">
            <label for="textarea-1">Гамма-последовательность</label>
            <textarea name="textarea-1" placeholder="Гамма-последовательность" readonly v-model="getGamma"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text">
          <div class="label-input">
            <label for="textarea-1">Расшифрованное сообщение</label>
            <textarea name="textarea-1" placeholder="Расшифрованное сообщение" readonly v-model="getDecrypt"></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex' 

export default {
  name: 'Gamm',
  data () {
    return {
      text: '',
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    ...mapGetters('gamm', ['getGamma', 'getEncrypt', 'getDecrypt']),
    showComponent () {
      return this.getView === 'gamming'
    },
  },
  methods: {
    ...mapActions('gamm', ['sendTextAction']),
    setParam () {
      this.sendTextAction({
        text: this.text,
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  .gamm-component {
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

        .label-input {
          display: block;
          width: 100%;
        }

        &.result {
          
          textarea {
            height: 100%;
          }
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