// modules
import engineModule from './modules/engine'
import sipherModule from './modules/cipher'
import rsaModule from './modules/rsa'

// plugins
import loggerPlugin from './plugins/logger'
import cipherPlugin from './plugins/cipher/cipher'
import rsaPlugin from './plugins/rsa'

export default ({
  strict: true,
  modules: {
    ui: engineModule,
    cipher: sipherModule,
    rsa: rsaModule
  },
  plugins: [
    loggerPlugin(),
    cipherPlugin(),
    rsaPlugin()
  ]
})
