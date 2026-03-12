# Glossary

Update this file before large review passes. Keep one preferred translation per recurring term.

## Core Terms

| English | Preferred pt-BR | Avoid | Notes |
| --- | --- | --- | --- |
| Customer | Cliente | Consumidor | Default business term |
| Supplier | Fornecedor | Supridor | |
| Lead | Lead | Potencial cliente | Keep in English unless project context requires otherwise |
| Opportunity | Oportunidade | Chance | CRM funnel |
| Task | Tarefa | Atividade | Use `Atividade` only when original is `Activity` |
| Workflow | Fluxo de trabalho | Workflow | |
| Submit | Enviar | Submeter | Use `Submeter` only if required by existing convention |
| Company | Empresa | Companhia | |
| Issue | Chamado | Problema | Helpdesk default |
| Ticket | Chamado | Ticket | Helpdesk default |

## Decision Log

- Use this section to record deliberate wording decisions that should remain stable across projects.
- Add project-specific notes when a term intentionally differs between `frappe`, `erpnext`, `crm`, and `helpdesk`.
- `frappe/ecosystem`: `Role` -> `Perfil`; avoid `Funcao` and `Papel` in admin/UI context.
- `frappe/ecosystem`: `Read` -> `Leitura` when a single shared gettext entry also covers permission/UI uses; prefer safety over status-specific `Lido`.
- `frappe/ecosystem`: keep product or feature names in English when they behave as proper names in the UI, including `Desk`, `Onboarding`, and `Helpdesk`.
- `frappe/ecosystem`: file action `Upload` -> `Carregar`; use `Enviar` only when the action is clearly about sending, not selecting/transferring a file.
- `erpnext`: sales-side `Quotation` -> `Orcamento`; buying-side `Request for Quotation` / `Supplier Quotation` stay in the `Cotacao` family.
- `erpnext`: `Rate` -> `Preco`; avoid `Valor` when the source is `Rate` so it does not collapse with `Amount`.
- `erpnext`: keep `BOM` as `BOM`; avoid `LDM` in manufacturing strings.
- `erpnext`: `CWIP` / `Capital Work in Progress` -> `imobilizado em andamento (CWIP)`.
- `erpnext`: `Bank Clearance` -> `compensacao bancaria`.
- `erpnext`: `Subscription` -> `Assinatura`.
- `erpnext`: `Write Off` -> `baixa`; avoid `abatimento` in accounting UI.
- `erpnext/manufacturing`: `Work Order` -> `Ordem de Trabalho`; avoid `Ordem de Servico`.
- `frappe`: docstatus `Submitted` -> `Enviado`; keep consistency with existing workflow/state vocabulary unless a source string is explicitly more technical.
- `frappe`: workflow/action `Amend` / `amend` -> `Retificar`; avoid mixing with `Corrigir` or `Alterar` for the formal document action.
- `frappe`: `Background Workers` -> `Processos em segundo plano`; avoid keeping `workers` in English in user-facing admin text.
- `frappe`: database/transaction `Commit` -> `Confirmar`; prefer this wording in current UI unless a future string explicitly exposes low-level transaction semantics.
- `frappe`: protocol identifiers such as `Client Secret Basic` and similar OAuth/OpenID labels stay in English when they match standard names.
- `frappe`: field type or UI identifier `Fold` stays `Fold`; avoid translating it as `Dobrar` in form-builder strings.
- `frappe/ecosystem`: `Workspace` -> `Área de trabalho`; keep the accent in the full family (`Configurações da área de trabalho`, `Tema da área de trabalho`, `Ícone da área de trabalho`).
- `erpnext`: `Party` / `Party Account` -> `Cadastro` / `Conta do cadastro`; avoid `Terceiro` and `Parceiro` as the default neutral ERP term.
- `erpnext`: `Stock Entry` -> `Movimento de estoque`; avoid alternating with `Lancamento de estoque`.
- `erpnext`: `Shipment` -> `Remessa`; use `Expedicao` or `Embarque` only when the source/context is explicitly narrower.
- `erpnext`: keep `UOM` in English as the canonical UI abbreviation; avoid mixing with `UDM`.
- `erpnext`: keep `VAT` in English in international/fiscal labels; avoid forcing `IVA` as the default.
- `erpnext`: prefer expanded `Work in Progress` translation when possible; keep `WIP` only where the source already uses the sigla or space is constrained.
- `erpnext`: official Incoterm names such as `Delivered At Place`, `Delivered At Place Unloaded`, and `Delivered Duty Paid` stay in English.
- `erpnext/accounts`: `Dunning` -> `Cobranca`; use `Carta de cobranca` for `Dunning Letter`.
- `erpnext/loyalty`: `Collection Rules` / `Collection Factor` -> `Regras de acumulo` / `Fator de acumulo`; avoid the `colecao` family in loyalty strings.
- `crm`: `Deal` -> `Negocio`; keep funnel/commercial vocabulary in pt-BR rather than preserving `Deal` in English.
- `crm`: `Workday` -> `Dia de trabalho`; avoid `Dia util` unless the source clearly refers to business-day calendar logic.
- `crm`: compounds with `Lead` should keep the anglicism and pluralize naturally in pt-BR, e.g. `Origens de leads`, `Status de leads`.
