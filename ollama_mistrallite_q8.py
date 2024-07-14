# Check if GPU is available
import tensorflow as tf

if tf.config.list_physical_devices('GPU'):
    print('GPU is available: {}'.format(tf.test.gpu_device_name()))
else:
    print('GPU is not available')

# Install Ollama and run it in the background
!curl -fsSL https://ollama.com/install.sh | sh
!ollama serve > rocama.log 2>&1 &

# Check Ollama version
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
!curl -X POST http://127.0.0.1:11434/api/generate -d '{ "model": "ollama_mistrallite_Q8", "prompt":"請問中文介紹你自己" , "stream": false }'
# get response {"model":"ollama_mistrallite_Q8","created_at":"2024-07-14T11:49:22.453653574Z","response":"我是ChatGPT，一個高度智慧的聊天機器人。我可以回答您的問題、幫助您解決問題、創造故事和撰寫代碼。我會盡力地回答你所有關於中文的詞彙，但在詳細的討論中文語法上或創作性質上可能需要更多的時間和鏈結。我希望您喜歡我，並繼續與我交流！","done":true,"done_reason":"stop","context":[523,28766,2521,28730,4983,28730,313,28766,28767,1838,28789,28766,416,28730,4983,28730,313,28766,3685,13,28801,13,30539,31142,28991,29019,30739,234,183,188,29383,29159,29957,28789,28766,28706,322,28730,313,28766,3409,28766,2521,28730,4983,28730,313,28766,28767,489,11143,28789,28766,416,28730,4983,28730,313,28766,3685,13,28801,13,29242,28971,18165,28777,6316,28924,28969,30070,29366,29184,30882,233,136,170,28914,31600,29354,30672,29180,29086,28944,29242,29052,29074,29034,30620,29689,28914,31142,31054,29041,232,188,174,30278,29689,29386,31515,31142,31054,29041,232,140,184,29925,31063,29339,29131,233,149,179,232,178,174,29314,30946,28944,29242,30332,234,158,164,29588,29146,29034,30620,29383,29163,28998,31085,30800,28991,29019,28914,235,172,161,232,192,156,28924,29926,29010,235,172,182,31451,28914,235,171,145,31677,28991,29019,30321,29095,29054,29355,232,140,184,29089,29261,235,182,173,29054,29052,29084,29259,29059,29250,29292,28914,29607,29996,29131,236,146,139,30486,28944,29242,30655,30606,29689,30754,233,176,164,29242,28924,31439,234,188,191,234,189,143,31138,29242,29471,29642,29267],"total_duration":5205807616,"load_duration":14093071,"prompt_eval_count":64,"prompt_eval_duration":111686000,"eval_count":145,"eval_duration":5038373000}