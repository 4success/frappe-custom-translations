# Traduções pt-BR para Frappe v16

Este repositório reúne um fluxo de trabalho para revisar, validar e distribuir traduções pt-BR para apps do ecossistema Frappe.

O foco atual é nestes projetos:

- `frappe/frappe`
- `frappe/erpnext`
- `frappe/crm`
- `frappe/helpdesk`

O objetivo é produzir arquivos de override mínimos, prontos para uso em um app customizado, mantendo consistência terminológica e compatibilidade com o formato gettext usado no Frappe v16.

## O que você encontra aqui

- regras e orientações do projeto em `AGENTS.md`
- configuração do OpenCode em `opencode.json`
- subagentes customizados em `.opencode/agents/`
- comandos customizados em `.opencode/commands/`
- scripts auxiliares em `scripts/`
- área de trabalho das traduções em `translations/`

## Fluxo recomendado

1. Baixe os arquivos originais `pt_BR.po` da branch correspondente:

   ```bash
   python3 scripts/fetch_po.py --all --branch version-16
   ```

2. Divida um projeto em lotes menores para revisão:

   ```bash
   python3 scripts/split_po.py --project frappe --size 150
   ```

3. Abra o OpenCode neste diretório e use os agentes ou comandos customizados para revisar os lotes.

4. Una novamente os lotes revisados em um único arquivo:

   ```bash
   python3 scripts/merge_batches.py --project frappe
   ```

5. Gere um arquivo mínimo de override contendo apenas as entradas alteradas:

   ```bash
   python3 scripts/build_overrides.py --project frappe
   ```

6. Valide o resultado:

   ```bash
   python3 scripts/check_po.py --project frappe
   ```

7. Use o arquivo gerado no ambiente de destino:

   ```text
   translations/projects/<project>/overrides/messages.po
   ```

O arquivo `merged/pt_BR.po` contém o resultado completo revisado. Já `overrides/messages.po` contém apenas as entradas que diferem do arquivo-fonte original e, por isso, é o artefato mais indicado para distribuição.

## Como aplicar os overrides em um ambiente

Os arquivos `overrides/messages.po` foram pensados para serem distribuídos dentro de um app customizado do Frappe.

Abordagem recomendada:

1. Crie ou reutilize um app customizado no ambiente de destino.

2. Coloque o arquivo de override no diretório de locale do app usando o código do idioma:

   ```text
   your_app/locale/pt_BR.po
   ```

3. Se o ambiente precisar de overrides de mais de um produto, combine os arquivos relevantes em um único `pt_BR.po`, preservando a estrutura do gettext, contextos, formas de plural, placeholders e HTML.

4. Garanta que o app customizado esteja instalado no site de destino.

5. Compile as traduções para que a aplicação carregue o catálogo gettext atualizado.

6. Limpe o cache da aplicação após a compilação.

7. Garanta que o idioma do usuário ou do site esteja configurado como `pt-BR` ou `pt_BR`.

### Observações importantes

- No Frappe v16, arquivos `.po` são o formato padrão de tradução.
- O app customizado funciona como camada de override para apps core como Frappe, ERPNext, CRM e Helpdesk.
- Se uma tradução não mudar imediatamente, limpe o cache novamente e recarregue a interface.
- Se uma string ainda não bater, verifique o `msgid` exato, o `msgctxt` quando existir, e as entradas de plural.

## Atalhos do OpenCode

- `/bootstrap-po version-16`
- `/prepare-project frappe 150`
- `/translate-batch translations/projects/frappe/batches/batch-001.po`
- `/review-batch translations/projects/frappe/reviewed/batch-001.po`
- `/build-overrides frappe`

## Estrutura de saída

Depois do bootstrap, cada projeto usa esta estrutura:

```text
translations/projects/<project>/
  source/pt_BR.po
  batches/batch-001.po
  reviewed/batch-001.po
  merged/pt_BR.po
  overrides/messages.po
```

## Notas

- Mantenha a branch alinhada com o ambiente de produção, normalmente `version-16`.
- `crm` e `helpdesk` atualmente usam `main` por padrão em `translations/projects.json`, porque esses repositórios publicam traduções compatíveis com v16 nessa branch.
- Edite o glossário em `translations/glossary.md` antes de grandes rodadas de revisão.
- O arquivo de override é o artefato que você pode distribuir dentro do seu app customizado.
- Depois de atualizar os lotes revisados, rode `scripts/merge_batches.py`, `scripts/build_overrides.py` e `scripts/check_po.py` antes de exportar os arquivos para importação.
