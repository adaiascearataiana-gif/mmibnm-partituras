# MM IBNM — gera o indice.json do repositório mmibnm-partituras
# (o app lê esse índice e sabe quais partituras existem, sem ficar testando endereços).
# Rode dentro da pasta ~/mmibnm-partituras sempre que acrescentar ou trocar arquivos.
import os, json
R=os.path.dirname(os.path.abspath(__file__))
PASTAS=['cc','hcc','harpa','cc-intro','musicas']
idx={}
for p in PASTAS:
    d=os.path.join(R,p)
    if os.path.isdir(d):
        idx[p]=sorted(f for f in os.listdir(d) if os.path.splitext(f)[1].lower() in ('.pdf','.jpg','.jpeg','.png'))
json.dump(idx,open(os.path.join(R,'indice.json'),'w',encoding='utf-8'),ensure_ascii=False)
print('✅ indice.json:',', '.join(f'{k}={len(v)}' for k,v in idx.items()) or 'nenhuma pasta')
