const axios = require('axios')

async function getFile(url) {
  let response = await axios({
    method: 'post',
    url: url,
    responseType: 'blob',
  })
  const filename = await response.headers['x-suggested-filename']
  const downloadUrl = window.URL.createObjectURL(new Blob([response.data]))
  const link = document.createElement('a')
  link.href = downloadUrl;
  link.setAttribute('download', filename) 
  document.body.appendChild(link)
  link.click()
  link.remove()
}

export default {
  namespaced: true,
  state: {
    rsa: {
      file: '',
      keys: null
    }
  },
  actions: {
    setFile: ({ commit }, payload) => {
      commit('SET_FILE', payload)
    },
    getEncrypt: async ({ state, commit }) => {
      let formData = new FormData()
      formData.append('file', state.rsa.file)
      let result = await axios.post('http://localhost:5000/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
      if (result.status == 200) {
        commit('GET_ENCRYPT', result.data)
      }
    },
    actionDownloadFileEncrypt: async ({ commit }, url) => {
      await getFile(url)
      commit('ACTION_DOWNLOAD_FILE_ENCRYPT', url)
    },
    actionDownloadFileDecrypt: async ({ commit }, url) => {
      await getFile(url)
      commit('ACTION_DOWNLOAD_FILE_DECRYPT', url)
    },
  },
  mutations: {
    SET_FILE: (state, payload) => { state.rsa.file = payload },
    GET_ENCRYPT: (state, payload) => { state.rsa.keys = payload },
    ACTION_DOWNLOAD_FILE_ENCRYPT: (state, payload) => {},
    ACTION_DOWNLOAD_FILE_DECRYPT: (state, payload) => {},
  },
  getters: {
    getView: state => state.engine.view,
    getEncrypt: state => state.rsa.keys
  }
}