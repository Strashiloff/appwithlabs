// modules
import engineModule from './modules/engine'
import sipherModule from './modules/cipher'

// plugins
import loggerPlugins from './plugins/logger'
import cipherPlugins from './plugins/cipher/cipher'

export default ({
  strict: true,
  modules: {
    ui: engineModule,
    cipher: sipherModule
  },
  plugins: [
    loggerPlugins(),
    cipherPlugins()
  ]
})
