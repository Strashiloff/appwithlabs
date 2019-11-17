<template>
  <div v-show="showComponent" class="container-component flex-mp">
    <div class="row-container" v-for="state in states" :key="state.item">
      <input v-for="item in state" :key="item.view" type="button" :value="item.label" class="task-button" @click="click(item)">
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import states from '../store/states/states'

export default {
  name: 'Main',
  data () {
    return {
      st: states
    }
  },
  computed: {
    ...mapGetters('ui', ['getView']),
    showComponent() { return this.getView === 'main' },
    states () {
      return this.st
    }
  },
  methods: {
    ...mapActions('ui', ['setView', 'setHeader']),
    click (item) {
      this.setView(item.view)
      this.setHeader(item.label)
    }
  }
}
</script>

<style lang="scss" scoped>
  .flex-mp {
    width: 100%;
    padding: 25px 105px;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    overflow: hidden;

    .row-container {
      width: 100%;
      height: 150px;
      margin: 25px 0;
      display: flex;
      flex-direction: row;
      box-sizing: border-box;
      justify-content: center;

      .task-button {
        height: 130px;
        width: 50%;
        border-radius: 10ch;
        margin: auto 20px;
        font: serif;
        font-size: xx-large;
      }
    }
  }
</style>