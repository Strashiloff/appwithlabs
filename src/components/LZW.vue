<template>
  <div class="container-component lzw-component" v-show="showComponent">
    <div class="row">
      <div class="buttons-block">
        <input type="button" value="Сжать" @click="setParam" :disabled="text == ''">
      </div>
    </div>
    <div class="row" height="300px">
      <div class="input-text">
        <div class="label-input">
          <label for="textarea-1">Cообщение{{getSize !== null ? ', размер: ' + getSize + ' байт': ''}}</label>
          <textarea name="text" placeholder="Сообщение" v-model="text"></textarea>
        </div>
      </div>
    </div>
    <div v-if="getDecoceHuff !== null">
      <div class="row">
        <div class="input-text ">
          <div class="label-input">
            <label for="textarea-1">Сообщение Зашифрованное методом Лемпеля Зива Велча, размер: {{getEncodeSize}} байт</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="getEncodedLzw"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text ">
          <div class="label-input">
            <label for="textarea-1">Сообщение Зашифрованное методом Хаффмана, размер: {{getEncodedHuff.length/8}} байт</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="getEncodedHuff"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text ">
          <div class="label-input">
            <label for="textarea-1">Сообщение Расшифрованное методом Хаффмана</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="getDecoceHuff"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text ">
          <div class="label-input">
            <label for="textarea-1">Сообщение Расшифрованное методом Лемпеля Зива Велча</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="getDecoceLzw"></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'lzw',
  data () {
    return {
      text: '',
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    ...mapGetters('lzw', ['getCodes', 'getDecoceHuff', 'getEncodedHuff', 'getDecoceLzw', 'getEncodedLzw', 'getSize', 'getEncodeSize']),
    showComponent () {
      return this.getView === 'lzw'
    },
  },
  methods: {
    ...mapActions('lzw', ['sendTextAction']),
    setParam () {
      this.sendTextAction({
        text: this.text,
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  .lzw-component {
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