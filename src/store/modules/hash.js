const axios = require('axios')

export default {
  namespaced: true,
  state: {
    hash: {
      hash: null
    }
  },
  actions: {
    sendPasswordAction: async ({ commit }, text) => {
      let result = await axios.post('http://localhost:5000/lab7', text)
      if (result.status == 200) commit('GET_PARAM_MUTATION', result.data)
    },
  },
  mutations: {
    GET_PARAM_MUTATION: (state, payload) => {
      state.hash.hash = payload.hashPass
    }
  },
  getters: {
    getHash: state => state.hash.hash
  }
}

