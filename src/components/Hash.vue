<template>
  <div class="container-component hash-component" v-show="showComponent">
    <div class="row">
      <div class="buttons-block">
        <input type="button" value="Захэшировать" @click="setParam" :disabled="text == ''">
      </div>
    </div>
    <div class="row" height="300px">
      <div class="input-text">
        <div class="label-input">
          <label for="textarea-1">Пароль</label>
          <textarea name="text" placeholder="Введите пароль" v-model="text"></textarea>
        </div>
      </div>
    </div>
    <div v-if="getHash !== null">
      <div class="row">
        <div class="input-text ">
          <div class="label-input">
            <label for="textarea-1">Захэшированный пароль</label>
            <textarea name="textarea-1" placeholder="Захэшированный пароль" readonly v-model="getHash"></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Hash',
  data () {
    return {
      text: '',
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    ...mapGetters('hash', ['getHash']),
    showComponent () {
      return this.getView === 'hash'
    },
  },
  methods: {
    ...mapActions('hash', ['sendPasswordAction']),
    setParam () {
      this.sendPasswordAction({
        text: this.text,
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  .hash-component {
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