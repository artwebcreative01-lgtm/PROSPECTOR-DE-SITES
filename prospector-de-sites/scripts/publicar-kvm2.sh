#!/usr/bin/env bash
# publicar-kvm2 — deploy de prospect para a VM KVM2 (Nginx) da Artweb.
# Substitui o /publicar original (HostGator/FTP-cPanel) do plugin prospector-de-sites.
# Compatível com o layout do plugin v0.14.0 (redesign = <slug>.html, capa = proposta.html).
#
# uso:  publicar-kvm2.sh <slug> [pasta-local]
#   <slug>          nome do cliente (ex.: padaria-luz)
#   [pasta-local]   default: sites/<slug>
#
# Publica:
#   <slug>.html (ou index.html) -> index.html   (a landing redesenhada)
#   proposta.html               -> proposta.html (a capa, se existir)
#   subpastas de assets/imagens -> copiadas como estão
# NUNCA publica o *-editor.html (ferramenta interna de edição).
#
# Auth: chave SSH via alias 'hostinger-kvm2' (~/.ssh/config). Nada de senha em config.
set -euo pipefail

SSH_ALIAS="hostinger-kvm2"
WEBROOT="/var/www/demo.artwebcreative.com.br"
BASE="prospect"                                  # pasta-mãe dos prospects no servidor
BASEURL="https://demo.artwebcreative.com.br"

SLUG="${1:-}"
SRC="${2:-sites/$SLUG}"

if [ -z "$SLUG" ]; then
  echo "uso: publicar-kvm2.sh <slug> [pasta-local]" >&2
  exit 1
fi
if [ ! -d "$SRC" ]; then
  echo "erro: pasta '$SRC' nao encontrada" >&2
  exit 1
fi

REMOTE_DIR="$WEBROOT/$BASE/$SLUG"
URL="$BASEURL/$BASE/$SLUG/"

echo "-> publicando '$SLUG' em $URL"
ssh "$SSH_ALIAS" "mkdir -p '$REMOTE_DIR'"

# 1) landing redesenhada -> index.html (aceita index.html OU <slug>.html)
if [ -f "$SRC/index.html" ]; then
  scp "$SRC/index.html" "$SSH_ALIAS:$REMOTE_DIR/index.html"
elif [ -f "$SRC/$SLUG.html" ]; then
  scp "$SRC/$SLUG.html" "$SSH_ALIAS:$REMOTE_DIR/index.html"
else
  echo "erro: nao achei index.html nem '$SLUG.html' em '$SRC'" >&2
  exit 1
fi

# 2) capa da proposta (opcional — é a página que vai no e-mail)
HAS_CAPA=0
if [ -f "$SRC/proposta.html" ]; then
  scp "$SRC/proposta.html" "$SSH_ALIAS:$REMOTE_DIR/proposta.html"
  HAS_CAPA=1
fi

# 3) assets: qualquer subpasta (imagens/etc). Sem subpastas, o glob nao casa e nada acontece.
shopt -s nullglob
for item in "$SRC"/*/; do
  scp -r "$item" "$SSH_ALIAS:$REMOTE_DIR/"
done
shopt -u nullglob

# Nginx (www-data) precisa ler o que foi enviado como root
ssh "$SSH_ALIAS" "chmod -R a+rX '$REMOTE_DIR'"

echo "OK publicado:"
echo "   pagina : $URL"
[ "$HAS_CAPA" = "1" ] && echo "   capa   : ${URL}proposta.html"
