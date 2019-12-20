const axios = require('axios')

export default function () {
  return store => {
    let dispatch = store.dispatch

    let getDec = () => {
      dispatch('rsa/actionDownloadFileDecrypt', 'http://localhost:5000/decrypt')
    }
      
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
          setTimeout(getDec(), 500)
          break
      }
    })
  }
}