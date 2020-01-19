const axios = require('axios')

export default {
  namespaced: true,
  state: {
    dh: {
      param: null,
      encrypt: '',
      decrypt: ''
    }
  },
  actions: {
    setParam: async ({ commit }) => {
      let result = await axios.post('http://localhost:5000/getdh')
      if (result.status == 200) commit('SET_PARAM', result.data)
    },
    setEncrypt: async ({ state, commit }, text) => {
      let result = await axios.post('http://localhost:5000/encryptdh', {
        text: text
      })
      if (result.status == 200) commit('GET_ENCRYPT', result.data)
    },
    // actionDownloadFileEncrypt: async ({ commit }, url) => {
    //   await getFile(url)
    //   commit('ACTION_DOWNLOAD_FILE_ENCRYPT', url)
    // },
    // actionDownloadFileDecrypt: async ({ commit }, url) => {
    //   await getFile(url)
    //   commit('ACTION_DOWNLOAD_FILE_DECRYPT', url)
    // },
  },
  mutations: {
    SET_PARAM: (state, payload) => { state.dh.param = payload },
    GET_ENCRYPT: (state, payload) => {
      state.dh.encrypt = payload.encrypt
      state.dh.decrypt = payload.decrypt
    },
    ACTION_DOWNLOAD_FILE_ENCRYPT: (state, payload) => {},
    ACTION_DOWNLOAD_FILE_DECRYPT: (state, payload) => {},
  },
  getters: {
    getParam: state => state.dh.param,
    getEncrypt: state => state.dh.encrypt,
    getDecrypt: state => state.dh.decrypt
  }
}