---
name: deploy-hostgator
description: Esta skill deve ser usada ao publicar páginas na VM KVM2 (Hostinger, Nginx) da Artweb — deploy via SSH, criação de pasta por cliente, verificação da URL pública e HTTPS. Acione quando o usuário disser "publicar", "subir o site", "colocar no ar", "deploy" ou rodar /publicar ou o teste de conexão do /setup. NÃO usa HostGator, FTP, cPanel nem publicador local do Windows — essa infra não existe mais neste fork.
---

# Deploy na VM KVM2 (Hostinger)

Publicar páginas em `/var/www/demo.artwebcreative.com.br/prospect/[slug]/` via SSH e garantir a URL pública `https://demo.artwebcreative.com.br/prospect/[slug]/` funcionando.

## Credenciais

Tudo vem de `prospector-config.json` (bloco `hosting`): `sshAlias` (padrão `hostinger-kvm2`), `webroot`, `baseUrl`, `script`. **Não há senha nenhuma** — a autenticação é por chave SSH já configurada no `~/.ssh/config` do usuário (alias `hostinger-kvm2`, `root@2.24.82.107`). O bloco `hostgator` do config é legado, fica vazio e **nunca deve ser usado ou preenchido**.

Se o alias SSH não existir ou a conexão falhar, oriente o usuário a verificar `~/.ssh/config` e a chave — não existe fallback de FTP/cPanel nesta infra.

## Método — Script SSH bundlado (único método, roda no sandbox)

O sandbox do Cowork alcança SSH normalmente (diferente do bloqueio de FTP/cPanel que existia na infra antiga). Rode diretamente:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/publicar-kvm2.sh" [slug] [pasta-ou-arquivo-local]
```

O script (`scripts/publicar-kvm2.sh`):

1. Cria a pasta remota `webroot/prospect/[slug]/` via `ssh hostinger-kvm2 "mkdir -p ..."`.
2. Envia `sites/[slug]/` inteira via `scp -r` (HTML + imagens/assets), ou um único arquivo se `[pasta-ou-arquivo]` apontar pra um arquivo.
3. Garante `index.html`: se não existir, promove `[slug].html` automaticamente.
4. Ajusta permissões (`chmod -R a+rX`) pra o Nginx (`www-data`) conseguir ler os arquivos enviados por `root`.

Se o script falhar (timeout, host unreachable), verifique o alias `hostinger-kvm2` em `~/.ssh/config` e a chave. Não caia para nenhum método de FTP/cPanel — essa infra não existe mais.

## Verificação (obrigatória, após publicar)

1. Abra `https://demo.artwebcreative.com.br/prospect/[slug]/` e a capa `.../proposta.html` — confirme que carregam com conteúdo certo.
2. **HTTPS obrigatório**: o certificado de `demo.artwebcreative.com.br` já cobre o path `/prospect/`, então o HTTPS é automático — não precisa rodar AutoSSL nem nada manual. Se aparecer erro de certificado, é sintoma de outra coisa (verifique o `location`/proxy do Nginx pra esse domínio) — link `http://` NUNCA vai para cliente.
3. Atualize `leads.md` + dashboard (skill `dashboard-leads`) com status `publicado` e a URL.

## Teste de conexão do /setup

Publique um `teste.html` simples ("Funcionou!") com `bash "${CLAUDE_PLUGIN_ROOT}/scripts/publicar-kvm2.sh" teste` e confirme `https://demo.artwebcreative.com.br/prospect/teste/` no ar. Se falhar, diagnostique o alias SSH antes de concluir o setup — não existe fluxo alternativo de instalador local ou FTP.
