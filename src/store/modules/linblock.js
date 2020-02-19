const axios = require('axios')

export default {
  namespaced: true,
  state: {
    linblock: {
      bits: null,
      blocks: null,
      G: null,
      P: null,
      R: null,
      P1: null,
      P1_error: null,
      mas_s: null,
      index_error: null,
      fix_code: null,
      first_code: null
    }
  },
  actions: {
    sendTextAction: async ({ commit }, text) => {
      let result = await axios.post('http://localhost:5000/lab5', text)
      if (result.status == 200) commit('GET_PARAM_MUTATION', result.data)
    },
  },
  mutations: {
    GET_PARAM_MUTATION: (state, payload) => {
      state.linblock = payload
    }
  },
  getters: {
    getBits: state => state.linblock.bits,
    getBlocks: state => state.linblock.blocks,
    getG: state => state.linblock.G,
    getP: state => state.linblock.P,
    getR: state => state.linblock.R,
    getP1: state => state.linblock.P1,
    getP1_error: state => state.linblock.P1_error,
    getMas_s: state => state.linblock.mas_s,
    getIndex_error: state => state.linblock.index_error,
    getFix_code: state => state.linblock.fix_code,
    getFirst_code: state => state.linblock.first_code
  }
}

