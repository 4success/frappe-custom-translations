# Output de Overrides pt-BR

Esta pasta contem os arquivos finais de override prontos para uso em outro projeto.

## Estrutura

- `output/frappe/messages.po`
- `output/erpnext/messages.po`
- `output/crm/messages.po`
- `output/helpdesk/messages.po`

## Contagem de entradas

- `frappe`: 5303 entradas
- `erpnext`: 7333 entradas
- `crm`: 1412 entradas
- `helpdesk`: 954 entradas

## O que estes arquivos sao

- Cada `messages.po` contem apenas as entradas alteradas em relacao ao arquivo source do projeto.
- Eles foram gerados a partir dos batches revisados em `translations/projects/<project>/reviewed/`.
- Os arquivos finais foram validados com `python3 scripts/check_po.py --project <project>`.

## Como usar em outro projeto

Use o arquivo do modulo correspondente como base de importacao do seu app/projeto de destino.

Fluxo recomendado:

1. Escolha o modulo que voce quer reaproveitar (`frappe`, `erpnext`, `crm` ou `helpdesk`).
2. Copie o arquivo `output/<project>/messages.po` para o local esperado pelo projeto de destino.
3. Importe ou carregue esse `.po` no mecanismo de traducoes do seu app.
4. Garanta que o locale de destino seja `pt_BR`.
5. Recompile/sincronize traducoes no projeto de destino, se ele exigir esse passo.

## Sugestao de organizacao no projeto de destino

Se o outro projeto usa overrides gettext por app, uma estrutura comum e:

```text
your-app/
  your_app/
    locale/
      pt_BR/
        messages.po
```

Ou, se o projeto separa por modulo, mantenha nomes claros como:

```text
translations/
  frappe-messages.po
  erpnext-messages.po
  crm-messages.po
  helpdesk-messages.po
```

## Observacoes

- Os arquivos foram montados com foco em override minimo, nao como traducao completa do produto.
- As decisoes terminologicas consolidadas estao em `translations/glossary.md`.
- Casos ainda sensiveis ou limitados por contexto continuam documentados em `translations/notes.md`.
- Se o projeto de destino misturar textos de mais de um modulo, voce pode precisar combinar mais de um `messages.po`.

## Verificacao rapida

Antes de importar em outro projeto, confirme:

- o arquivo escolhido corresponde ao modulo certo
- o locale e `pt_BR`
- o sistema de destino aceita gettext `.po`
- placeholders, HTML e pluralizacao foram preservados no processo de importacao
