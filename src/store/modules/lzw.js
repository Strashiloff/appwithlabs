const axios = require('axios')

export default {
  namespaced: true,
  state: {
    lzw: {
      codes: null,
      decoceHuff: null,
      encodedHuff: null,
      decoceLzw: null,
      encodedLzw: null,
      size: null,
      encodeSize: null
    }
  },
  actions: {
    sendTextAction: async ({ commit }, text) => {
      let result = await axios.post('http://localhost:5000/lab6', text)
      if (result.status == 200) commit('GET_PARAM_MUTATION', result.data)
    },
  },
  mutations: {
    GET_PARAM_MUTATION: (state, payload) => {
      state.lzw = payload
    }
  },
  getters: {
    getCodes: state => state.lzw.codes,
    getDecoceHuff: state => state.lzw.decoceHuff,
    getEncodedHuff: state => state.lzw.encodedHuff,
    getDecoceLzw: state => state.lzw.decoceLzw,
    getEncodedLzw: state => state.lzw.encodedLzw,
    getSize: state => state.lzw.size,
    getEncodeSize: state => state.lzw.encodeSize
  }
}

