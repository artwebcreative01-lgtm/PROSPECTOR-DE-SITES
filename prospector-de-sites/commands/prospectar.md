---
description: Busca no Google Maps negócios bem avaliados e gera a lista de leads — escolha a regra na hora (site ruim OU empresas que anunciam)
argument-hint: "[nicho] [cidade] — opcional, usa os padrões do config"
---

Prospecte leads qualificados seguindo a skill `prospeccao-maps`.

## 0. Escolha da regra (SEMPRE perguntar antes de buscar)

Antes de qualquer busca, pergunte ao usuário (via AskUserQuestion) qual regra usar nesta rodada. As duas mudam o critério de qualificação E o fluxo depois:

- **Regra A — "Site ruim" (constrói-primeiro):** negócio bem avaliado que TEM site, mas o site é ruim. Fluxo: `/prospectar` → `/redesenhar` (constrói) → `/publicar` → `/proposta` (manda a página pronta). É a regra clássica.
- **Regra B — "Empresas que anunciam" (e-mail-primeiro):** negócio bem avaliado que PAGA anúncio e tem site ruim **ou não tem site**. Fluxo: `/prospectar` → `/proposta` (e-mail de análise + convite, sem página pronta) → `/respostas` → **só então** `/redesenhar` + `/publicar` **para quem respondeu**. Economiza: só se redesenha quem levantou a mão.

Marque cada lead gerado com o campo `regra: A` ou `regra: B` — os comandos seguintes leem isso pra saber o fluxo. Se o usuário passar a regra em `$ARGUMENTS` (ex.: "regra B"), não pergunte.

## Preparação

1. Leia `prospector-config.json` na pasta conectada. Se não existir, oriente a rodar `/setup` primeiro.
2. Determine nicho e cidade: use os argumentos `$ARGUMENTS` se informados; senão, pergunte ao usuário qual dos nichos padrão do config usar (e confirme a cidade). O usuário SEMPRE pode trocar nicho e cidade na hora.
3. Leia `leads.md` na pasta conectada (se existir) para saber quais negócios já foram avaliados — estes devem ser EXCLUÍDOS da nova busca.

## Execução

Use as ferramentas do Claude in Chrome (carregue via ToolSearch se necessário) para abrir a Pesquisa Google e executar o fluxo da skill `prospeccao-maps` correspondente à regra escolhida:

### Comum às duas regras
- Buscar "[nicho] em [cidade]"; avaliar até 25 estabelecimentos ou até bater a meta de leads do config (padrão 10), o que vier primeiro.
- Filtro financeiro (eliminatório em ambas): nota ≥ 4.7 + avaliações ≥ 40. Reprovou → pula.
- E-mail público é OBRIGATÓRIO nas duas regras (a abordagem é por e-mail). Sem e-mail → descarta com motivo.
- Coletar sempre: nome, nota, nº de avaliações, telefone, **WhatsApp em formato 55DDDnúmero**, e-mail, URL do site (ou "sem site").

### Se Regra A — "site ruim"
- Eliminatórios: sem site / site fora do ar / diretório de terceiros → pula; site bom → pula. Só qualifica site ATIVO porém ruim (2+ problemas da skill).
- Registrar o motivo objetivo pelo qual o site é ruim (vai na proposta).

### Se Regra B — "empresas que anunciam"
- **Confirmar que anuncia** (eliminatório) em pelo menos UMA fonte pública, nesta ordem, parando na 1ª confirmação: (1) rótulo `Patrocinado`/`Anúncio` no Google (Maps e Busca); (2) Biblioteca de Anúncios da Meta — `https://www.facebook.com/ads/library` (país Brasil, busca pelo nome/Instagram); (3) Centro de Transparência do Google Ads — `https://adstransparency.google.com` (região Brasil). Não confirmou anúncio em nenhuma → descarta.
- Aceita site ruim **OU sem site** (os dois qualificam — o sem-site é o lead mais quente: paga tráfego sem destino próprio).
- **Análise para o e-mail:** se tem site, registrar 2+ achados objetivos de melhoria (skill); se não tem, registrar os canais atuais e a oportunidade da página própria.
- **Automação do nicho:** escolher a automação mais dolorosa do nicho na tabela da skill `prospeccao-maps` e registrar no campo `automação sugerida` do lead (vai no e-mail).
- Registrar também `fonte da evidência` e `evidência de anúncio` (o que confirmou que anuncia) + `data da busca`.

## Saída — Google Sheets + dashboard + cópia local

1. **Google Sheets**: salve os leads numa PLANILHA DO GOOGLE via conector do Google Drive (`create_file` com `contentMimeType: text/csv` e o CSV como `textContent`). Título: `Leads Prospector — [nicho] [cidade]`. Colunas: #, Nome, Nota, Avaliações, E-mail, Telefone, Site atual, **Regra**, Motivo/Achados, **Automação sugerida**, **Evidência de anúncio** (só Regra B), Situação (Qualificado/Descartado + motivo), Status, URL nova. Inclua qualificados E descartados, ranqueados por potencial. Retorne o link ao usuário.
2. **Cópia local `leads.md`** (mesmas colunas) como cópia de trabalho. Em rodadas novas, some aos antigos numa planilha só, nunca duplique.
3. **Dashboard**: crie/atualize `dashboard.html` pela skill `dashboard-leads` — leads novos entram com `status: novo`, descartados com `status: descartado`.

A entrega final DEVE incluir "Dashboard atualizado: [N] leads". Mostre a tabela com o link da planilha e do `dashboard.html`, e sugira o próximo passo conforme a regra:
- **Regra A:** `/redesenhar` para os 5+ melhores leads.
- **Regra B:** `/proposta` para mandar os e-mails de análise+convite (a página vem depois, só pra quem responder).
