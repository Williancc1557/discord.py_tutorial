# Como Iniciar!

primeiramente, **instale o módulo do discord.py.** Instale utilizando o seguinte comando no cmd:

```
python -m pip install discord.py
```

Após isso, **importe o modulo do discord na sua instância** escrevendo o seguinte:

```python
import discord
```

# Preparações

Vamos nos **preparar para começar produzir comandos?** Então vamos lá!


**setar o prefixo** é essencial para a criação de nosso bot.
Então vamos criar a seguinte variável:

```py
bot = discord.Bot(command_prefix='w!')
```

No caso o prefixo escolhido por mim foi `w!`.

Após isso, **precisamos colocar o token(identificação)** do bot:

```python
bot.run('token')
```

No lugar do `token`, coloque o token do seu bot.

***A partir desse momento já podemos iniciar o nosso bot.***

# Primeiro Comando!

Pronto para fazer o seu **primeiro comando?** Vamos lá!

**todo comando possui no seu início:** @bot.command()

Então entre o seu prefixo que aqui denominei como `bot` e seu token coloque o seguinte comando:

```python
@bot.command()
async def teste(ctx):
    await ctx.send('olá mundo')
```

Toda função assíncrona de um comando deve possuir no início o `ctx` - Ele é o contexto do comando!

colocamos o `await ctx.send` com a seguinte função:

O `await` é obrigatório por causa da função assíncrona.
O `ctx` tem a função de indentificar o local onde vai ser enviado a mensagem!

O `send` traduzindo para o português significa **enviar**

***Executando o comando no discord:***
Digite o prefixo e o nome da função juntos. Aqui no caso seria `w!teste`


Não entendeu? Ou tem mais dúvidas? Entre no discord: 


