---
description: Publica as páginas redesenhadas na VM KVM2 (Nginx) da Artweb, via SSH. Substitui o publicar original (HostGator/FTP).
argument-hint: "[nome do cliente ou todos]"
---

# /publicar — versão Artweb KVM2 (Hostinger VPS)

Publica as páginas do prospect na VM KVM2 da Artweb, servida pelo Nginx em
`demo.artwebcreative.com.br`. **Não usa FTP, cPanel nem o publicador local do Windows.**
Autenticação é por chave SSH (bloco `hosting` do `prospector-config.json`) — os campos
`hostgator` são ignorados.

## Destino

- Servidor: alias SSH `hostinger-kvm2` (root@2.24.82.107, chave já configurada)
- Webroot: `/var/www/demo.artwebcreative.com.br/prospect/[slug]/`
- URL pública: `https://demo.artwebcreative.com.br/prospect/[slug]/`

## Passos

1. Leia `prospector-config.json` (bloco `hosting`: `sshAlias`, `webroot`, `baseUrl`).
2. Determine o que publicar: `$ARGUMENTS` (um cliente ou "todos"), ou liste as páginas com
   status `redesenhado` em `leads.md` e pergunte.
3. **Gere a página-capa de cada cliente**: preencha `references/capa-proposta-template.html`
   (skill `proposta-email`) com os dados do lead + a assinatura do config e salve como
   `sites/[slug]/proposta.html`. É ela que vai no e-mail de proposta.
4. **Publique cada cliente** rodando o script de deploy bundlado no plugin (uma vez por slug):
   ```bash
   bash "${CLAUDE_PLUGIN_ROOT}/scripts/publicar-kvm2.sh" [slug]
   ```
   Ele envia a landing (`[slug].html` → `index.html`) e a capa (`proposta.html`), copia
   subpastas de assets, ignora o `[slug]-editor.html` e ajusta as permissões pro Nginx servir.
   Rode a partir da pasta conectada (onde fica `sites/`).
5. **Verificação HTTPS (bloqueante)**: abra `https://demo.artwebcreative.com.br/prospect/[slug]/`
   e a capa `.../proposta.html` — confirme que ambas carregam com cadeado válido (o certificado
   do `demo.artwebcreative.com.br` já cobre o path, então o HTTPS é automático). Link `http://`
   NUNCA vai para o cliente.
6. Atualize `leads.md` e o banco do dashboard (skill `dashboard-leads`): status `publicado` +
   a URL pública nova.

## Saída

Liste, por cliente: URL da landing e URL da capa (`.../proposta.html`), ambas testadas em https.
Sugira o próximo passo: `/proposta` para enviar os e-mails.

## Observações

- Um prospect por pasta. Para republicar, rode o mesmo comando (sobrescreve).
- Se o script falhar por SSH (timeout/host unreachable), verifique o alias `hostinger-kvm2`
  em `~/.ssh/config` e a chave — não caia para FTP/HostGator, que não existem nesta infra.
- O script está em `scripts/publicar-kvm2.sh` dentro deste plugin (auto-contido); há também
  uma cópia de referência em `C:/Usuarios/trabalho/system/prospector-kvm2/`.
