---
description: Escreve e envia (ou cria rascunho) da proposta por e-mail via Gmail — adapta o e-mail à regra do lead (A: página pronta · B: análise + convite)
argument-hint: "[nome do cliente ou todos]"
---

Envie propostas por e-mail seguindo a skill `proposta-email`. O e-mail muda conforme o campo `regra` do lead.

## Passos

1. Leia `prospector-config.json` (assinatura e modo de envio) e `leads.md`.
2. Determine os destinatários por `$ARGUMENTS`, ou pelo status certo de cada regra:
   - **Regra A**: leads com status `publicado` que ainda não receberam proposta (a página já está no ar).
   - **Regra B**: leads com status `novo` (ainda não abordados) — a página NÃO existe ainda e é intencional; o e-mail é de análise + convite.
   Somente leads com e-mail confirmado — para os demais, informe que a abordagem fica manual via WhatsApp (ofereça o texto adaptado).
3. Para cada cliente, escreva o e-mail seguindo a skill `proposta-email` na variante da regra dele:
   - **Regra A** → seção "REGRA A" da skill: elogio + defeito específico + o ÚNICO link, a página-capa publicada (`https://demo.artwebcreative.com.br/prospect/[slug]/proposta.html`, montada de `hosting.baseUrl` + `hosting.base`). Se a capa não foi publicada, publique-a antes (skill `deploy-hostgator` = SSH KVM2).
   - **Regra B** → seção "VARIANTE B" da skill: e-mail de análise + convite, usando os `achados` da prospecção, o argumento de autoridade (tráfego frio precisa de credibilidade imediata) e a `automação sugerida` do nicho. **SEM link e SEM anexo** — o CTA é responder "quero ver"; a página só é construída depois da resposta.
   NUNCA mencione preço em nenhuma das duas.
4. **Checklist anti-spam (bloqueante)**: valide contra a checklist da variante certa na skill `proposta-email`. Regra B exige zero link/anexo, uma automação só, um único pedido. Reescreva até passar.
5. Envio conforme o modo do config:
   - **rascunho** (padrão): crie o rascunho pelo conector do Gmail e avise que está pronto para revisão.
   - **enviar direto**: se o conector não oferecer envio, use o Claude in Chrome no Gmail web, ou crie o rascunho e avise.
6. Atualize `leads.md` e o dashboard com o status certo + data de envio:
   - Regra A → `proposta enviada`.
   - Regra B → `email enviado`.

## Saída

Resuma: quantos e-mails criados/enviados e para quem. Na Regra A, cite o link da capa de cada um. Na Regra B, lembre que a página vem depois e só para quem responder. Próximos passos: `/respostas` verifica quem respondeu (dá pra agendar diário) e `/followup` cuida de quem está 3+ dias sem responder. **Na Regra B, quem responder vira alvo de `/redesenhar` + `/publicar`.**
