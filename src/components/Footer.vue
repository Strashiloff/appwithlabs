<template>
  <div v-show="true" class="main-app-footer">
    <span class="footer-text">© 2019. Strashiloff LLC. All rights reserved.</span>
  </div>
</template>

<script>
export default {
  name: 'Header',
}
</script>

<style lang="scss" scoped>
  .main-app-footer {
    position: relative;
    bottom: 0;
    width: 100%;
    height: 10vh;
    max-height: 100px;
    min-height: 50px;
    display: flex;
    background-color: white;
    box-shadow: 0px -12px 34px rgba(0, 0, 0, 0.2);
    text-align: center;

    .footer-text {
      user-select: none; 
      margin: auto
    }
  }
</style>