<template>
  <div class="container-component linblock-component" v-show="showComponent">
    <div class="row">
      <div class="buttons-block">
        <input type="button" value="Передать" @click="setParam" :disabled="text == ''">
      </div>
    </div>
    <div class="row" height="300px">
      <div class="input-text">
        <div class="label-input">
          <label for="textarea-1">Текст</label>
          <textarea name="text" placeholder="Текст" v-model="text"></textarea>
        </div>
      </div>
    </div>
    <div v-if="getBits !== null">
     <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">Фраза в битовом виде:</label>
            <textarea name="textarea-1" placeholder="Фраза в битовом виде" readonly v-model="bitsToStr"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">Фраза разбитая на блоки по 4 бита:</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="blocksToStr"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text">
          <div class="label-input">
            <label for="textarea-1">Порождающая матрица G (первые 4 бита - информационные, остальные 4 - контрольные):</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="gToStr"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text">
          <div class="label-input">
            <label for="textarea-1">Матрица проверки четности Р: </label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="pToStr"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text" :class="{ 'result': getR.length != 4 }">
          <div class="label-input">
            <label for="textarea-1">Суммирование строк для построения блочного кода:</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="rToStr"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">Линейный блочный код:</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="rToP1"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">В блоке сгенерирована ошибка: </label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="rToP1_error"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">Синдром ошибки:</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="rToP1_error"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">Синдром ошибки:</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="mas_sToStr"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">Разряд ошибки:</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="getIndex_error"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">Исправленный код:</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="fix_codeToStr"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="input-text result">
          <div class="label-input">
            <label for="textarea-1">Исходный блок кода:</label>
            <textarea name="textarea-1" placeholder="Зашифрованное сообщение" readonly v-model="first_codeToStr"></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Linblock',
  data () {
    return {
      text: '',
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    ...mapGetters('linblock', ['getBits', 'getBlocks', 'getG', 'getP', 'getR', 'getP1', 'getP1_error', 'getMas_s', 'getIndex_error', 'getFix_code', 'getFirst_code']),
    showComponent () {
      return this.getView === 'lbc'
    },
    bitsToStr () {
      return this.getBits.join('')
    },
    blocksToStr () {
      return '[' + this.getBlocks.join('] [') + ']'
    },
    gToStr () {
      return '[' + this.getG.join(']\n[') + ']'
    },
    pToStr () {
      return '[' + this.getP.join(']\n[') + ']'
    },
    rToStr () {
      return '[' + this.getR.join(']\n[') + ']'
    },
    rToP1 () {
      return this.getP1.join(' ')
    },
    rToP1_error () {
      return this.getP1_error.join(' ')
    },
    rToP1_error () {
      return this.getP1_error.join(' ')
    },
    mas_sToStr () {
      return this.getMas_s.join(' ')
    },
    fix_codeToStr () {
      return this.getFix_code.join(' ')
    },
    first_codeToStr () {
      return this.getFirst_code.join(' ')
    }
  },
  methods: {
    ...mapActions('linblock', ['sendTextAction']),
    setParam () {
      this.sendTextAction({
        text: this.text,
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  .linblock-component {
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