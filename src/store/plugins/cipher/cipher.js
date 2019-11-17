import cipherUtils from './utils'

export default function() {
  return store => {
    let getter = store.getters
    let dispatch = store.dispatch

    // qwertyuiopasdfghjklzxcvbnmйцукенгшщзфывапр

    let includeSymbol = (matr, symbol) => {
      for (let i = 0; i < matr.length; i++) {
        if(matr[i].includes(symbol)) return false;
      }
      return true
    }

    store.subscribe((mutation, state) => {
      let payload = mutation.payload

      switch (mutation.type) {
        case 'cipher/SET_KEY':
          dispatch('cipher/setText', {
            text: payload.text
          })
          break
        case 'cipher/SET_TEXT':
          let key = getter['cipher/getKey']
          let matr = [[], [], [], []]
          let k = 0
          for (let i = 0; i < key.length; i++) {
            if ((i + 1) % 30 === 0) k++
            matr[k].push(key[i])
          }
          for (let i = 1040; i < 1104; i++) {
            let char = String.fromCharCode(i)
            if (matr[k].length === 29 && k < 4) k++
            if (includeSymbol(matr, char)) matr[k].push(char)
          }
          for (let i = 65; i < 91; i++) {
            let char = String.fromCharCode(i)
            if (matr[k].length === 29 && k < 4) k++
            if (includeSymbol(matr, char)) matr[k].push(char)
          }
          for (let i = 97; i < 123; i++) {
            let char = String.fromCharCode(i)
            if (matr[k].length === 29 && k < 3 ) k++
            if (includeSymbol(matr, char)) matr[k].push(char)
          }

          dispatch('cipher/setEncryptionTable', matr)
          break
        case 'cipher/SET_ENCRYPTION_TABLE':
          let type = getter['cipher/getType']
          let table = payload
          let text = getter['cipher/getText']
          let newText
          switch (type) {
            case 'encrypt':
              newText = cipherUtils.encryptText(text, table)
              dispatch('cipher/setNewText', newText)
              break
            case 'decrypt':
              newText = cipherUtils.decryptText(text, table)
              dispatch('cipher/setNewText', newText)
              break
          }
          break
      }
    })
  }
}