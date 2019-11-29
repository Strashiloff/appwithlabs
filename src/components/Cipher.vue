<template>
  <div v-show="showComponent" class="container-component cipher-component">
    <div class="component-row type-block">
      <input
        type="button"
        class="left"
        value="Зашифровка"
        :class="{ 'select': getType === 'encrypt' }"
        @click="setTypeCip('encrypt')"
      >
      <input 
        type="button"
        class="right"
        value="Расшифровка"
        :class="{ 'select': getType === 'decrypt' }"
        @click="setTypeCip('decrypt')"
      >
    </div>
    <div class="component-row text-block">
      <div class="textarea-block">
        <textarea name="text" id="textarea1" cols="30" rows="10" placeholder="Текст который нужно зашифровать, поддерживаются только буквы русского и английского алфавита" v-model="text" autofocus></textarea>
        <label for="textarea1" v-if="this.alert1 !== null" class="label-input">{{ this.alert1 }}</label>
      </div>
      <div class="right-content">
        <div class="right-alert">
          <input type="text" name="key" placeholder="Ключ" v-model="key">
          <label for="textarea1" class="right-alert-text" v-if="this.alert2 !== null">{{ this.alert2 }}</label>
        </div> 
        <input type="button" value="Выполнить" v-bind:disabled="!enabled || !enabled2" @click="getTextFunction()">
      </div>
    </div>
    <div v-if="getEncryptionTable !== null" class="component-row result-blok">
      <h2>Шифрующая таблица:</h2>
      <KeyTable
        :array="getEncryptionTable"
      />
      <div class="old-new-text">
        <div class="content-area">
          <h2>{{ getType === 'encrypt' ? 'Исходный текст (преобразованный)' : 'Зашифрованный текст' }}</h2>
          <textarea cols="25" rows="6" readonly v-model="oldText"></textarea>
        </div>
        <div class="content-area">
          <h2 style="user-select: none; ">{{ getType === 'encrypt' ? 'Зашифрованный текст' : 'Расшифрованный текст' }}</h2>
          <textarea cols="30" rows="6" readonly v-model="newText"></textarea>
          <h2>Ключ: <i>{{ getKey }}</i></h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import KeyTable from './laba1/KeyTable'

export default {
  name: 'Cipher',
  components: {
    KeyTable
  },
  data () {
    return {
      text: '',
      key: '',
      alert1: null,
      alert2: null,
      enabled: false,
      enabled2: false
    }
  },
  watch: {
    text () {
      this.text = this.text.replace(/[^a-zA-Zа-яА-ЯёЁ ]/g, '')
      this.text = this.text.replace(/  /g, ' ')
      this.text = this.text.replace(/ё/g, 'е')
      this.text = this.text.replace(/Ё/g, 'Е')
      if (this.text.length > 0) {
        this.alert1 = null
        this.enabled2 = true
      } else {
        this.enabled2 = false
        this.alert1 = 'Заполните текст!'
      }
    },
    key () {
      this.key = this.key.replace(/[^a-zA-Zа-яА-ЯёЁ]/g, '')
      if (this.key.length > 0) {
        for (let i = 0; i < this.key.length; i++) {
          let count = 0
          for (let j = 0; j < this.key.length; j++) {
            if (this.key[i] === this.key[j] && i !== j) count++
            if (count > 0) {
              this.enabled = false
              this.alert2 = 'В ключе есть повторяющийся символ: ' + this.key[i]
              return
            }
          }
        }
        this.enabled = true 
        this.alert2 = null
      } else {
        this.enabled = false
        this.alert2 = 'Заполните ключ!'
      }
    },
    getNewText () {
      let scroll = document.getElementById('app')
      this.alert1 = null
      this.alert2 = null
      this.enabled = false
      this.enabled2 = false
      setTimeout(() => {
        window.scrollTo(0, scroll.scrollHeight)
      }, 100)
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    ...mapGetters('cipher', ['getType', 'getEncryptionTable', 'getText', 'getNewText', 'getKey']),
    showComponent() { return this.getView === 'cipher' },
    oldText: {
      get () { return this.getText },
      set () {}
    },
    newText: {
      get () { return this.getNewText },
      set () {}
    },
  },
  methods: {
    ...mapActions('cipher', ['setType', 'setKey']),
    getTextFunction () {
      if (this.text.length % 2 === 0){
        this.setKey({
          key: this.key,
          text: this.text
        })
        this.initial()
      } else {
        this.alert1 = 'Текст должен содержать четное количество символов'
        this.enabled2 = false
      }
    },
    initial () {
      this.text = ''
      this.key = ''
    },
    setTypeCip (type) {
      this.setType(type)
    }
  }
}
</script>

<style lang="scss" scoped>
  .cipher-component {
    padding: 20px 50px;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;

    .component-row {
      height: fit-content;
      min-width: 300px;
      margin: 10px 30px;
      display: flex;
      box-sizing: border-box;

      &.type-block {
        align-items: center;
        justify-content: center;
        
        input[type=button] {
          font-size: 1.7em;
          padding: 10px;
          width: 250px;
          margin: 0;
          border: none;
          outline: none;
        }

        .left {
          border-top-left-radius: 10px;
          border-bottom-left-radius: 10px
        }

        .right {
          border-top-right-radius: 10px;
          border-bottom-right-radius: 10px
        }

        .select {
          background-color: #4CAF50;
        }
      }

      &.text-block {
        height: 320px;
        justify-content: space-around;

        .textarea-block {
          height: 100%;
          width: 70%;
          box-sizing: border-box;

          textarea {
            height: 90%;
            width: 100%;
            padding: 10px;
            font-size: 2.2em;
            resize: none;
            margin: 0;
            box-sizing: border-box;
          }

          .label-input {
            height: 40px;
            width: 100%;
            background-color: rgb(230, 67, 67);
            margin-bottom: 10px;
            color: #ffffff;
            opacity: 0.6;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
            text-align: center;
            box-sizing: border-box;
            line-height: 40px
          }
        }

        .right-content {
          display: flex;
          flex-direction: column;
          height: 100%;
          width: 30%;
          box-sizing: border-box;

          input[type=button] {
            height: 60%;
            margin: auto;
            width: 60%;
            font-size: 2vw;
            background-color: #4CAF50;
            border: none;
            color: black;
            border-radius: 30px
          }

          @media (min-width: 400px) {
            input[type=button] {
              font-size: 2vw;
            }
          }

          input[type=button]:disabled {
            opacity: 0.3;
            height: 40%;
          }

          .right-alert {
            display: block;
            padding: 0 10%;
            width: 100%;
            height: 76px;
            box-sizing: border-box;

            input[type=text] {
              height: 80%;
              width: 100%;
              font-size: 1.6em;
              box-sizing: border-box;
            }

            .right-alert-text {
              height: fit-content;
              width: 100%;
              padding: 5px;
              background-color: rgb(230, 67, 67);
              color: #ffffff;
              opacity: 0.6;
              border-bottom-left-radius: 10px;
              border-bottom-right-radius: 10px;
              text-align: center;
              box-sizing: border-box;
            }
          }
        }
      }

      &.result-blok {
        padding: 0 0 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;

        h2 {
          margin-top: 0;
          margin-bottom: 5px;
        }

        .old-new-text {
          padding: 30px 10px;
          height: fit-content;
          width: 100%;
          display: flex;
          flex-direction: row;

          .content-area {
            height: 100%;
            width: 50%;
            display: inline-block;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;

            h2 {
              text-align: center;
              margin-bottom: 5px
            }

            textarea {
              width: 80%;
              margin: auto auto 20px auto;
              padding: 10px;
              font-size: 2em;
              resize: none;
              box-sizing: border-box;
              
            }
          } 
        }
      }

      textarea, label {
        display: block;
      }
    }
  }
</style>
