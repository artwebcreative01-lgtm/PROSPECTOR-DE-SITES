---
description: Redesenha os sites dos leads com estética premium (lote de 5 ou mais)
argument-hint: "[URLs ou nomes dos leads] — opcional, usa os 5+ melhores de leads.md"
---

Redesenhe as páginas dos leads seguindo a skill `redesign-premium`. Ela é obrigatória — leia a skill ANTES de escrever qualquer HTML.

## Seleção dos clientes

1. Leia `prospector-config.json` e `leads.md` na pasta conectada.
2. Selecione conforme a regra do lead:
   - **Regra A ("site ruim"):** leads com status `novo` mais bem ranqueados — este é o passo que CONSTRÓI antes do e-mail.
   - **Regra B ("empresas que anunciam"):** SOMENTE leads com status `respondeu` (a pessoa respondeu o e-mail de convite pedindo pra ver a prévia). **Nunca redesenhe lead Regra B que ainda não respondeu** — o modelo é construir só pra quem levantou a mão. Se não há nenhum `respondeu`, avise o usuário e pare (rode `/respostas` primeiro).
   - Se `$ARGUMENTS` trouxer URLs ou nomes, use-os (o usuário pode forçar um lead específico).
3. Lote: para a Regra A, **mínimo de 5 por lote** (se houver menos de 5 novos, use todos e avise). A Regra B não tem mínimo — redesenhe quantos responderam, mesmo que seja 1 (é lead quente, não espere juntar lote).
4. Confirme a lista com o usuário antes de começar.

## Para cada cliente do lote

1. **Extração**: abra o site original no Claude in Chrome (o sandbox costuma bloquear fetch direto a esses domínios). Extraia TODO o conteúdo real: textos, serviços, formação/credenciais, endereço, telefone/WhatsApp, e-mail, redes sociais, horários, paleta de cores e — OBRIGATÓRIO — as URLs reais do logo e das fotos (via JavaScript no navegador: colete `img.currentSrc` de todas as imagens; se forem lazy-load, role a página até o fim antes de coletar). Tire um screenshot do site original para referência.
2. **Redesign**: aplique a skill `redesign-premium` na íntegra. Regra de ouro: NADA inventado — é uma nova versão da página do cliente, não uma página nova. O logo original e as fotos originais DEVEM aparecer na página nova (se o cliente não tem site/logo, use composição tipográfica — nunca invente logo).
3. **Salvar** na pasta conectada, com o nome do cliente no arquivo para fácil identificação:
   - `sites/[slug]/[slug].html` — a página final (arquivo único, autocontido, responsivo)
   - `sites/[slug]/[slug]-editor.html` — a MESMA página com a camada de edição visual injetada antes de `</body>` (script completo em `references/editor-visual.md` da skill `redesign-premium`). Gere SEMPRE, sem esperar o usuário pedir.
4. **Comparador (OBRIGATÓRIO — não é opcional)**: crie/atualize `comparar.html` na RAIZ da pasta conectada usando o template pronto `references/comparador-template.html` da skill `redesign-premium`: copie o template, substitua `__CLIENTES__` pelo array JSON dos clientes (formato documentado no rodapé do próprio template). Se `comparar.html` já existir, LEIA o array atual e acrescente os novos clientes no topo — nunca perca os antigos.
5. **Atualizar** o status do lead em `leads.md` para `redesenhado` e o `dashboard.html` (skill `dashboard-leads`): `status: redesenhado`.

## Checklist de saída (bloqueante)

Antes de apresentar qualquer resultado ao usuário, confirme que TODOS estes arquivos existem — se faltar algum, gere-o agora:

- [ ] `sites/[slug]/[slug].html` para CADA cliente do lote
- [ ] `sites/[slug]/[slug]-editor.html` para CADA cliente do lote
- [ ] `comparar.html` na raiz, com abas para TODOS os clientes do lote

Um redesign sem o editor ou sem o comparador é entrega incompleta — o usuário usa o comparador na proposta e no conteúdo dele.

## Verificação do lote

Antes de encerrar, para cada página criada: renderize/revise o HTML procurando textos placeholder esquecidos, links quebrados, seções vazias e problemas de contraste. Todos os CTAs devem apontar para o WhatsApp ou contato REAL do cliente.

## Saída (TRAVADA — siga exatamente este formato)

A entrega final ao usuário DEVE conter, nesta ordem, sem exceção:

1. **Cards de arquivo apresentados no chat** (via ferramenta de apresentação de arquivos): o `comparar.html` PRIMEIRO, depois a página e o editor de cada cliente. Se você não apresentou o card do `comparar.html`, a entrega está errada — apresente antes de escrever qualquer resumo.
2. **Resumo de 1 linha por cliente** (o que melhorou).
3. **Confirmação do dashboard**: frase explícita "Dashboard atualizado: [N] leads com status redesenhado" após atualizar o banco/dashboard conforme a skill `dashboard-leads` (se a pasta ainda não tem dashboard, CRIE-o agora pela skill — pasta nova nunca é desculpa para pular).
4. Orientação curta: `comparar.html` = antes/depois lado a lado · `[slug]-editor.html` = editar textos/imagens · próximo passo `/publicar`.
   - **Regra B:** depois de `/publicar`, NÃO mande cold mail — o lead já respondeu. Responda no PRÓPRIO e-mail dele (mesma thread) com o link da prévia: "Preparei como prometi, olha aí: [link]". Contato quente, pessoal. Aí atualize o status para `fechado` quando avançar pra proposta comercial/preço.

É PROIBIDO encerrar a resposta sem os itens 1 e 3. Se qualquer arquivo do checklist não existir, gere-o antes de responder.
