const axios = require('axios')

export default {
  namespaced: true,
  state: {
    gamma: {
      encrypt: null,
      gamma: null,
      decrypt: null
    }
  },
  actions: {
    sendTextAction: async ({ commit }, text) => {
      let result = await axios.post('http://localhost:5000/lab8', text)
      if (result.status == 200) commit('GET_PARAM_MUTATION', result.data)
    },
  },
  mutations: {
    GET_PARAM_MUTATION: (state, payload) => {
      state.gamma.encrypt = payload.encrypt
      state.gamma.gamma = payload.gamma
      state.gamma.decrypt = payload.decrypt
    }
  },
  getters: {
    getGamma: state => state.gamma.gamma,
    getEncrypt: state => state.gamma.encrypt,
    getDecrypt: state => state.gamma.decrypt
  }
}

