// modules
import engineModule from './modules/engine'
import sipherModule from './modules/cipher'
import rsaModule from './modules/rsa'
import dhMudule from './modules/dh'
import blocksModule from './modules/blocks'
import lzwModule from './modules/lzw'
import hashModule from './modules/hash'
import gammModule from './modules/gamm'
import linblockModule from './modules/linblock'

// plugins
import loggerPlugin from './plugins/logger'
import cipherPlugin from './plugins/cipher/cipher'
import rsaPlugin from './plugins/rsa'

export default ({
  strict: true,
  modules: {
    ui: engineModule,
    cipher: sipherModule,
    rsa: rsaModule,
    dh: dhMudule,
    blocks: blocksModule,
    lzw: lzwModule,
    hash: hashModule,
    gamm: gammModule,
    linblock: linblockModule
  },
  plugins: [
    loggerPlugin(),
    cipherPlugin(),
    rsaPlugin()
  ]
})
