<template>
  <div class="encryption-table">
    <table border="1">
      <tbody>
        <tr v-for="row in array" v-bind:key="row[0]">
          <td v-for="cell in row" v-bind:key="cell">{{ cell }}</td>
        </tr>
      </tbody>
    </table>   
  </div>
</template>

<script>
export default {
  name: 'KeyTable',
  props: ['array']
}
</script>

<style lang="scss" scoped>
  .encryption-table {
    margin: 0;
    font-size: 2.1em;

    table {
      user-select: none; 
      text-align: center;
      border-collapse: collapse;
    }

    tr, td {
      border-style: solid;
      border-width: 2px;
      border-color: rgb(73, 151, 53);
    }

    td {
      height: fit-content;
      width: 40px;
      background-color: rgba(108, 197, 86, 0.897);
    }
  }

</style>