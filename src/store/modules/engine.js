export default {
  namespaced: true,
  state: {
    engine: {
      view: 'main',
      header: 'Главное меню'
    }
  },
  actions: {
    setView: ({ commit }, payload) => commit('SET_VIEW', payload),
    setHeader: ({ commit }, payload) => commit('SET_HEADER', payload)
  },
  mutations: {
    SET_VIEW: (state, payload) => { state.engine.view = payload },
    SET_HEADER: (state, payload) => { state.engine.header = payload }
  },
  getters: {
    getView: state => state.engine.view,
    getHeader: state => state.engine.header
  }
}
