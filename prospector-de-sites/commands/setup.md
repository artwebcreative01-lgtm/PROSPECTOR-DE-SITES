---
description: Configura o plugin — assinatura, preferências e conexão com a VM KVM2 da Hostinger via SSH (roda uma vez)
---

Configure o ambiente do Prospector de Sites. Siga esta ordem:

## 1. Pasta de trabalho

Verifique se há uma pasta do usuário conectada. Se não houver, peça para conectar uma pasta (ex.: "Clientes") usando a ferramenta de solicitação de pasta — tudo (config, leads e sites criados) será salvo nela para persistir entre sessões.

## 2. Verificar config existente

Procure `prospector-config.json` na pasta conectada. Se existir, mostre um resumo (sem exibir a senha) e pergunte o que o usuário quer atualizar. Se não existir, colete os dados abaixo.

## 3. Dados do usuário (perguntar via AskUserQuestion / formulário)

Colete:

- **Assinatura da proposta**: nome completo, como quer se apresentar (ex.: "Designer de páginas de alta conversão") e WhatsApp/telefone de contato.
- **Nichos padrão de prospecção**: sugira nutricionistas, psicólogos, advogados e psiquiatras como ponto de partida, mas deixe o usuário editar livremente.
- **Cidade/região padrão**.
- **Leads qualificados por busca**: padrão 10.
- **Modo de envio da proposta**: padrão "criar rascunho no Gmail para revisão" (recomendado). Alternativa: enviar direto.

## 4. Conexão com a VM KVM2 (Hostinger)

Este fork não usa HostGator, FTP nem cPanel — publica direto na VM KVM2 da Artweb (Hostinger, Nginx) via chave SSH. Não há senha nenhuma pra coletar ou guardar.

- Confirme que o bloco `hosting` existe em `prospector-config.json` com `sshAlias` (`hostinger-kvm2`), `webroot` (`/var/www/demo.artwebcreative.com.br/prospect`), `baseUrl` (`https://demo.artwebcreative.com.br/prospect`) e `script` (caminho do `publicar-kvm2.sh`). Se não existir, crie com esses valores padrão.
- Confirme que o alias SSH `hostinger-kvm2` está configurado em `~/.ssh/config` do usuário e que a chave funciona (`ssh hostinger-kvm2 "echo ok"`). Se não estiver, isso é responsabilidade da equipe de infra da Artweb (fora do escopo deste plugin) — avise o usuário e pare aqui.
- O bloco `hostgator` do config é legado — mantenha vazio, nunca peça esses dados ao usuário.

## 5. Salvar e testar

Salve tudo em `prospector-config.json` na pasta conectada, neste formato:

```json
{
  "assinatura": { "nome": "", "apresentacao": "", "whatsapp": "" },
  "prospeccao": { "nichos": ["nutricionistas", "psicologos", "advogados", "psiquiatras"], "cidade": "", "leadsPorBusca": 10 },
  "envio": { "modo": "rascunho" },
  "hosting": { "provedor": "kvm2", "sshAlias": "hostinger-kvm2", "webroot": "/var/www/demo.artwebcreative.com.br/prospect", "baseUrl": "https://demo.artwebcreative.com.br/prospect", "script": "scripts/publicar-kvm2.sh" },
  "hostgator": { "usuario": "", "dominio": "", "servidor": "", "senha": "", "pastaBase": "clientes", "_obs": "NAO USADO — Artweb publica na KVM2 via SSH (bloco 'hosting'). Manter vazio." }
}
```

Teste a conexão seguindo a skill `deploy-hostgator` (agora KVM2/SSH): publique uma página `teste.html` simples e informe a URL pública ao usuário. Se o teste falhar, diagnostique o alias SSH e a chave antes de concluir.

## 6. Dashboard inicial

Siga a seção "Setup" da skill `dashboard-leads`: copie `dashboard-server.py` e `iniciar-dashboard.bat` para a raiz da pasta conectada, crie o banco `prospector.db` (schema da skill) e gere o `dashboard.html` do template. Explique ao usuário: duplo clique em `iniciar-dashboard.bat` abre o painel completo em http://localhost:8765 com edição/exclusão salvando no banco (requer Python no Windows; sem ele, o dashboard.html abre no modo leitura).

## 7B. Entregar o manual

Copie `manual.html` da pasta do plugin para a pasta conectada (sobrescrevendo versão antiga), mais o iniciador do dashboard certo (`iniciar-dashboard.bat` ou `.command`). Não há mais publicador local do Windows/Mac pra instalar — o deploy roda direto do sandbox via SSH (skill `deploy-hostgator`). Apresente o `manual.html` ao usuário com a frase: "Esse é o seu manual — guarda ele que responde 90% das dúvidas."

## 7. Encerrar

Confirme o que foi salvo e explique o ciclo (guiando SEMPRE o próximo passo ao fim de cada comando): `/prospectar` → `/redesenhar` → `/publicar` → `/proposta`, com `/editor` opcional para ajustes manuais e o `dashboard.html` como painel de controle de tudo.
