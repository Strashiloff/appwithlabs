<template>
  <div v-show="true" class="main-app-header">
    <div class="back-content" >
      <transition name="back">
        <img class="back" v-show="showComponent" src="../assets/arrow-121-1282.png" @click="back">
      </transition>
    </div>
    <span class="header-text">{{ getHeader }}</span>
    <div class="cat-logo"></div>
    <div class="cat-background"></div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Header',
  computed: {
    ...mapGetters('ui', ['getView', 'getHeader']),
    showComponent() { return this.getView !== 'main' },
  },
  methods: {
    ...mapActions('ui', ['setView', 'setHeader']),
    back () {
      this.setView('main'),
      this.setHeader('Главное меню')
    }
  },
}
</script>

<style lang="scss" scoped>
  .main-app-header {
    position:fixed;
    width: 100%;
    height: 10vh;
    max-height: 100px;
    min-height: 50px;
    background-color: white;
    text-align: center;
    box-shadow: 0px 6px 14px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    z-index: 3;
    
    .header-text {
      font-size: xx-large;
      user-select: none; 
      margin: auto
    }

    .back-content {
      position: absolute;
      height: 100%;
      display: flex;
      flex-direction: column;
      z-index: 3;
      padding-left: 30px;

      .back {
        border-radius: 50%;
        height: 50%;
        background-position: center center;
        background-repeat: no-repeat;
        background-position: center;
        margin: auto;
        z-index: 3;
      }
    }
  
    .cat-logo {
      position: absolute;
      height: calc(100% - 20px);
      width: 38vw;
      background-image: url('../assets/cat.gif');
      background-position: center right;
      background-repeat: no-repeat;
      background-size: contain;
      margin: 10px auto;
      z-index: 2;
    }

    .cat-background {
      position: absolute;
      height: calc(100% - 36px);
      width: 38vw;
      background-image: linear-gradient(
          0deg,
          transparent,
          magenta,
          red,
          yellow,
          limegreen,
          turquoise,
          blue,
          magenta,
          transparent
        );
      background-position: center right 3.5vw;
      background-repeat: no-repeat;
      background-size: contain;
      margin: 18px 0;
      z-index: 1;
    }
    .back-enter-active, .back-leave-active {
      transition: all 0.5s ease-in-out;
    }
    .back-enter, .back-leave-to {
      transform: rotate(-180deg);
      opacity: 0;
    }
  }
</style>
