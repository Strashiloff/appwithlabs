const axios = require('axios')

export default {
  namespaced: true,
  state: {
    blocks: {
      decode: null,
      encode: null,
      key: null
    }
  },
  actions: {
    sendParamAction: async ({ commit }, payload) => {
      let result = await axios.post('http://localhost:5000/feistel', {
        text: payload.text,
        key: payload.key
      })
      if (result.status == 200) commit('SEND_PARAM_MUTATION', {
        key: payload.key,
        result: result.data
      })
    },
    getParamAction: ({ commit }, payload) => {
      commit('GET_PARAM_MUTATION')
    }
  },
  mutations: {
    SEND_PARAM_MUTATION: (state, payload) => {
      state.blocks.decode = payload.result.decode
      state.blocks.encode = payload.result.encode
      state.blocks.key = payload.key
    },
    GET_PARAM_MUTATION: (state, payload) => {}
  },
  getters: {
    getDecode: state => state.blocks.decode,
    getEncode: state => state.blocks.encode,
    getKey: state => state.blocks.key
  }
}