
## E se o Pitágoras fosse um moderninho?
*E se a gente pudesse mostrar pra todo mundo as maravilhas da matemática?*
Retornando ao passado para aproximadamente 535 A.C. nos encontramos com o grande
filósofo matemático Pitágoras que naquela época estava pensando em largar tudo e desistir
de seu trabalho. Com isso, o nosso retorno ao passado trouxe um enorme desafio, que irá
revolucionar o mundo, mas para isso precisei provar ao grande filósofo que tudo aquilo
que ele tinha construído até o momento era algo promissor e por isso ele deveria continuar.

### Eis que nasce esse projetinho, o *PythaGeek*!
Pensando na melhor maneira de você ver o funcionamento, foi feito uma documentação com seus comportamentos no Postman!
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/86ab90f08b3c810715ed)

### Ele contém três rotas, sendo:

 - PythaOp()
 Que é onde ele vai pegar os parâmetros( os catetos) necessários para fazer a conta.
 Mas pera ai ***PI PI PI*** 🚓 🚓 
 Se você não preencher os espaços com números, não vai retornar a conta! Afinal, um triangulo precisa de dois catetos, né? 🔺 

> numA:  *primeiro cateto*
> numB:  *segundo cateto*

 - ListResult()
 É onde você vê a sua última continha pra não perder de vista, afinal, todo mundo ás vezes esquece, não é?

- ListResults()
Aqui é onde você vê as dez últimas operações dentro de uma listinha, se não, fica difícil decorar tudo 🙈

## Deu vontade de experimentar?
PythaGeek foi feito em VueJS com Buefy para frontend, e Python 3.9 com FlaskRestful de backend.
Então, se você quiser experimentar a API , tenha Python junto com virtualenv instalado e atualizado.
```

pip install virtualenv

```
### Configurando a máquina.
Já que o ambiente está em sandbox( ou seja, sem a necessidade de muitas instalações pois está tudo remoto no projetinho) basta seguir:
Se for Linux, com a pasta **./pythageek_web** aberta, digite:
```
 source env/bin/activate
```
Windows:
```
env/Scripts/activate
```
E então rodar o projetinho com:
```
python app.py
```
E acessar com http://localhost:8000/theory para fazer as continhas.
http://localhost:8000/last_results para ver as últimas continhas!
![](https://64.media.tumblr.com/tumblr_lsm7vvTjDR1qe36qq.gif)
# O frontend :construction: :no_entry_sign:
Infelizmente não pôde ser concluído a tempo, mas dá pra dar uma olhadinha nele!
Foi criado até um logo pra remeter ao nosso moderníssimo Pitágoras.
![Imgur](https://i.imgur.com/DSRPyPL.png)
**Você precisa de Vue-CLI para acessar adequadamente, não se esqueça!**

## client

### Configurando a máquina.
```
npm install
```

### Compilando!
```
npm run serve
```
E acessar http://localhost:8000/
# Progresso ![Imgur](https://i.imgur.com/1tyiTCv.png)
 
 - [x] Criação do Projeto 🎉
 - [x] Criação da API Restful com Flask
 - [x] Rota de POST
 - [x] 2 Rotas de GET
 - [x] Pausa para um cházinho 🍵
 - [x] Documentação e testes com Postman
 - [x] Criação do projeto em frontend
 - [x] Menu de navegação
 - [x] Página sobre Pitágoras
 - [x] Página da operação matemática(~~não funciona~~) :construction:
 - [ ] Página de resultados
 - [ ] Usar EletronJS

 Foi usado um sistema de emojis para apontar os progressos no commit, acho divertido e fácil de identificar! Você pode checar aqui: [GITmoji](https://gitmoji.dev/)


