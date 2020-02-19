<template>
  <div id="app" class="class" data-app>
    <Header/>
    <div class="spacer"></div>
    <Main/>
    <Cipher/>
    <RSA/>
    <DH/>
    <Blocks/>
    <LZW/>
    <Hash/>
    <Gamm/>
    <Linblock/>
    <Footer/>
  </div>
</template>

<script>
import Header from './components/Header'
import Main from './components/Main'
import Cipher from './components/Cipher'
import Footer from './components/Footer'
import RSA from './components/RSA'
import DH from './components/DH'
import Blocks from './components/Blocks'
import LZW from './components/LZW'
import Hash from './components/Hash'
import Gamm from './components/Gamm'
import Linblock from './components/Lin'

export default {
  name: 'app',
  components: {
    Header,
    Main,
    Cipher,
    RSA,
    Footer,
    DH,
    LZW,
    Hash,
    Blocks,
    Gamm,
    Linblock
  }
}
</script>

<style lang="scss">
  html {
    overflow-x: hidden;
  }

  body {
    margin: 0;
    min-width: 640px;
  }

  ::-webkit-scrollbar {
    width: 12px;
  }
  
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
    border-radius: 10px;
  }
  
  ::-webkit-scrollbar-thumb {
    border-radius: 10px;
    box-shadow: inset 0 0 6px rgba(0,0,0,0.5); 
  }

  #app {
    position: relative;
    margin: 0;
    padding: 0;
    width: 100vw;
    height: fit-content;
    display: flex;
    overflow-y: auto;
    flex-direction: column;
    /* overflow: hidden; */
  }

  .container-component {
    min-height: 80vh;
  }

  .spacer {
    height: 10vh;
    max-height: 100px;
    min-height: 50px;
  }

  .component-enter-active{
    transition: opacity 0.5s ease-in;
  }
  .component-enter, .component-leave-to {
    opacity: 0;
  }

</style>
