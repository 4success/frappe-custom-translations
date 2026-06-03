# 🇧🇷 Traduções pt-BR para Frappe v16

Ferramentas, arquivos e fluxo de trabalho para revisar, validar e distribuir traduções pt-BR para apps do ecossistema Frappe.

Este repositório foi pensado para quem quer manter overrides de tradução com mais consistência, rastreabilidade e compatibilidade com o formato gettext usado no Frappe v16.

## 📚 Projetos cobertos

- `frappe/frappe`
- `frappe/erpnext`
- `frappe/crm`
- `frappe/helpdesk`

## ✨ O que você encontra aqui

- regras e orientações do projeto em `AGENTS.md`
- configuração do OpenCode em `opencode.json`
- subagentes customizados em `.opencode/agents/`
- comandos customizados em `.opencode/commands/`
- scripts auxiliares em `scripts/`
- área de trabalho das traduções em `translations/`

## 🚀 Fluxo recomendado

1. Baixe o template `main.pot` e o baseline `pt_BR.po` das branches configuradas em `translations/projects.json`:

   ```bash
   python3 scripts/fetch_po.py --all
   ```

   Use `--branch` apenas como override manual para um projeto ou rodada específica. O fluxo padrão respeita os pins versionados em `translations/projects.json`.

2. Divida um projeto em lotes menores para revisão. Por padrão, o split é incremental: ele gera apenas entradas presentes no `main.pot` que ainda não têm tradução no baseline upstream `pt_BR.po` nem na memória incremental local `output/<project>/messages.po`.

   ```bash
   python3 scripts/split_po.py --project frappe --size 150
   ```

   Para revisar o arquivo inteiro, use `--all`:

   ```bash
   python3 scripts/split_po.py --project frappe --size 150 --all
   ```

3. Abra o OpenCode neste diretório e use os agentes ou comandos customizados para revisar os lotes. Para revisão em lote, use o fluxo com `translation-orchestrator`, `po-translator`, `po-reviewer` e `po-validator`.

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

7. Atualize a pasta `output/` com os artefatos finais prontos para distribuição e com a memória incremental local:

   ```bash
   python3 scripts/sync_output.py --project frappe
   ```

   Para sincronizar todos os projetos, rode `python3 scripts/sync_output.py` sem `--project`.

8. Use o arquivo exportado no ambiente de destino:

   ```text
   output/<project>/messages.po
   ```

## 📦 Artefatos principais

O pipeline gera o override mínimo em:

```text
translations/projects/<project>/overrides/messages.po
```

Depois do `sync_output.py`, a cópia pronta para distribuição fica em:

```text
output/<project>/messages.po
```

- `source/main.pot` contém as strings reais do app na branch configurada
- `source/pt_BR.po` contém o baseline de traduções upstream
- `merged/pt_BR.po` contém o resultado completo revisado, reconstruído a partir do `main.pot` com overlays do baseline upstream, traduções já publicadas em `output/` e novas revisões em `reviewed/`
- `overrides/messages.po` contém apenas as entradas diferentes do baseline upstream `pt_BR.po`
- `output/<project>/messages.po` é a cópia sincronizada do override, pronta para distribuição e usada como memória incremental nas próximas revisões
- para distribuição em um app customizado, o arquivo em `output/<project>/messages.po` costuma ser a melhor opção

## 🛠️ Como aplicar os overrides em um ambiente

Os arquivos `overrides/messages.po` foram pensados para serem distribuídos dentro de um app customizado do Frappe.

### Abordagem recomendada

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

### ✅ Resultado esperado

Depois da compilação e da limpeza de cache:

- as strings alteradas devem aparecer em pt-BR na interface
- o app customizado deve funcionar como camada de override para os apps core
- novas revisões podem ser publicadas reaproveitando o mesmo fluxo

### ⚠️ Observações importantes

- no Frappe v16, arquivos `.po` são o formato padrão de tradução
- o app customizado funciona como camada de override para apps como Frappe, ERPNext, CRM e Helpdesk
- se uma tradução não mudar imediatamente, limpe o cache novamente e recarregue a interface
- se uma string ainda não bater, verifique o `msgid` exato, o `msgctxt` quando existir, e as entradas de plural

## 🤖 Atalhos do OpenCode

- `/bootstrap-po`
- `/prepare-project frappe 150`
- `/translate-batch translations/projects/frappe/batches/batch-001.po`
- `/review-batch translations/projects/frappe/reviewed/batch-001.po`
- `/build-overrides frappe`

## 📤 Exportar para `output/`

Para evitar esquecer a sincronização dos artefatos finais, use:

```bash
python3 scripts/sync_output.py
```

Ou apenas para um projeto específico:

```bash
python3 scripts/sync_output.py --project frappe
```

Esse script:

- copia `translations/projects/<project>/overrides/messages.po` para `output/<project>/messages.po`
- atualiza as contagens em `output/README.md`
- mantém a pasta `output/` alinhada com os overrides mais recentes

## 🗂️ Estrutura de saída

Depois do bootstrap, cada projeto usa esta estrutura:

```text
translations/projects/<project>/
  source/main.pot
  source/pt_BR.po
  batches/batch-001.po        # quando houver pendências
  reviewed/batch-001.po
  merged/pt_BR.po
  overrides/messages.po
```

## 🧭 Notas

- mantenha as branches em `translations/projects.json` alinhadas com o ambiente de produção; `frappe` e `erpnext` estão pinados em `version-16`
- `crm` e `helpdesk` atualmente usam `main` por padrão em `translations/projects.json`, porque esses repositórios publicam traduções compatíveis com v16 nessa branch
- entradas em `reviewed/` que não existem mais em `source/main.pot` são ignoradas no merge/output por padrão
- strings fixadas diretamente no código não entram no fluxo gettext enquanto não existirem no `main.pot`
- edite o glossário em `translations/glossary.md` antes de grandes rodadas de revisão
- o arquivo sincronizado em `output/<project>/messages.po` é o artefato que você pode distribuir dentro do seu app customizado
- depois de atualizar os lotes revisados, rode `scripts/merge_batches.py`, `scripts/build_overrides.py`, `scripts/check_po.py` e `scripts/sync_output.py` antes de exportar os arquivos para importação
