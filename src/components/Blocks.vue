<template>
  <div class="container-component blocks-component" v-show="showComponent">
    <div class="row">
      <div class="buttons-block">
        <input type="button" value="Зашифровать" @click="setParam" :disabled="text == '' || key == ''">
      </div>
    </div>
    <div class="row" height="100px">
      <div class="input-text key">
        <textarea name="text" placeholder="Ключ" v-model="key"></textarea>
      </div>
    </div>
    <div class="row" height="300px">
      <div class="input-text">
        <textarea name="text" placeholder="Сообщение" v-model="text"></textarea>
      </div>
    </div>
    <div class="row" height="300px">
      <div class="column no-border">
        <textarea name="text" v-model="getEncode" placeholder="Зашифрованное сообщение" readonly></textarea>
      </div>
      <div class="column no-border">
        <textarea name="text" v-model="getDecode" placeholder="Расшифрованное сообщение" readonly></textarea>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Blocks',
  data () {
    return {
      text: '',
      key: ''
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    ...mapGetters('blocks', ['getDecode', 'getEncode']),
    showComponent () {
      return this.getView === 'blocks'
    },
  },
  methods: {
    ...mapActions('blocks', ['sendParamAction']),
    setParam () {
      this.sendParamAction({
        text: this.text,
        key: this.key
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  .blocks-component {
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

        &.key {
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