export default {
  deleteSpacesFromText (text) {
    let txt = ''
    for (let i = 0; i < text.length; i++) {
      if (text[i] === ' ') {
        if (i % 2 === 0) {
          if (['я','Z','z'].includes(text[i+1])) {
            txt += String.fromCharCode(text[i+1].charCodeAt(0) - 1)
          } else {
            txt += String.fromCharCode(text[i+1].charCodeAt(0) + 1)
          }
        } else {
          if (['я','Z','z'].includes(text[i-1])) {
            txt += String.fromCharCode(text[i-1].charCodeAt(0) - 1)
          } else {
            txt += String.fromCharCode(text[i-1].charCodeAt(0) + 1)
          }
        }
      } else {
        txt += text[i]
      }
    }
    return txt
  },
  // Привет мир и все все все Пишу секретное сообщениее
  encryptText (text, matr) {
    let bigrams = []
    // Создаем массив биграм
    for (let i = 0, k = 0; i < text.length; i++) {
      if (i % 2 === 0) bigrams.push([])
      bigrams[k].push(text[i])
      if (i % 2 === 1 && i < text.length) k++
    }

    // Проверяем биграмы условию. В биграме не должно быть одинаковых символов
    for (let i = 0, j = 0; i < bigrams.length; i++) {
      let char1 = bigrams[i][0]
      let char2 = bigrams[i][1]

      if (char1 === char2) {
        if (['я','Z','z'].includes(char2)) {
          bigrams[i][0] = String.fromCharCode(char2.charCodeAt(0) - 1)
        } else {
          bigrams[i][1] = String.fromCharCode(char2.charCodeAt(0) + 1)
        }
      }
    }

    let newBigrams = []
    // всЕ ТАЙНОЕ СТАНЕТ ЯВНЫМм   афик
    bigrams.forEach(bigram => {
      let char1 = bigram[0]
      let char2 = bigram[1]
      let newChar1
      let newChar2

      // y - сткроки, x - столбцы
      let coordChar1 = this.findIndex(char1, matr)
      let coordChar2 = this.findIndex(char2, matr)

      if (coordChar1.x == coordChar2.x) {
        if (coordChar1.y < 3) {
          newChar1 = matr[coordChar1.y + 1][coordChar1.x]
        } else {
          newChar1 = matr[0][coordChar1.x]
        }

        if (coordChar2.y < 3) {
          newChar2 = matr[coordChar2.y + 1][coordChar2.x]
        } else {
          newChar2 = matr[0][coordChar2.x]
        }
        
      } else if (coordChar1.y == coordChar2.y) {
        if (coordChar1.x < 29) {
          newChar1 = matr[coordChar1.y][coordChar1.x + 1]
        } else {
          newChar1 = matr[coordChar1.y][0]
        }

        if (coordChar2.x < 29) {
          newChar2 = matr[coordChar2.y][coordChar2.x + 1]
        } else {
          newChar2 = matr[coordChar2.y][0]
        }
       
      } else {
        if (coordChar1.y < coordChar2.y) {
          newChar1 = matr[coordChar1.y][coordChar2.x]
          newChar2 = matr[coordChar2.y][coordChar1.x]
        } else {
          newChar1 = matr[coordChar2.y][coordChar1.x]
          newChar2 = matr[coordChar1.y][coordChar2.x]
        }
      }
      newBigrams.push([newChar1, newChar2])
    })

    let newText = ''
    newBigrams.forEach(bigram => {
      newText += bigram[0]
      newText += bigram[1]
    })
    return newText
  },
  decryptText (text, matr) {
    let bigrams = []
    // Создаем массив биграм
    for (let i = 0, k = 0; i < text.length; i++) {
      if (i % 2 === 0) bigrams.push([])
      bigrams[k].push(text[i])
      if (i % 2 === 1 && i < text.length) k++
    }

    // На всякий случай, если пользователь решит что-нибудь добавить...
    for (let i = 0, j = 0; i < bigrams.length; i++) {
      let char1 = bigrams[i][0]
      let char2 = bigrams[i][1]

      if (char1 === char2) {
        if (['я','Z','z'].includes(char2)) {
          bigrams[i][0] = String.fromCharCode(char2.charCodeAt(0) - 1)
        } else {
          bigrams[i][1] = String.fromCharCode(char2.charCodeAt(0) + 1)
        }
      }
    }

    let newBigrams = []

    bigrams.forEach(bigram => {
      let char1 = bigram[0]
      let char2 = bigram[1]
      let newChar1
      let newChar2

      // y - сткроки, x - столбцы
      let coordChar1 = this.findIndex(char1, matr)
      let coordChar2 = this.findIndex(char2, matr)

      if (coordChar1.x == coordChar2.x) {
        if (coordChar1.y > 0) {
          newChar1 = matr[coordChar1.y - 1][coordChar1.x]
        } else {
          newChar1 = matr[3][coordChar1.x]
        }

        if (coordChar2.y > 0) {
          newChar2 = matr[coordChar2.y + 1][coordChar2.x]
        } else {
          newChar2 = matr[3][coordChar2.x]
        }
        
      } else if (coordChar1.y == coordChar2.y) {
        if (coordChar1.x > 0) {
          newChar1 = matr[coordChar1.y][coordChar1.x - 1]
        } else {
          newChar1 = matr[coordChar1.y][29]
        }

        if (coordChar2.x > 0) {
          newChar2 = matr[coordChar2.y][coordChar2.x - 1]
        } else {
          newChar2 = matr[coordChar2.y][29]
        }
       
      } else {
        if (coordChar1.y < coordChar2.y) {
          newChar1 = matr[coordChar1.y][coordChar2.x]
          newChar2 = matr[coordChar2.y][coordChar1.x]
        } else {
          newChar1 = matr[coordChar2.y][coordChar1.x]
          newChar2 = matr[coordChar1.y][coordChar2.x]
        }
      }
      newBigrams.push([newChar1, newChar2])
    })

    let newText = ''
    newBigrams.forEach(bigram => {
      newText += bigram[0]
      newText += bigram[1]
    })
    return newText
  },
  findIndex (char, matr) {
    let x, y
    matr.forEach((str, index) => {
      let i = str.indexOf(char)
      if (i !== -1) x = i, y = index
    })
    return { x, y }
  }
  /* tempdeleteSpacesFromText (text) {
    let txt = ''
    for (let i = 0; i < text.length; i++) {
      if (text[i] === ' ') {
        if (text[i-1] !== undefined) {
          console.log(text[i-1] === text[i])
          if (text[i-1] === text[i]) {
            if (text[i-1] === 'я' || text[i-1] === 'Z' || text[i-1] === 'z') {
              txt += String.fromCharCode(text[i-1].charCodeAt(0) - 1)
            } else {
              txt += String.fromCharCode(text[i-1].charCodeAt(0) + 1)
            }
          } else {
            txt += text[i-1]
          }
        } else {
          if (text[i+1] === text[i]) {
            if (text[i+1] === 'я' || text[i+1] === 'Z' || text[i+1] === 'z') {
              txt += String.fromCharCode(text[i+1].charCodeAt(0) - 1)
            } else {
              txt += String.fromCharCode(text[i+1].charCodeAt(0) + 1)
            }
          } else {
            txt += text[i+1]
          }
        }
      } else {
        txt += text[i]
      }
    }
    return txt
  } */
}