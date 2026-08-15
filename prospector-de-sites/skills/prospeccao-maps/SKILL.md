---
name: prospeccao-maps
description: Esta skill deve ser usada ao prospectar clientes no Google Maps — buscar negócios bem avaliados com sites ruins, qualificar leads, avaliar qualidade de sites de terceiros e montar a planilha de leads. Acione quando o usuário disser "prospectar", "buscar clientes", "achar leads", "clientes com site ruim" ou rodar /prospectar.
---

# Prospecção no Google Empresas

Encontrar o cliente ouro: negócio que JÁ fatura bem (nota alta, muitas avaliações) mas perde clientes por causa de um site fraco. Não se cria demanda — conserta-se onde o dinheiro está escapando.

## Fluxo (via Claude in Chrome)

1. Abrir `https://www.google.com/search` e buscar `[nicho] em [cidade]`. Usar os perfis exibidos no bloco Empresas como fonte dos dados.
2. Percorrer os resultados um a um, em ordem. Para cada estabelecimento:
   - Abrir o perfil e ler nota, nº de avaliações e link do site.
   - **Filtro 1 — potencial financeiro**: nota ≥ 4.7 E avaliações ≥ 40. Reprovou → próximo.
   - **Filtro 2 — TEM site**: o lead PRECISA ter um site ativo e acessível — a oferta é "uma versão muito melhor do SEU site", e o conteúdo/fotos vêm de lá. Sem site, site fora do ar ou "site" que é só diretório de terceiros/linktree → descartar (registrar o motivo) e seguir.
   - **Filtro 3 — site ruim**: abrir o site em nova aba e avaliar pelos critérios abaixo. Site bom → descartar. Site ativo porém ruim → candidato (falta só o e-mail).
3. Parar ao atingir a meta de leads qualificados (config, padrão 10) ou após avaliar 25 estabelecimentos.
4. Pular estabelecimentos que já estão em `leads.md` (avaliados em buscas anteriores).

## Critérios de site ruim (guardar o motivo específico)

Qualifica como lead se o site (ativo) tiver 2 ou mais destes problemas:

- Layout datado (aparência de template de 10+ anos, fontes de sistema, imagens esticadas/pixeladas)
- Sem CTA claro de agendamento/contato (nenhum botão de WhatsApp ou agenda visível na primeira dobra)
- Domínio gratuito ou hospedado em plataforma alheia (Google Sites, Wix grátis, subdomínio de terceiros com marca da plataforma)
- Não responsivo (quebra no mobile)
- Conteúdo desorganizado: serviços escondidos, sem hierarquia, texto corrido sem seções
- Sem prova social (nenhuma avaliação/depoimento, apesar da nota alta no Google)

O motivo anotado deve ser objetivo e verificável — ele será citado na proposta. Ex.: "domínio redireciona para Google Sites gratuito, template básico, sem CTA de agendamento".

## Coleta por lead

Nome, nota, nº de avaliações, telefone, WhatsApp, e-mail, URL do site, motivo.

**WHATSAPP: capture SEMPRE, separado do telefone.** Fontes, na ordem: botão/link de WhatsApp no site do lead (procure `wa.me/`, `api.whatsapp.com` ou ícone de WhatsApp — extraia o número do link); telefone celular do perfil do Maps (números com 9º dígito são celular no Brasil — assuma WhatsApp). Registre no formato internacional `55 + DDD + número` (ex.: `5511999990000`), pronto pra `wa.me`. O WhatsApp alimenta os botões do dashboard e o plano B de abordagem quando o e-mail não responde.

**E-MAIL É OBRIGATÓRIO.** A proposta vai por e-mail — lead sem e-mail público não fecha o ciclo. Procure nesta ordem: site (rodapé e página de contato), links `mailto:`, home do site da clínica onde atende, busca no Google por "[nome] + email/contato". Se NÃO encontrar e-mail: **descarte o lead, registre na lista de descartados (com o contato que existir, ex. WhatsApp/Instagram) e continue buscando o próximo** até bater a meta. Atenção: "site" que aponta para diretório de terceiros (localtreino, acheioprofissional etc.) não conta como site próprio — descarta pelo Filtro 2.

## Regra B — "Empresas que anunciam" (fluxo e-mail-primeiro)

Alternativa à regra clássica, escolhida no início do `/prospectar`. A tese: quem PAGA anúncio já tem verba e intenção de crescer comprovadas — é o lead mais quente. E quem clica no anúncio chega frio; sem um site forte pra gerar credibilidade imediata, o dinheiro do anúncio vaza. Aqui o e-mail vem ANTES da página: só se redesenha quem responder.

**Qualificação (todos obrigatórios):**
1. Filtro financeiro: nota ≥ 4.7 + avaliações ≥ 40.
2. **Anuncia** — confirmar em ao menos UMA fonte pública, parando na 1ª: (a) rótulo `Patrocinado`/`Anúncio` no Google (Maps e Busca); (b) Biblioteca de Anúncios da Meta `https://www.facebook.com/ads/library` (país Brasil, busca nome/Instagram); (c) Centro de Transparência do Google Ads `https://adstransparency.google.com` (Brasil). Não confirmou → descarta.
3. Site ruim (2+ problemas da lista acima) **OU sem site próprio** — os dois qualificam. Sem site é o lead mais quente (paga tráfego sem destino próprio).
4. E-mail público (obrigatório, como na Regra A).

**Coleta extra da Regra B** (além da coleta comum): `regra: B`, `evidência de anúncio` (o que confirmou + fonte + data), `tipo de presença` (site fraco / sem site), `achados` (2+ pontos objetivos se tem site; canais atuais + oportunidade se não tem), e `automação sugerida` (da tabela abaixo).

### Tabela nicho → automação (escolher a MAIS dolorosa do nicho, uma só)

A automação citada no e-mail deve ser específica e óbvia pro nicho. Escolha uma:

| Nicho | Automação a oferecer (a dor nº 1) |
|---|---|
| Clínicas / saúde (nutri, psi, dentista, fisio, médicos) | Confirmação e lembrete automático de consulta por WhatsApp (reduz falta/no-show) |
| Psicólogos / psiquiatras | Agendamento online + triagem inicial por formulário antes da 1ª sessão |
| Advogados | Formulário de triagem de casos + resposta automática imediata ao lead do anúncio |
| Estética / salão / barbearia | Agendamento com lembrete + reengajamento automático de cliente inativo |
| Academia / estúdio / personal | Captura do lead do anúncio → resposta instantânea no WhatsApp + agendamento de aula experimental |
| Restaurante / food / delivery | Reserva/pedido por WhatsApp com confirmação automática |
| Imobiliária / corretor | Qualificação automática do lead do anúncio + distribuição pro corretor + follow-up |
| Pet (clínica/petshop) | Lembrete de vacina/retorno + agendamento de banho/consulta por WhatsApp |
| E-commerce / loja local | Recuperação de carrinho + resposta automática a dúvida de produto |
| **Qualquer nicho (curinga)** | **Resposta automática em segundos ao lead que vem do anúncio** — o lead pago que espera resposta esfria rápido; responder na hora é o que mais recupera venda |

Na dúvida ou nicho fora da tabela, use o curinga (resposta instantânea ao lead do anúncio) — é universal e conversa direto com a dor de quem anuncia.

## Saída — Google Sheets + leads.md local

Destino principal: PLANILHA DO GOOGLE (via conector do Google Drive: `create_file` com CSV em `textContent` e `contentMimeType: text/csv` — converte automaticamente para Sheets). Título `Leads Prospector — [nicho] [cidade]`; incluir qualificados e descartados, ranqueados por potencial (nota alta + site pior). Entregar o link ao usuário.

Cópia de trabalho local `leads.md` (mesmas colunas) para controle de status, já que o conector do Drive não edita células:

```markdown
| # | Nome | Nota | Aval. | E-mail | Telefone | Site atual | Motivo | Status | URL nova |
```

Status possíveis por regra:
- **Regra A (constrói-primeiro):** `novo` → `redesenhado` → `publicado` → `proposta enviada` → `respondeu` / `sem resposta`.
- **Regra B (e-mail-primeiro):** `novo` → `email enviado` → `respondeu` → `redesenhado` → `publicado` → `fechado` (ou `sem resposta` após o follow-up). Na Regra B só se redesenha lead com status `respondeu`.

Quando um status mudar, regenerar a planilha do Google com os dados acumulados e atualizar o `dashboard.html` (skill `dashboard-leads`). Nunca sobrescrever leads antigos — apenas acrescentar e atualizar.

## Boas práticas

- Trabalhar por região dá vantagem: menos concorrência na oferta e conhecimento local.
- Enquanto o navegador trabalha, não interromper o fluxo com perguntas — só reportar a tabela final.
- Se a Pesquisa Google ou o bloco Empresas pedir login/captcha, pausar e avisar o usuário.
