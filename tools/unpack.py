#!/usr/bin/env python3
"""Unpack repo.json.zst into a folder (exact bytes). Usage: unpack.py repo.json.zst OUTDIR [manifest.json to verify sha256]"""
import os, sys, json, hashlib, zstandard, base64
z = open(sys.argv[1], 'rb').read()
if len(sys.argv) > 3:
    m = json.load(open(sys.argv[3])); assert hashlib.sha256(z).hexdigest() == m['sha256'], 'sha256 mismatch'
b = json.loads(zstandard.ZstdDecompressor().decompress(z, max_output_size=1 << 31))
assert b.get('format') == 'apex-repo-bundle'
for rel, txt in b['files'].items():
    p = os.path.join(sys.argv[2], rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'wb') as f: f.write(base64.b64decode(txt['base64']) if isinstance(txt, dict) else txt.encode('utf-8'))
print('UNPACKED', len(b['files']), 'files')
