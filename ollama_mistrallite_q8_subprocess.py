import tensorflow as tf
import subprocess
import requests
import json

# Check if GPU is available, expect to show "GPU is available: /device:GPU:0"
if tf.config.list_physical_devices('GPU'):
    print('GPU is available: {}'.format(tf.test.gpu_device_name()))
else:
    print('GPU is not available')

# Install Ollama and run it in the background
subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True)
subprocess.Popen("ollama serve > rocama.log 2>&1 &", shell=True)

# Check Ollama version, expect to show "ollama version is 0.2.5"
ollama_version = subprocess.check_output("ollama --version", shell=True).decode().strip()
print(ollama_version)

# Install Hugging Face and download model
subprocess.run("pip install huggingface-hub", shell=True)
print('start install mistrallite.Q8_0.gguf')
subprocess.run("huggingface-cli download TheBloke/MistralLite-7B-GGUF mistrallite.Q8_0.gguf --local-dir downloads --local-dir-use-symlinks False", shell=True)
print('install mistrallite.Q8_0.gguf ok')

# Create model in Ollama
subprocess.run("ollama create ollama_mistrallite_Q8 -f Modelfile", shell=True)

# Check created models in Ollama
ollama_list = subprocess.check_output("ollama list", shell=True).decode().strip()
print(f'Created models:\n{ollama_list}')

# Example API usage to generate text
url = "http://127.0.0.1:11434/api/generate"
payload = {
    "model": "ollama_mistrallite_Q8",
    "prompt": "請用繁體中文介紹MistralLite-7B-GGUF",
    "stream": False
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to generate text: {response.status_code}, {response.text}")
# get response 
# {
#   "model":"ollama_mistrallite_Q8",
#   "created_at":"2024-07-14T12:50:19.157498611Z",
#   "response":"MistralLite-7B-GGUF是一種高效率的翻譯模型，可以將英文文本轉換為繁體中文。它使用了由Hugging Face開發的Transformer架構，並且培訓在大量的英文和繁體中文資料上，使其能夠產生高品質的翻譯結果。",
#   "done":true,
#   "done_reason":"stop",
#   "context":[523,28...],
#   "total_duration":2244659961,
#   "load_duration":7821835,
#   "prompt_eval_count":74,
#   "prompt_eval_duration":108984000,
#   "eval_count":59,
#   "eval_duration":2086399000
# }