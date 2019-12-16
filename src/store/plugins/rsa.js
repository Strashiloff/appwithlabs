const axios = require('axios')

export default function () {
  return store => {
    let dispatch = store.dispatch
      
    store.subscribe((mutation, state) => {
      let payload = mutation.payload

      switch (mutation.type) {
        case 'rsa/SET_FILE':
          dispatch('rsa/getEncrypt')
          break
        case 'rsa/GET_ENCRYPT':
          dispatch('rsa/actionDownloadFileEncrypt', 'http://localhost:5000/encrypt')
          break
        case 'rsa/ACTION_DOWNLOAD_FILE_ENCRYPT':
          setTimeout(dispatch('rsa/actionDownloadFileDecrypt', 'http://localhost:5000/decrypt'), 500)
          break
      }
    })
  }
}