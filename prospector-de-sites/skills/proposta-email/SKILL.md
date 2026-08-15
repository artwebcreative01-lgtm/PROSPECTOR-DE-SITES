---
name: proposta-email
description: Esta skill deve ser usada ao escrever e enviar a proposta comercial por e-mail para um lead prospectado — e-mail de apresentação da nova versão do site, com rapport e sem preço. Acione quando o usuário disser "enviar proposta", "e-mail para o cliente", "mandar o site para o cliente" ou rodar /proposta ou /followup.
---

# Proposta por e-mail

O e-mail NÃO vende — ele desperta curiosidade e prova trabalho feito. O fechamento (preço, escopo, reunião) acontece na resposta. Um e-mail que parece de vendedor morre no spam; um e-mail que parece de uma pessoa que já trabalhou de graça pro destinatário é aberto e respondido.

## Duas variantes (escolhidas pela regra do lead)

O lead carrega o campo `regra` (A ou B). O e-mail muda conforme ela:

- **Regra A — "site ruim" (fluxo constrói-primeiro):** a página nova JÁ está no ar. O e-mail prova o trabalho feito e o único link é a capa. Use as seções **Princípios**, **Estrutura** e a **Página-capa** abaixo.
- **Regra B — "empresas que anunciam" (fluxo e-mail-primeiro):** ainda NÃO existe página pronta. O e-mail faz a análise, oferta (site + automação do nicho) e convida a ver uma prévia. **Só redesenhamos quem responder.** Use a seção **Variante B** abaixo — ela substitui Estrutura e não tem link nenhum.

---

## VARIANTE B — e-mail de análise + convite (Regra "empresas que anunciam")

Contexto neuro: o lead PAGA por anúncio e mesmo assim perde cliente porque a página de destino é fraca (ou não existe). O gatilho mais forte aqui é **viés de perda** — ele já gasta pra trazer a pessoa, e ela escapa na porta. Não prometa; faça ele SENTIR o vazamento e ofereça fechar a torneira. Um único pedido: responder "quero ver".

### Princípios da Variante B

1. **Elogio verificável + reconhecer o investimento.** Nota real, nº de avaliações, e o fato de ele já anunciar (investe em crescer — isso merece elogio genuíno).
2. **Viés de perda, sem ofender.** O problema não é o profissional — é o dinheiro do anúncio escapando. "Você paga pra trazer o cliente; parte dele se perde na porta de entrada." Concreto, reversível, sem culpa.
3. **Autoridade vende (argumento central).** Quem chega pelo anúncio está FRIO — não te conhece e decide em segundos se confia. Um site forte, com as avaliações e o trabalho à mostra, cria credibilidade imediata; sem isso, o clique pago vira desconfiança e a pessoa desiste. Enquadre o site não como estética, mas como a ponte de confiança que transforma tráfego frio em cliente. Autoridade vende.
4. **Antecipação, não entrega.** Não mande a página (não existe). Ofereça MOSTRAR como ficaria — a prévia é a recompensa que abre a dopamina. Loop aberto.
5. **Oferta dupla, na medida.** Site novo (principal) + **uma** automação específica do nicho (secundária). Nunca listar várias — carga cognitiva mata. Uma frase, a automação mais dolorosa do nicho (ver tabela na skill `prospeccao-maps`).
6. **Um único CTA, custo quase zero:** responder "quero ver". Sem link, sem anexo, sem agenda, sem preço.
7. **Curto e falado.** 140-170 palavras. Leia em voz alta — se travar, reescreve.

### Estrutura da Variante B

- **Assunto** (≤ 60 caracteres, pessoal, cara de gente): `[Nome], vi o anúncio da [Empresa] — posso te mostrar algo?` ou `[Nome], uma ideia rápida sobre a [Empresa]`.
- **P1 — rapport:** onde encontrou (o anúncio) + elogio específico (nota/avaliações) + reconhecer que ele investe em anúncio.
- **P2 — a perda, sem ofensa:** o anúncio traz gente interessada, mas [ela cai num site abaixo do seu atendimento: [motivo específico] / não há um site próprio pra recebê-la — ela para no Instagram e boa parte se perde]. "Você já paga pra trazer o cliente; parte escapa logo na entrada."
- **P3 — oferta + antecipação:** "Posso te mostrar, de graça e sem compromisso, como ficaria uma página feita pra converter quem o seu anúncio traz." + uma frase de automação do nicho ("e dá pra automatizar [automação do nicho] pra você não perder mais tempo nem cliente com isso").
- **P4 — CTA único:** "Quer ver? Responde só 'quero ver' que eu preparo a prévia da sua página e te mando."
- **Assinatura** completa do config (nome, apresentação, WhatsApp).

### Modelo pronto (corpo HTML minimalista — ajuste os [campos])

```html
<p>Oi, [Nome], tudo bem?</p>
<p>Sou [assinatura.nome], [assinatura.apresentacao]. Cheguei na [Empresa] pelo anúncio [no Google/no Instagram] e fui olhar com calma: [nota]★ com [N] avaliações — dá pra ver que quem passa por você sai satisfeito. Empresa com essa reputação e que ainda investe em anúncio é exatamente o tipo de negócio que eu gosto de ajudar.</p>
<p>Reparei numa coisa, e falo como quem quer ajudar, não criticar: seu anúncio traz gente interessada, mas [ela cai num site que não está à altura do seu atendimento ([motivo]) / não existe um site próprio pra recebê-la — ela para no Instagram e boa parte se perde]. E quem chega pelo anúncio ainda não te conhece: decide em segundos se confia. Sem um site forte mostrando suas avaliações e seu trabalho, essa confiança não se forma — e o clique que você pagou vira desconfiança. Autoridade vende. Você já paga pra trazer o cliente; parte dele escapa logo na porta de entrada.</p>
<p>Posso te mostrar — de graça e sem compromisso — como ficaria uma página feita pra converter justamente quem o seu anúncio traz, com a credibilidade que faz a pessoa escolher você na hora. E, se fizer sentido pro seu dia a dia, dá pra automatizar [automação do nicho] pra você não perder mais tempo nem cliente com isso.</p>
<p>Quer ver? Responde só “quero ver” que eu preparo a prévia da sua página e te mando.</p>
<p>Um abraço,<br>[assinatura.nome]<br>[assinatura.apresentacao]<br>[assinatura.whatsapp]</p>
```

### Checklist da Variante B (BLOQUEANTE)

- [ ] **ZERO link e ZERO anexo.** A prévia só existe depois da resposta — o CTA é responder, não clicar. Isso deixa o e-mail ainda mais limpo pro spam.
- [ ] **Primeira linha 100% personalizada** (nome + fato real das avaliações + o anúncio).
- [ ] **A perda é concreta e sem culpa** — o alvo é o dinheiro do anúncio escapando, nunca o profissional.
- [ ] **UMA automação só**, específica do nicho (tabela na skill `prospeccao-maps`). Nunca uma lista.
- [ ] **Um único pedido:** responder "quero ver". Sem preço, sem agenda, sem segundo CTA.
- [ ] **Sem palavras-gatilho** (grátis como isca, promoção, imperdível, urgente, garantido), sem CAIXA ALTA / "!!" / emoji no assunto, assunto ≤ 60 caracteres.
- [ ] **130-160 palavras**, lido em voz alta sem travar.
- [ ] Remetente = Gmail pessoal ativo do usuário; envios 1 a 1.

---

## REGRA A — proposta com página pronta (fluxo constrói-primeiro)

## Princípios

1. **Rapport primeiro.** Abrir com elogio ESPECÍFICO e verificável: a nota no Google, uma avaliação real citada, uma credencial do site. Nunca elogio genérico.
2. **A dor sem ofensa.** Apontar 1-2 defeitos objetivos do site atual como oportunidade ("notei que no celular o site fica difícil de ler"), nunca como crítica ao profissional.
3. **A prova antes do pedido.** O trabalho JÁ está feito e no ar. O link é a proposta.
4. **Zero preço.** Preço só na conversa que a resposta abre.
5. **Zero pressão.** Sem urgência falsa, sem "últimas vagas". Um único CTA: dar uma olhada e responder o que achou.
6. **Curto.** 120-180 palavras. Profissional ocupado não lê e-mail longo de desconhecido.

## Estrutura

- **Assunto**: pergunta pessoal e específica, ≤ 60 caracteres, sem cara de marketing. Ex.: `Dra. [Nome], posso te mostrar uma coisa sobre seu site?` ou `Preparei algo para a [Clínica X]`.
- **Parágrafo 1**: quem encontrou + elogio específico (avaliações/credencial).
- **Parágrafo 2**: observação sobre o site atual (1-2 pontos objetivos).
- **Parágrafo 3**: "preparei uma nova versão, já no ar" + O ÚNICO LINK do e-mail: a página-capa (`.../proposta.html`), que mostra antes e depois lado a lado. Se a capa não existir, linkar a página nova direto.
- **Parágrafo 4**: CTA — abrir no celular também, responder com a impressão.
- **Assinatura**: nome, apresentação e WhatsApp do config (assinatura completa humaniza e reduz suspeita).

## Checklist anti-spam (BLOQUEANTE — rodar antes de criar o rascunho)

Revise o e-mail pronto contra CADA item; se falhar em qualquer um, reescreva antes de criar o rascunho:

- [ ] **1 link só** (a página-capa). Dois links no máximo se incluir o site antigo — nunca mais que isso.
- [ ] **Sem encurtador de URL** (bit.ly e afins = spam na certa). O link é o domínio real, com `https://`.
- [ ] **Link como âncora HTML com texto visível limpo.** O Gmail embrulha TODO link em um redirect próprio (`google.com/url?q=...`) ao salvar — não dá pra impedir, e em corpo de texto puro o embrulho fica VISÍVEL, o que parece golpe. Por isso o rascunho é criado com corpo HTML e o link como âncora: `<a href="https://[dominio]/[pastaBase]/[slug]/proposta.html">https://[dominio]/[pastaBase]/[slug]/proposta.html</a>` — texto visível = a URL limpa montada a partir do config (nunca copiada de outro e-mail). O redirect do Google fica só no href invisível, como em qualquer e-mail do Gmail. Depois de criar, confira o rascunho: o texto visível deve começar em `https://[dominio do config]`.
- [ ] **URL pública limpa e humana.** Monte o link usando `hosting.baseUrl` do config, normalmente `https://demo.artwebcreative.com.br/prospect`, seguido de `[slug]/proposta.html`. Nunca use campos legados de HostGator, FTP ou cPanel.
- [ ] **Sem palavras-gatilho**: grátis, promoção, imperdível, oferta, desconto, clique aqui, 100%, garantido, urgente.
- [ ] **Sem CAIXA ALTA no assunto, sem "!!", sem emoji** no assunto.
- [ ] **Texto simples** — corpo HTML minimalista (só parágrafos e a âncora do link; zero cores, botões, imagens ou anexos) (anexo de desconhecido aumenta score de spam E medo de abrir; a capa no link substitui o preview).
- [ ] **Assunto ≤ 60 caracteres**, formulado como pergunta ou frase pessoal com o nome do negócio.
- [ ] **Primeira linha 100% personalizada** (nome + fato real das avaliações) — filtros de spam e humanos reconhecem template genérico.
- [ ] **Remetente = conta Gmail pessoal ativa do usuário** (já tem SPF/DKIM do Google). Nunca sugerir disparo em massa: os envios são 1 a 1, poucos por dia — padrão humano.

## Envio

- Modo **rascunho** (padrão): criar via conector do Gmail (`create_draft`) com destinatário, assunto e corpo prontos. Avisar o usuário para revisar antes de enviar.
- Modo **enviar direto**: se o conector não suportar envio, abrir o Gmail web via Claude in Chrome, ou criar o rascunho e avisar.
- Nunca enviar para lead sem e-mail confirmado; nesses casos, sugerir contato via WhatsApp com a mesma mensagem adaptada.

## Página-capa (o que o cliente vê ao clicar)

O link do e-mail leva à página-capa gerada no `/publicar` (template em `references/capa-proposta-template.html`): nome do cliente no topo, antes/depois lado a lado e a assinatura do usuário. Ela existe para dar credibilidade ao clique — o cliente vê o próprio negócio, não um link estranho. Exigências: servida em `https://`, personalizada com dados reais, sem pedido de dado pessoal nenhum.

## Depois do envio

Registrar no banco/`leads.md` (status + data) e no dashboard. As respostas são verificadas pelo comando `/respostas` (Gmail via conector) — sugira ao usuário agendar a verificação diária. Follow-up pelo `/followup` após 3+ dias úteis sem resposta (1 único follow-up por lead: curto, gentil, "conseguiu ver a página?").


