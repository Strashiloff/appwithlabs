import cipherUtils from '../plugins/cipher/utils'

export default {
  namespaced: true,
  state: {
    cipher: {
      type: 'encrypt',
      text: null,
      key: null,
      table: null,
      newText: null
    }
  },
  actions: {
    setType: ({ commit }, payload) => commit('SET_TYPE', payload),
    setKey: ({ commit }, payload) => commit('SET_KEY', payload),
    setText: ({ commit }, payload) => commit('SET_TEXT', cipherUtils.deleteSpacesFromText(payload.text)),
    setEncryptionTable: ({ commit }, payload) => commit('SET_ENCRYPTION_TABLE', payload),
    setNewText: ({ commit }, payload) => commit('SET_NEW_TEXT', payload),
  },
  mutations: {
    SET_TYPE: (state, payload) => { state.cipher.type = payload },
    SET_KEY: (state, payload) => { state.cipher.key = payload.key },
    SET_TEXT: (state, payload) => { state.cipher.text = payload },
    SET_ENCRYPTION_TABLE: (state, payload) => { state.cipher.table = payload },
    SET_NEW_TEXT: (state, payload) => { state.cipher.newText = payload },
  },
  getters: {
    getType: state => state.cipher.type,
    getKey: state => state.cipher.key,
    getText: state => state.cipher.text,
    getEncryptionTable: state => state.cipher.table,
    getNewText: state => state.cipher.newText
  }
}
