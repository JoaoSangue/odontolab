# Odontolab

PoC criado para apresentação na disciplina de Projeto Orientado a Objeto

## Requisitos

* Usar uma estrutura em MVC
* Apresentar ao menos padrões de projeto
* Respeitar os princípios de SOLID

## Descrição dos casos de uso

A descrição dos requisitos no formato de minimundo pode ser encontrado em [MiniMundo.md](MiniMundo.md)

## Requisitos

* make
* Python 3.10

## Como usar

O Makefile providencia todas os comandos necessários para preparar as dependencias e executar o PoC.

### Ambiente virtual

Crie o ambiente virtual onde as dependências do Python serão instaladas com o comando:

```bash
$ make create-env
```

### Dependências

Instale as dependências com o comando:

```bash
$ make install-requirements
```

### Execução

Execute a aplicação com o comando:

```bash
$ make run
```
