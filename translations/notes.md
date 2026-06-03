# Translation Notes

Use this file to capture ambiguous strings, terminology conflicts, and decisions that need human review.

## Template

- Project:
- File:
- `msgid`:
- Current `msgstr`:
- Proposed `msgstr`:
- Why this is ambiguous:
- Decision:

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-011.po`
- `msgid`: `Enabling this will submit documents in background`
- Current `msgstr`: `Ativar isso enviara documentos em segundo plano`
- Proposed `msgstr`: `Ao ativar isso, os documentos serao enviados em segundo plano`
- Why this is ambiguous: `submit` em Frappe pode significar a acao tecnica de submissao do documento, nao apenas enviar.
- Decision: usar a familia `enviar/enviado`; recomendar `Ao ativar isso, os documentos serao enviados em segundo plano`

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-013.po`
- `msgid`: `For Links, enter the DocType as range.\nFor Select, enter list of Options, each on a new line.`
- Current `msgstr`: `Para Links, informe o DocType como intervalo.\nPara Select, informe a lista de opcoes, uma por linha.`
- Proposed `msgstr`: mesmo texto por enquanto
- Why this is ambiguous: `range` no original parece incorreto ou tecnico demais; pode haver problema no texto-fonte.
- Decision: manter como esta por ora; o problema parece estar no texto-fonte e reinterpretar demais aumenta o risco

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-014.po`
- `msgid`: `From User`
- Current `msgstr`: `Do usuario`
- Proposed `msgstr`: `Usuario de origem`
- Why this is ambiguous: o contexto do campo nao basta para escolher entre origem tecnica ou remetente.
- Decision: recomendar `Usuario de origem`; em `Notification Log`, o campo funciona melhor como origem tecnica do que como remetente

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-014.po`
- `msgid`: `Get ...`
- Current `msgstr`: varias entradas com `Obter ...`
- Proposed `msgstr`: possivelmente `Buscar ...`, `Carregar ...` ou `Gerar ...` conforme o caso
- Why this is ambiguous: o verbo natural em pt-BR depende da acao real de cada botao.
- Decision: manter as traducoes atuais por ora nas entradas ambiguas e ajustar apenas quando houver contexto local suficiente; nao criar regra unica para `Get`

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-014.po`
- `msgid`: `Genderqueer`
- Current `msgstr`: `Genderqueer`
- Proposed `msgstr`: manter em ingles ou padronizar se houver convencao previa
- Why this is ambiguous: termo de identidade sensivel; precisa seguir eventual padrao ja adotado no projeto.
- Decision: manter em ingles por ora; e a opcao mais segura sem convencao interna mais ampla

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-016.po`
- `msgid`: `Info`
- Current `msgstr`: `Informações`
- Proposed `msgstr`: `Informativo`
- Why this is ambiguous: pode ser rotulo tecnico, categoria visual ou texto comum; o contexto exibido nao fecha a escolha ideal.
- Decision: recomendar `Informativo` quando o uso for a opcao de estilo visual; `Informacoes` fica semantico demais

## Open Notes

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-025.po`
- `msgid`: `Invalid Serial and Batch Bundle` / `Is Short/Long Year` / `Is Opening`
- Current `msgstr`: vazio
- Proposed `msgstr`: `Pacote inválido de número de série e lote` / `É ano curto/longo` / `É abertura`
- Why this is ambiguous: ainda falta padronizar a família `Serial and Batch Bundle` (`pacote` vs `conjunto`), decidir se `Fiscal Year` deve preferir `ano` ou `exercício`, e alinhar `Is Opening` com a família já usada em `lançamento de abertura`.
- Decision: aplicar as traduções acima nesta passada por contexto local, mas revisar se o projeto fechar uma convenção mais ampla.

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-027.po`
- `msgid`: `Joule`, `Kelvin`, `Kg`, `Kip`, `LIFO`, `Lft`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: mistura nomes canonicos de unidade, sigla contábil/metodológica e abreviacao tecnica (`Lft`) em que localizar pode piorar a consistencia ou inventar significado.
- Decision: mantidos vazios nesta passada por seguranca; revisar apenas se o projeto adotar convencao explicita para esses identificadores

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-045.po`
- `msgid`: `SCIO Detail` / `SCO Supplied Item`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: siglas tecnicas internas sem expansao clara no contexto do campo; traduzir arrisca inventar o significado.
- Decision: manter sem traducao por seguranca ate haver definicao funcional oficial

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-048.po`
- `msgid`: `Shipping County`
- Current `msgstr`: `Condado de entrega`
- Proposed `msgstr`: manter como esta por enquanto
- Why this is ambiguous: `county` e divisao administrativa pouco natural em pt-BR e a melhor adaptacao depende do mercado/pais alvo da tela fiscal.
- Decision: manter `Condado de entrega` nesta passada e revisar se o projeto preferir outro termo neutro

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-049.po`
- `msgid`: `Skip Material Transfer to WIP` / `Skip Material Transfer to WIP Warehouse`
- Current `msgstr`: `Ignorar transferência de material para WIP` / `Ignorar transferência de material para o depósito WIP`
- Proposed `msgstr`: manter como esta por enquanto
- Why this is ambiguous: o glossario recomenda expandir `Work in Progress` quando possivel, mas aqui a sigla pode ser a convencao visivel do produto e a area de tela pode pedir brevidade.
- Decision: manter `WIP` por ora; revisar se o projeto padronizar a expansao nesses rotulos

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-036.po`, `batch-038.po`, `batch-039.po`, `batch-040.po`
- `msgid`: `Pint (UK)`, `Pint (US)`, `Pint, Dry (US)`, `Pint, Liquid (US)`, `Pond`, `Pood`, `Pound`, `Pound-Force`, `Pound/Cubic Foot`, `Pound/Cubic Inch`, `Pound/Cubic Yard`, `Pound/Gallon (UK)`, `Pound/Gallon (US)`, `Poundal`, `Psi/1000 Feet`, `Quart (UK)`, `Quart Dry (US)`, `Quart Liquid (US)`, `Private Equity`, `Please enable Use Old Serial / Batch Fields to make_bundle`, `Progress % for a task cannot be more than 100.`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: mistura nomes padronizados de UOM, termo de mercado normalmente mantido em ingles, uma mensagem com identificador code-like (`make_bundle`) e um texto com `python-format` inconsistente no source (`Progress % ...`), em que traduzir aumenta o risco ou quebra a validacao.
- Decision: mantidos vazios nesta passada por seguranca; revisar apenas se surgir convencao explicita do produto ou correcao do source

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-009.po`
- `msgid`: `Bisecting Right ...` / `Bisecting To`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: `bisect` parece tecnico e o contexto funcional nao basta para escolher uma traducao natural e segura em pt-BR.
- Decision: manter sem alteracao por ora ate haver contexto de produto mais claro

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-001.po`
- `msgid`: `A - B` / `A - C`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: sao expressoes de formula/abreviacao em relatorio tecnico; traduzir nao agrega valor e pode quebrar a leitura do relatorio.
- Decision: manter sem alteracao por seguranca

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-021.po`
- `msgid`: `G - D`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: abreviacao de formula em relatorio tecnico sem contexto suficiente para localizar com seguranca.
- Decision: manter sem alteracao por seguranca

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-018.po`, `batch-019.po`, `batch-020.po`, `batch-033.po`, `batch-038.po`
- `msgid`: `Ledger`, `Legal`, `Master`, `Message-id`, `Mx`, `MyISAM`, `Timeless Launchpad`, `Timeless Night`, `login_required`, `nonce`, `old_parent`, `plain`, `s256`, `{0} ${skip_list ? "" : type}`, `{0} ${type}`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: mistura tamanhos padronizados de papel, honorificos, identificadores tecnicos/protocolares, nomes de tema e expressoes JS em que traduzir aumenta o risco.
- Decision: mantidos vazios nesta passada por seguranca; revisar apenas se surgir convencao explicita do produto

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-013.po`
- `msgid`: `Folio`
- Current `msgstr`: `Fólio`
- Proposed `msgstr`: manter como está por enquanto
- Why this is ambiguous: em contexto de tamanho de página/PDF, `Folio` pode funcionar como nome técnico do formato de papel e alguns projetos optam por não localizar esse tipo de rótulo.
- Decision: manter `Fólio` por ora; revisar se o projeto quiser padronizar nomes de formatos de papel em inglês

- Project: frappe
- File: `translations/projects/frappe/reviewed/batch-016.po`
- `msgid`: `Introspection URI`
- Current `msgstr`: `Introspection URI`
- Proposed `msgstr`: manter como está
- Why this is ambiguous: trata-se de rótulo técnico de OAuth/OpenID e traduzir `Introspection` pode colidir com terminologia de protocolo.
- Decision: manter em inglês por segurança terminológica

- Project: crm
- File: `translations/projects/crm/reviewed/batch-008.po`
- `msgid`: `Rolling Response Due` / `Rolling Responses`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: o recurso de SLA reinicia a resposta a cada nova interacao do cliente, mas `rolling` pode pedir `recorrente`, `continua` ou outra formulacao de produto; sem padrao local, qualquer escolha arrisca soar artificial.
- Decision: manter sem traducao por enquanto e revisar quando houver contexto funcional ou decisao terminologica do produto

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-041.po`
- `msgid`: `Raw Material Voucher No` / `Raw Material Voucher Type`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: `Voucher` pode significar `documento`, `comprovante` ou `lancamento` conforme o relatorio.
- Decision: manter sem alteracao por ora ate haver contexto mais claro do uso no relatorio

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-001.po`
- `msgid`: `'From Date' must be after 'To Date'`
- Current `msgstr`: `A 'Data inicial' deve ser posterior à 'Data final'`
- Proposed `msgstr`: manter como está por enquanto
- Why this is ambiguous: o texto-fonte em inglês parece invertido em relação ao sentido esperado; reinterpretar a tradução para “corrigir” o source aumentaria o risco.
- Decision: manter tradução literal/coerente com o original e tratar como provável inconsistência do texto-fonte

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-003.po`
- `msgid`: `Add Quote`
- Current `msgstr`: `Adicionar citação`
- Proposed `msgstr`: manter como está por enquanto
- Why this is ambiguous: neste contexto pode significar citação/frase editorial, não cotação comercial; sem contexto adicional, forçar a família `cotação` seria arriscado.
- Decision: manter `Adicionar citação`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-006.po`
- `msgid`: `Arshin`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteração por ora
- Why this is ambiguous: unidade de medida obscura; não ficou claro se deve permanecer como nome técnico internacional ou receber equivalente localizado.
- Decision: manter sem alteração por ora

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-043.po`
- `msgid`: `Resolution Due`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: em SLA pode funcionar como status, prazo vencido ou rotulo de prazo de resolucao.
- Decision: manter sem alteracao por ora para nao fixar um termo incorreto no fluxo de suporte

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-022.po`
- `msgid`: `H - F` / `I - J` / `I - K`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: parecem marcadores tecnicos de relatorio/formula por faixa de letras; traduzir nao agrega valor e pode atrapalhar a leitura do relatorio.
- Decision: manter sem traducao por seguranca

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-041.po`
- `msgid`: `Raw Material Voucher No` / `Raw Material Voucher Type`
- Current `msgstr`: vazio
- Proposed `msgstr`: `Nº do comprovante de matéria-prima` / `Tipo de comprovante de matéria-prima`
- Why this is ambiguous: `Voucher` no ERPNext pode oscilar entre `comprovante`, `documento` e `lancamento` conforme o relatorio.
- Decision: usar a familia `comprovante` por consistencia com outras entradas de `Voucher No` / `Voucher Type`; revisar se este relatorio adotar outra convencao

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-042.po`
- `msgid`: `Request for`
- Current `msgstr`: vazio
- Proposed `msgstr`: `Solicitar para`
- Why this is ambiguous: como rotulo do campo `warehouse` em `Item Reorder`, o texto-fonte e curto demais e pode pedir formulacoes como `Solicitar para`, `Solicitar de` ou `Solicitar ao atingir` dependendo da UX.
- Decision: usar `Solicitar para` por enquanto e revisar se surgir contexto de tela mais claro

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-043.po`
- `msgid`: `Resolution Due`
- Current `msgstr`: vazio
- Proposed `msgstr`: `Prazo de resolução`
- Why this is ambiguous: em SLA pode representar status, prazo de resolucao ou estado de vencimento, e o source sozinho nao fixa isso.
- Decision: usar `Prazo de resolução` por proximidade com a familia `Response By` / `Resolution Time`; revisar se o produto exigir leitura mais claramente status

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-047.po`
- `msgid`: `Select Job Worker Address`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: `Job Worker` pode pedir `terceirizado`, `prestador` ou outro termo especifico de subcontratacao no projeto.
- Decision: manter sem alteracao por ora ate confirmar a terminologia dominante no modulo

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-048.po`
- `msgid`: `Service Address`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: no contexto de garantia pode ser `endereco de atendimento`, `endereco do servico` ou `endereco da assistencia`.
- Decision: manter sem alteracao por ora

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-049.po`
- `msgid`: `Show in Bucket View`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: `bucket` pode significar `faixa`, `intervalo` ou `periodo`, dependendo do relatorio.
- Decision: manter sem alteracao por ora

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-050.po`
- `msgid`: `Stock Closing Entry`
- Current `msgstr`: vazio
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: o DocType pode pedir `entrada`, `registro` ou `lancamento` de fechamento de estoque conforme a convencao interna.
- Decision: manter sem alteracao por ora

## Consolidated In Glossary

- `frappe/ecosystem`: `Role` -> `Perfil`
- `frappe/ecosystem`: `Read` -> `Leitura` for shared permission/UI entries
- `frappe/ecosystem`: keep `Desk`, `Onboarding`, and `Helpdesk` in English as product/feature names
- `frappe/ecosystem`: `Upload` -> `Carregar` for file actions
- `frappe`: `Submitted` -> `Enviado`
- `frappe`: `Amend` / `amend` -> `Retificar`
- `frappe`: `Background Workers` -> `Processos em segundo plano`
- `frappe`: `Commit` -> `Confirmar`
- `frappe`: OAuth/OpenID protocol identifiers such as `Client Secret Basic` stay in English
- `frappe`: field type/UI identifier `Fold` stays `Fold`
- `erpnext`: `Party` / `Party Account` -> `Cadastro` / `Conta do cadastro`
- `erpnext`: `Stock Entry` -> `Movimento de estoque`
- `erpnext`: `Shipment` -> `Remessa`
- `erpnext`: keep `UOM` and `VAT` in English as canonical labels when applicable
- `erpnext`: prefer expanded translation for `Work in Progress`; keep `WIP` only when needed
- `erpnext`: official Incoterm names such as `Delivered At Place`, `Delivered At Place Unloaded`, and `Delivered Duty Paid` stay in English
- `erpnext/accounts`: `Dunning` -> `Cobranca`; `Dunning Letter` -> `Carta de cobranca`
- `erpnext/loyalty`: `Collection Rules` / `Collection Factor` -> `Regras de acumulo` / `Fator de acumulo`
- `crm`: `Deal` -> `Negocio`
- `crm`: `Workday` -> `Dia de trabalho`
- `crm`: compounds with `Lead` keep the anglicism and pluralize naturally in pt-BR

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-030.po`
- `msgid`: `Minute`
- Current `msgstr`: ``
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: o mesmo `msgid` cobre a unidade de medida `Minute` e tambem o campo singular de ata/reuniao; o contexto agrupado nao permite uma traducao unica sem risco.
- Decision: mantido sem alteracao por ora


- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-028.po`
- `msgid`: `Make`
- Current `msgstr`: `Criar`
- Proposed `msgstr`: `Criar` por enquanto
- Why this is ambiguous: o mesmo `msgid` cobre botoes de acao (`Criar`) e o campo de veiculo `Make`, em que o natural seria `Marca`.
- Decision: mantido `Criar` por cobrir a maioria dos usos; revisar se o projeto quiser separar esse contexto na fonte

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-024.po`
- `msgid`: `Invalid Primary Role`
- Current `msgstr`: ``
- Proposed `msgstr`: `Perfil principal invalido`
- Why this is ambiguous: `Role` ainda nao tem decisao global estavel entre `perfil`, `funcao` ou manutencao do termo tecnico no ecossistema Frappe.
- Decision: ja resolvido no glossario; usar `Perfil principal invalido`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-024.po`
- `msgid`: `Incorrect Check in (group) Warehouse for Reorder`
- Current `msgstr`: ``
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: o texto-fonte parece truncado ou tecnicamente estranho; `Check in` nao deixa claro se se refere a validacao, configuracao ou campo especifico do armazem de grupo para reposicao.
- Decision: manter sem alteracao por ora; o texto-fonte parece truncado ou malformado

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-024.po`
- `msgid`: `Invalid Blanket Order for the selected Customer and Item`
- Current `msgstr`: ``
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: `Blanket Order` ainda nao tem decisao terminologica estavel no projeto; pode ser `pedido em aberto`, `pedido guarda-chuva` ou `contrato aberto`, e a escolha afeta varias telas.
- Decision: manter sem alteracao por ora; precisa de decisao terminologica antes de padronizar

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-001.po`
- `msgid`: `0 - Draft; 1 - Submitted; 2 - Cancelled`
- Current `msgstr`: `0 - Rascunho; 1 - Enviado; 2 - Cancelado`
- Proposed `msgstr`: `0 - Rascunho; 1 - Enviado; 2 - Cancelado`
- Why this is ambiguous: `Submitted` in Frappe docstatus may need a state-specific term beyond glossary-default `Enviar/Enviado`.
- Decision: ja resolvido no glossario; manter `Enviado` para docstatus `Submitted`

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-002.po`
- `msgid`: `Allow Roles`
- Current `msgstr`: translated with `perfis`
- Proposed `msgstr`: `Permitir perfis`
- Why this is ambiguous: `Role` is drifting between `perfil` and `funcao` in framework/admin UI.
- Decision: ja resolvido no glossario; manter a familia `Perfil`

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-003.po`
- `msgid`: `Amend`
- Current `msgstr`: translated with `corrigir/correcao` family in related entries
- Proposed `msgstr`: `Retificar`
- Why this is ambiguous: Frappe workflow may require a stable term such as `corrigir`, `retificar`, or another approved convention.
- Decision: ja resolvido no glossario; usar `Retificar`

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-004.po`
- `msgid`: `Background Workers`
- Current `msgstr`: translated in pt-BR
- Proposed `msgstr`: `Processos em segundo plano`
- Why this is ambiguous: unclear whether to keep technical `workers` in English or standardize as `processos em segundo plano`.
- Decision: ja resolvido no glossario; usar `Processos em segundo plano`

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-006.po`
- `msgid`: `Client Secret Basic`
- Current `msgstr`: translated conservatively
- Proposed `msgstr`: `Client Secret Basic`
- Why this is ambiguous: OAuth/OpenID labels may be better kept in English as protocol identifiers.
- Decision: ja resolvido no glossario; manter em ingles como identificador de protocolo

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-007.po`
- `msgid`: `Commit`
- Current `msgstr`: `Confirmar`
- Proposed `msgstr`: `Confirmar`
- Why this is ambiguous: in system/admin context this likely refers to transaction/database commit, not generic confirmation.
- Decision: ja resolvido no glossario; manter `Confirmar`

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-009.po`
- `msgid`: `Desk Access`
- Current `msgstr`: translated with `Desk` terminology under review
- Proposed `msgstr`: `Acesso ao Desk`
- Why this is ambiguous: `Desk` may be a product term that should remain untranslated across Frappe UI.
- Decision: ja resolvido no glossario; manter `Desk` em ingles

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-010.po`
- `msgid`: `Edit Onboarding`
- Current `msgstr`: translated conservatively
- Proposed `msgstr`: `Editar Onboarding`
- Why this is ambiguous: `Onboarding` may need to stay in English as a product/feature label.
- Decision: ja resolvido no glossario; manter `Onboarding` em ingles

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-031.po`
- `msgid`: `T`
- Current `msgstr`: `T`
- Proposed `msgstr`: `T`
- Why this is ambiguous: contexto `Number system`; nao esta claro se deve permanecer como abreviacao tecnica ou receber forma localizada.
- Decision: manter como esta por ora; sem politica fechada para toda a serie de abreviacoes do sistema numerico

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-032.po`
- `msgid`: `There can be only one Fold in a form`
- Current `msgstr`: `Pode haver apenas um Fold em um formulario`
- Proposed `msgstr`: `Pode haver apenas um Fold em um formulario`
- Why this is ambiguous: `Fold` parece ser um termo tecnico/tipo de campo da interface e pode precisar de padronizacao global.
- Decision: recomendar manter `Fold` em ingles; virar regra de glossario para tipo de campo/identificador tecnico

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-037.po`
- `msgid`: `amend`
- Current `msgstr`: `retificar`
- Proposed `msgstr`: `retificar`
- Why this is ambiguous: termo de workflow do framework; vale decidir se o padrao global deve ser `retificar`, `alterar` ou outro equivalente.
- Decision: ja resolvido no glossario; manter `retificar`

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-026.po`
- `msgid`: `Read`
- Current `msgstr`: `Leitura`
- Proposed `msgstr`: `Leitura`
- Why this is ambiguous: o mesmo `msgid` cobre status de entrega ("Read" = "Lido") e também permissão/ação de interface ("Read" = "Leitura"). O gettext agrupa tudo em uma única entrada.
- Decision: ja resolvido no glossario; manter `Leitura` por ser a opcao mais segura nas entradas compartilhadas de permissao/UI

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-036.po`
- `msgid`: `Weekly Long`
- Current `msgstr`: `Weekly Long`
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: o rótulo isolado não deixa claro se `Long` é nome técnico de fila/processo, frequência estendida ou outro identificador interno do scheduler.
- Decision: manter em inglês por ora para evitar uma localização especulativa

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-034.po`
- `msgid`: `Use % for any non empty value.`
- Current `msgstr`: `Use % for qualquer valor não vazio.`
- Proposed `msgstr`: manter esta forma por ora
- Why this is ambiguous: a entrada está marcada como `python-format`; traduções naturais em pt-BR quebram a validação porque o `%` literal passa a ser interpretado como placeholder inválido.
- Decision: manter a sequência `% for` para preservar a validação gettext; o ideal seria corrigir a marcação ou o texto-fonte

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-042.po`
- `msgid`: `Request for`
- Current `msgstr`: `Solicitar para`
- Proposed `msgstr`: `Solicitacao para`
- Why this is ambiguous: rotulo isolado em `Item Reorder`; o contexto nao deixa claro se aponta para destino, deposito ou outro alvo da solicitacao.
- Decision: recomendar `Solicitacao para`; como rotulo de campo, a forma nominal e mais natural do que o verbo no infinitivo

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-045.po`
- `msgid`: `Sales Incoming Rate`
- Current `msgstr`: `Preco de entrada de vendas`
- Proposed `msgstr`: `Preco de entrada da venda`
- Why this is ambiguous: o campo aparece em documentos de compra e pode indicar um preco vinculado a vendas ou outro conceito tecnico de avaliacao.
- Decision: recomendar `Preco de entrada da venda`; o campo aponta para a taxa vinda da Sales Invoice em transferencias internas

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-045.po`
- `msgid`: `Sales Contributions and Incentives`
- Current `msgstr`: `Contribuicoes e incentivos de vendas`
- Proposed `msgstr`: `Contribuicoes e incentivos de vendas`
- Why this is ambiguous: o contexto pode ser mais especifico de comissoes/incentivos da equipe comercial do que `contribuicoes` em sentido amplo.
- Decision: manter como esta por ora; o contexto nao sustenta forcar `comissoes` sem risco de estreitar o sentido

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-046.po`
- `msgid`: `BOM`
- Current `msgstr`: variando entre `BOM` e `LDM` em lotes antigos
- Proposed `msgstr`: `BOM`
- Why this is ambiguous: o glossario manda manter `BOM`, mas ainda ha heranca de `LDM` em traducoes existentes do projeto.
- Decision: ja resolvido no glossario; harmonizar globalmente em `BOM`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-048.po`
- `msgid`: `Shipment`
- Current `msgstr`: `Remessa`
- Proposed `msgstr`: `Remessa`
- Why this is ambiguous: em fluxos logisticos pode significar `remessa`, `expedicao`, `embarque` ou `entrega`, conforme o papel exato do DocType.
- Decision: ja resolvido no glossario; manter `Remessa` como padrao e usar outras formas so com contexto mais restrito

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-050.po`
- `msgid`: `Stock Entry`
- Current `msgstr`: `Movimento de estoque`
- Proposed `msgstr`: `Movimento de estoque`
- Why this is ambiguous: em ERPs, `Stock Entry` pode ser tratado como `movimento` ou `lancamento`; ambos sao plausiveis para o documento operacional.
- Decision: ja resolvido no glossario; manter `Movimento de estoque`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-011.po`
- `msgid`: `Claimed Landed Cost Amount (Company Currency)`
- Current `msgstr`: traduzido de forma conservadora no lote revisado
- Proposed `msgstr`: `Valor do custo adicional apropriado (moeda da empresa)`
- Why this is ambiguous: `claimed` pode significar apropriado, lancado ou reivindicado conforme o contexto contabil do landed cost.
- Decision: manter `apropriado` por ora; no contexto contabil de landed cost, e a opcao mais segura

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-014.po`
- `msgid`: `Customer LPO` / `Customer LPO No.`
- Current `msgstr`: `LPO do Cliente` / `Nro. da LPO do Cliente`
- Proposed `msgstr`: manter sigla por ora
- Why this is ambiguous: a sigla `LPO` nao esta expandida no contexto e pode ser termo comercial/localizavel ou identificador que deve permanecer em ingles.
- Decision: mantido com `LPO` por ora

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-015.po`
- `msgid`: `Deductee Details`
- Current `msgstr`: revisado com termo fiscal conservador
- Proposed `msgstr`: `Detalhes do Beneficiario da Deducao`
- Why this is ambiguous: termo fiscal/jurisdicional; a forma ideal em pt-BR depende do contexto regional do ERPNext.
- Decision: manter como esta por ora; termo fiscal regional sem equivalente pt-BR seguro no contexto atual

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-016.po`
- `msgid`: `Delivered At Place` / `Delivered At Place Unloaded` / `Delivered Duty Paid`
- Current `msgstr`: traduzidos para pt-BR no lote revisado
- Proposed `msgstr`: manter em ingles como no `msgid`
- Why this is ambiguous: Incoterms podem precisar permanecer com a nomenclatura oficial em ingles, mesmo quando ha traducao descritiva.
- Decision: recomendar manter em ingles como nomes oficiais de Incoterms; virar regra de glossario

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-018.po`
- `msgid`: `Dunning` e correlatos
- Current `msgstr`: padronizados com a familia `cobranca`
- Proposed `msgstr`: `cobranca` por enquanto
- Why this is ambiguous: fluxos financeiros de inadimplencia podem exigir termo juridico/financeiro mais especifico do que `cobranca`.
- Decision: recomendar regra de glossario: `Dunning` -> `Cobranca`; usar `Carta de cobranca` para `Dunning Letter`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-019.po`
- `msgid`: `Excise Entry` / `Excise Page Number`
- Current `msgstr`: traduzidos de forma conservadora no lote revisado
- Proposed `msgstr`: manter em ingles por ora
- Why this is ambiguous: sao termos fiscais regionais/legados e o melhor equivalente pt-BR depende da localizacao fiscal desejada.
- Decision: manter em ingles por ora; sao termos fiscais regionais/legados sem equivalente seguro no contexto atual

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-037.po`
- `msgid`: `Please select a value for {0} quotation_to {1}`
- Current `msgstr`: ``
- Proposed `msgstr`: manter sem alteracao por ora
- Why this is ambiguous: `quotation_to` parece um nome interno de campo vazado na UI; sem contexto adicional, não dá para saber se a frase final deve ser técnica ou natural para o usuário.
- Decision: manter sem alteracao por ora; `quotation_to` parece nome interno de campo vazado na UI

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-037.po`
- `msgid`: `Please select the Multiple Tier Program type for more than one collection rules.`
- Current `msgstr`: `Selecione o tipo de programa de varios niveis para mais de uma regra de colecao.`
- Proposed `msgstr`: `Selecione o tipo de programa com multiplas faixas quando houver mais de uma regra de acumulo.`
- Why this is ambiguous: `collection rules` no contexto de fidelidade pode significar `regras de acumulacao`, `regras de coleta` ou outro termo funcional específico do módulo.
- Decision: recomendar a familia `acumulo`; revisar a frase para `mais de uma regra de acumulo` e consolidar a regra no glossario de loyalty

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-038.po`
- `msgid`: `Process Statement Of Accounts CC`
- Current `msgstr`: ``
- Proposed `msgstr`: `CC do processamento de extrato de contas`
- Why this is ambiguous: a sigla `CC` não tem expansão no contexto exibido; pode significar `carbon copy`, `cost center` ou outro identificador técnico do DocType.
- Decision: manter `CC` e traduzir apenas o restante; sem expansao confiavel no contexto atual

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-038.po`
- `msgid`: `Process Statement Of Accounts Customer`
- Current `msgstr`: `Declaração de Processo de Contas do Cliente`
- Proposed `msgstr`: `Cliente do processamento de extrato de contas`
- Why this is ambiguous: depende de como a família `Process Statement Of Accounts*` será padronizada em pt-BR; pode ser `Cliente do processamento de extrato de contas` ou outra forma orientada a DocType.
- Decision: manter como esta por ora; `Cliente do processamento de extrato de contas` e aceitavel ate haver padrao melhor para a familia de DocTypes

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-031.po`
- `msgid`: `No Outstanding Invoices found for this party`
- Current `msgstr`: `Nenhuma fatura em aberto encontrada para este cadastro`
- Proposed `msgstr`: `Nenhuma fatura em aberto encontrada para este cadastro`
- Why this is ambiguous: `party` em ERPNext pode representar cliente, fornecedor ou outra entidade contabil. Nesta revisao foi usado `cadastro` como termo neutro, mas o projeto pode preferir `terceiro` em contexto financeiro.
- Decision: ja resolvido no glossario; manter `cadastro`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-032.po`
- `msgid`: `Numero has not set in the XML file`
- Current `msgstr`: revisar conforme contexto
- Proposed `msgstr`: `A tag Numero nao foi definida no arquivo XML`
- Why this is ambiguous: `Numero` pode ser nome literal de tag/campo fiscal no XML. Se for literal, convem manter sem acento; se nao for, o natural seria `Numero`/`Numero` localizado conforme a politica do projeto.
- Decision: tratar `Numero` como nome literal de tag/campo; recomendar `A tag Numero nao foi definida no arquivo XML`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-034.po`
- `msgid`: `Party`
- Current `msgstr`: `Cadastro`
- Proposed `msgstr`: `Cadastro`
- Why this is ambiguous: `Party` e um termo funcional generico em ERPNext e colide com `Partner/Sales Partner`. `Cadastro` foi usado como opcao neutra neste lote, mas vale confirmar se o padrao global deve ser `Cadastro`, `Terceiro` ou outro equivalente.
- Decision: ja resolvido no glossario; manter `Cadastro`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-035.po`
- `msgid`: `Permanent Address Is`
- Current `msgstr`: `Endereco permanente e`
- Proposed `msgstr`: `O endereco permanente e`
- Why this is ambiguous: o rotulo-fonte parece truncado e nao deixa claro se descreve tipo de moradia, situacao do endereco permanente ou outra classificacao do cadastro de funcionario.
- Decision: recomendar `O endereco permanente e`; e a leitura mais segura para um rotulo-clausula de campo

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-038.po`
- `msgid`: `Process Statement Of Accounts CC`
- Current `msgstr`: `CC do processamento de extrato de contas`
- Proposed `msgstr`: `CC do processamento de extrato de contas`
- Why this is ambiguous: `CC` nao esta expandido no contexto e pode significar copia de e-mail ou outro identificador tecnico do DocType.
- Decision: manter `CC` e traduzir apenas o restante; sem expansao confiavel no contexto atual

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-039.po`
- `msgid`: `Providing`
- Current `msgstr`: ``
- Proposed `msgstr`: `Prestacao`
- Why this is ambiguous: opcao de `Bank Guarantee Type` sem contexto suficiente para escolher com seguranca entre termos como `Prestacao`, `Emissao` ou outro equivalente juridico-financeiro.
- Decision: recomendar `Prestacao`; faz par mais natural com `Receiving` -> `Recebimento`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-002.po`
- `msgid`: `Accepted Warehouse`
- Current `msgstr`: `Armazem de recebimento`
- Proposed `msgstr`: `Armazem de recebimento`
- Why this is ambiguous: o campo pode significar o armazem do item aceito apos inspecao/recebimento ou outro armazem operacional especifico do fluxo.
- Decision: mantido `Armazem de recebimento` por ora

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-002.po`
- `msgid`: `Account Pay Only`
- Current `msgstr`: `Somente para credito em conta`
- Proposed `msgstr`: `Somente para credito em conta`
- Why this is ambiguous: parece rotulo bancario/cheque do tipo `A/C Payee Only`, mas o `msgid` esta incompleto e sem contexto suficiente.
- Decision: mantido `Somente para credito em conta` por ora

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-008.po`
- `msgid`: `Bin`
- Current `msgstr`: `Bin`
- Proposed `msgstr`: `Bin`
- Why this is ambiguous: e um DocType tecnico de estoque; traduzir para `registro de estoque` perde o nome do objeto, mas manter em ingles exige decisao de terminologia do produto.
- Decision: mantido `Bin` por ora

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-009.po`
- `msgid`: `Blanket Order`
- Current `msgstr`: `Pedido guarda-chuva`
- Proposed `msgstr`: `Pedido guarda-chuva`
- Why this is ambiguous: o termo de ERP pode variar entre `pedido guarda-chuva`, `pedido aberto` e `contrato guarda-chuva` conforme a convencao adotada.
- Decision: manter `Pedido guarda-chuva` por ora; nao promover ao glossario sem mais evidencia de uso do modulo

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-010.po`
- `msgid`: `Catch All`
- Current `msgstr`: `Catch-all`
- Proposed `msgstr`: `Catch-all`
- Why this is ambiguous: em contexto de email, pode ser melhor manter o anglicismo tecnico ou adotar um termo funcional como `endereco coringa` conforme padrao do produto.
- Decision: mantido `Catch-all` por ora

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-051.po`
- `msgid`: `Submit ERR Journals?`
- Current `msgstr`: revisado de forma conservadora no lote
- Proposed `msgstr`: `Enviar lancamentos de ERR?`
- Why this is ambiguous: `ERR` aparece sem expansao no contexto; nao fica claro se deve permanecer como sigla tecnica ou receber traducao descritiva.
- Decision: manter `ERR` em ingles e traduzir apenas a acao; `Enviar lancamentos de ERR?`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-052.po`
- `msgid`: `UOM` e derivados
- Current `msgstr`: revisados com `UOM` neste passe
- Proposed `msgstr`: `UOM`
- Why this is ambiguous: o projeto mistura `UOM` e `UDM` em varios lotes; vale confirmar se a sigla deve permanecer em ingles em toda a UI.
- Decision: ja resolvido no glossario; manter `UOM`

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-057.po`
- `msgid`: `VAT` e rotulos correlatos
- Current `msgstr`: revisados com `IVA` neste intervalo
- Proposed `msgstr`: `VAT`
- Why this is ambiguous: em contextos fiscais internacionais, o projeto pode preferir manter `VAT` em ingles em vez de localizar para `IVA`.
- Decision: ja resolvido no glossario; manter `VAT` em ingles

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-058.po`
- `msgid`: `WIP` / `Work in Progress`
- Current `msgstr`: variacoes entre sigla e expansao
- Proposed `msgstr`: traduzir `Work in Progress` por extenso quando possivel e manter `WIP` quando a fonte usar a sigla
- Why this is ambiguous: a manufatura mistura `WIP` e formas traduzidas; falta decidir se a sigla deve ser preservada ou expandida sistematicamente.
- Decision: ja resolvido no glossario; preferir `Work in Progress` traduzido por extenso quando possivel e manter `WIP` so quando a fonte usar a sigla ou houver restricao de espaco

- Project: `crm`
- File: `translations/projects/crm/reviewed/batch-001.po`
- `msgid`: `Deal` e correlatos
- Current `msgstr`: traduzidos como `Negocio` neste intervalo
- Proposed `msgstr`: `Negocio` por ora
- Why this is ambiguous: o projeto CRM ainda nao tem decisao de glossario para manter `Deal` em ingles ou padronizar como `Negocio` em toda a UI e analytics.
- Decision: ja resolvido no glossario; manter `Negocio`

- Project: `crm`
- File: `translations/projects/crm/reviewed/batch-002.po`
- `msgid`: `At least one valid Workday with Workday, Start Time, and End Time is required`
- Current `msgstr`: revisado com familia `dia de trabalho`
- Proposed `msgstr`: manter por enquanto
- Why this is ambiguous: `Workday` pode ser `dia de trabalho`, `dia util` ou `dia de atendimento` no contexto de SLA/calendario.
- Decision: ja resolvido no glossario; manter `Dia de trabalho`

- Project: `crm`
- File: `translations/projects/crm/reviewed/batch-004.po`
- `msgid`: `Drag & Drop files here or upload from`
- Current `msgstr`: `Arraste e solte arquivos aqui ou envie de`
- Proposed `msgstr`: `Arraste e solte arquivos aqui ou carregue de`
- Why this is ambiguous: o texto-fonte parece incompleto e provavelmente depende de um controle visual/logo apos a frase; sem esse contexto, qualquer complemento fica arriscado.
- Decision: manter `Arraste e solte arquivos aqui ou carregue de` por ora; preserva o fragmento do fonte e alinha `upload` com a regra `Carregar`

- Project: `crm`
- File: `translations/projects/crm/reviewed/batch-006.po`
- `msgid`: compostos com `Lead` (`Lead Sources`, `Lead Statuses`)
- Current `msgstr`: revisados com plural em pt-BR
- Proposed `msgstr`: `Origens de leads`, `Status de leads`
- Why this is ambiguous: falta uma regra de estilo consolidada para compostos com o anglicismo `lead` em singular/plural nos rotulos do projeto.
- Decision: ja resolvido no glossario; manter pluralizacao natural em pt-BR (`Origens de leads`, `Status de leads`)

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-060.po`
- `msgid`: `Party` / `Party Account`
- Current `msgstr`: revisado com `parceiro` neste lote
- Proposed `msgstr`: `Cadastro` / `Conta do cadastro`
- Why this is ambiguous: ERPNext usa `Party` para cliente, fornecedor e outras entidades contabeis; o repositorio ainda oscila entre `cadastro`, `parceiro` e outras formas neutras.
- Decision: ja resolvido no glossario; manter `Cadastro` / `Conta do cadastro`

- Project: `helpdesk`
- File: `translations/projects/helpdesk/reviewed/batch-003.po`
- `msgid`: `Helpdesk`
- Current `msgstr`: `Helpdesk`
- Proposed `msgstr`: `Helpdesk`
- Why this is ambiguous: o nome do workspace/modulo pode soar traduzivel como titulo de UI, mas o restante do projeto preserva `Helpdesk` como nome do produto.
- Decision: ja resolvido no glossario; manter `Helpdesk` em ingles como nome do produto/modulo

- Project: `helpdesk`
- File: `translations/projects/helpdesk/reviewed/batch-006.po`
- `msgid`: `Role`

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-022.po`
- `msgid`: `Open Documents`
- Current `msgstr`: `Documentos abertos`
- Proposed `msgstr`: manter por enquanto
- Why this is ambiguous: no campo `subscribed_documents`, nao fica claro se o sentido e `documentos abertos`, `documentos acompanhados` ou outro nome interno da feature.
- Decision: manter por ora e revisar quando houver contexto funcional mais claro

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-023.po`
- `msgid`: `Password Email Sent`
- Current `msgstr`: `E-mail de senha enviado`
- Proposed `msgstr`: manter por enquanto
- Why this is ambiguous: sem contexto adicional, nao fica claro se e e-mail de redefinicao de senha, envio de credenciais ou outra notificacao ligada a senha.
- Decision: manter por ora

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-025.po`
- `msgid`: `Quoting must be between 0 and 3`
- Current `msgstr`: `O valor de quoting deve estar entre 0 e 3`
- Proposed `msgstr`: manter por enquanto
- Why this is ambiguous: `quoting` e tecnico e o contexto nao mostra se ha termo localizado melhor sem risco.
- Decision: manter o termo tecnico por ora

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-026.po`
- `msgid`: `Reference Owner`
- Current `msgstr`: revisado de forma conservadora no lote
- Proposed `msgstr`: manter por enquanto
- Why this is ambiguous: pode significar tanto o proprietario da referencia quanto o dono do documento referenciado.
- Decision: manter por ora ate haver contexto mais claro

- Project: `frappe`
- File: `translations/projects/frappe/reviewed/batch-027.po`
- `msgid`: `Request Data`
- Current `msgstr`: `Solicitação de dados`
- Proposed `msgstr`: manter por enquanto
- Why this is ambiguous: o mesmo `msgid` cobre rotulo tecnico e tambem titulo/botao de web form; a forma nominal funciona melhor no conjunto, mas o botao isolado poderia pedir verbo.
- Decision: manter `Solicitação de dados` por ora por ser a opcao mais segura para o contexto compartilhado
- Current `msgstr`: `Funcao`
- Proposed `msgstr`: `Perfil`
- Why this is ambiguous: em Frappe/Helpdesk, `Role` pode precisar seguir uma convencao global como `perfil`, `papel` ou manutencao tecnica, e o repositorio ainda nao tem decisao estavel.
- Decision: ja resolvido no glossario; usar `Perfil`

- Project: `helpdesk`
- File: `translations/projects/helpdesk/reviewed/batch-007.po`
- `msgid`: `Upload` e correlatos (`Upload image`, `Upload photo`)
- Current `msgstr`: traduzidos com a familia `Carregar`
- Proposed `msgstr`: `Carregar` e correlatos
- Why this is ambiguous: a UI pode preferir padronizar a acao de arquivo com `Carregar` ou `Enviar`; ambas aparecem como opcoes naturais em pt-BR.
- Decision: ja resolvido no glossario; usar a familia `Carregar`

- Project: `helpdesk`
- File: `translations/projects/helpdesk/reviewed/batch-001.po`
- `msgid`: `% SLA Fulfilled` / `% of tickets created that were resolved within SLA`
- Current `msgstr`: mantidos com inicio `% SLA` / `% of` para preservar validacao
- Proposed `msgstr`: manter as formas atuais conservadoras para preservar a sintaxe
- Why this is ambiguous: as strings-fonte usam `%` inicial em formato que o validador interpreta como placeholder; uma traducao totalmente natural quebra a verificacao automatica.
- Decision: mantida traducao conservadora para preservar a sintaxe

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-002.po`
- `msgid`: `Learn about <a href="https://docs.frappe.io/erpnext/user/manual/en/common_party_accounting" rel="noopener noreferrer">Common Party</a>`
- Current `msgstr`: `Saiba mais sobre <a href="https://docs.frappe.io/erpnext/user/manual/en/common_party_accounting" rel="noopener noreferrer">cadastro comum</a>`
- Proposed `msgstr`: manter por ora
- Why this is ambiguous: a família `Common Party` ainda mistura nome de recurso em inglês e tradução funcional do conceito (`cadastro comum` / `contabilização comum de cadastro`) em outros lotes.
- Decision: manter `cadastro comum` neste lote e revisar quando a convenção do recurso estiver fechada no projeto

- Project: `erpnext`
- File: `translations/projects/erpnext/reviewed/batch-004.po`
- `msgid`: `Source Manufacture Entry` / `Source Stock Entry {0} belongs to Work Order {1}, not {2}. Please use a manufacture entry from the same Work Order.` / `When there are multiple finished goods ({0}) in a Repack stock entry...`
- Current `msgstr`: vazio
- Proposed `msgstr`: `Movimento de fabricação de origem` / `...Use um movimento de fabricação...` / `...o custo básico...`
- Why this is ambiguous: ainda falta consolidar no projeto se `Manufacture Entry` deve seguir a família `movimento` ou `lançamento`, e se `Basic Rate` em custos/estoque deve ficar como `custo básico` ou outra forma estável.
- Decision: usar `movimento de fabricação` e `custo básico` nesta passada por consistência local; revisar se surgir convenção mais ampla
