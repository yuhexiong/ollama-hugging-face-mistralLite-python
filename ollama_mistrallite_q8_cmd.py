# Check if GPU is available, expect to show "GPU is available: /device:GPU:0"
import tensorflow as tf

if tf.config.list_physical_devices('GPU'):
    print('GPU is available: {}'.format(tf.test.gpu_device_name()))
else:
    print('GPU is not available')

# Install Ollama and run it in the background
!curl -fsSL https://ollama.com/install.sh | sh
!ollama serve > rocama.log 2>&1 &

# Check Ollama version, expect to show "ollama version is 0.2.5"
!ollama --version

# Install Hugging Face and download model
!pip install huggingface-hub
!huggingface-cli download \
  TheBloke/MistralLite-7B-GGUF \
  mistrallite.Q8_0.gguf \
  --local-dir downloads \
  --local-dir-use-symlinks False

# Create model in Ollama
!ollama create ollama_mistrallite_Q8 -f Modelfile

# Check created models in Ollama
!ollama list

# Example API usage to generate text
!curl -X POST http://127.0.0.1:11434/api/generate -d '{ "model": "ollama_mistrallite_Q8", "prompt":"請用繁體中文介紹MistralLite-7B-GGUF" , "stream": false }'
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